"""Ingest MIMIC-IV EHR data"""
import pandas as pd
from pathlib import Path
from typing import Dict, List
import gzip


class MIMICIngester:
    def __init__(self, mimic_dir: Path):
        """
        Initialize with MIMIC-IV data directory
        Note: MIMIC requires credentialed access from PhysioNet
        """
        self.mimic_dir = Path(mimic_dir)
        self.hosp_dir = self.mimic_dir / "hosp"
        self.icu_dir = self.mimic_dir / "icu"
        
    def load_patients(self) -> pd.DataFrame:
        """Load patient demographics"""
        return pd.read_csv(self.hosp_dir / "patients.csv.gz")
    
    def load_admissions(self) -> pd.DataFrame:
        """Load hospital admissions"""
        return pd.read_csv(self.hosp_dir / "admissions.csv.gz")
    
    def load_diagnoses(self) -> pd.DataFrame:
        """Load diagnosis codes"""
        return pd.read_csv(self.hosp_dir / "diagnoses_icd.csv.gz")
    
    def load_procedures(self) -> pd.DataFrame:
        """Load procedure codes"""
        return pd.read_csv(self.hosp_dir / "procedures_icd.csv.gz")
    
    def load_prescriptions(self) -> pd.DataFrame:
        """Load medication prescriptions"""
        return pd.read_csv(self.hosp_dir / "prescriptions.csv.gz")
    
    def load_labevents(self, chunksize: int = 100000) -> pd.DataFrame:
        """Load lab results (large file, use chunking)"""
        return pd.read_csv(self.hosp_dir / "labevents.csv.gz", chunksize=chunksize)
    
    def load_notes(self, chunksize: int = 10000) -> pd.DataFrame:
        """Load clinical notes"""
        notes_path = self.hosp_dir / "discharge.csv.gz"
        if notes_path.exists():
            return pd.read_csv(notes_path, chunksize=chunksize)
        return None
    
    def create_patient_records(self, patient_ids: List[int] = None) -> List[Dict]:
        """Create comprehensive patient records"""
        patients = self.load_patients()
        admissions = self.load_admissions()
        diagnoses = self.load_diagnoses()
        prescriptions = self.load_prescriptions()
        
        if patient_ids:
            patients = patients[patients['subject_id'].isin(patient_ids)]
        
        records = []
        
        for _, patient in patients.iterrows():
            subject_id = patient['subject_id']
            
            # Get patient admissions
            patient_admissions = admissions[admissions['subject_id'] == subject_id]
            
            # Get diagnoses
            patient_diagnoses = diagnoses[diagnoses['subject_id'] == subject_id]
            
            # Get medications
            patient_meds = prescriptions[prescriptions['subject_id'] == subject_id]
            
            record = {
                'patient_id': subject_id,
                'demographics': patient.to_dict(),
                'admissions': patient_admissions.to_dict('records'),
                'diagnoses': patient_diagnoses['icd_code'].tolist(),
                'medications': patient_meds['drug'].unique().tolist()
            }
            
            records.append(record)
        
        return records
    
    def ingest_to_vectordb(self, embedder, vector_db, collection_name: str,
                          batch_size: int = 100, max_patients: int = None):
        """Ingest MIMIC data into vector database"""
        patients = self.load_patients()
        
        if max_patients:
            patients = patients.head(max_patients)
        
        patient_ids = patients['subject_id'].tolist()
        
        stats = {'processed': 0, 'failed': 0}
        
        for i in range(0, len(patient_ids), batch_size):
            batch_ids = patient_ids[i:i+batch_size]
            
            try:
                records = self.create_patient_records(batch_ids)
                
                # Generate embeddings
                embeddings = []
                metadata = []
                
                for record in records:
                    emb = embedder.embed_structured_ehr(record)
                    embeddings.append(emb)
                    
                    metadata.append({
                        'source': 'MIMIC-IV',
                        'patient_id': str(record['patient_id']),
                        'modality': 'EHR',
                        'record_type': 'comprehensive'
                    })
                
                # Insert into vector DB
                vector_db.insert_vectors(collection_name, embeddings, metadata)
                
                stats['processed'] += len(records)
                
            except Exception as e:
                print(f"Error processing batch: {e}")
                stats['failed'] += len(batch_ids)
        
        return stats
