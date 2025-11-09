"""Ingest data from The Cancer Imaging Archive (TCIA)"""
import requests
import os
from pathlib import Path
from typing import List, Dict
import pydicom
from tqdm import tqdm


class TCIAIngester:
    def __init__(self, api_url: str = "https://services.cancerimagingarchive.net/services/v4"):
        self.api_url = api_url
        self.session = requests.Session()
        
    def get_collections(self) -> List[str]:
        """Get list of available collections"""
        url = f"{self.api_url}/TCIA/query/getCollectionValues"
        response = self.session.get(url)
        response.raise_for_status()
        return [item['Collection'] for item in response.json()]
    
    def get_patients(self, collection: str) -> List[str]:
        """Get patients in a collection"""
        url = f"{self.api_url}/TCIA/query/getPatient"
        params = {'Collection': collection}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return [item['PatientID'] for item in response.json()]
    
    def get_series(self, collection: str, patient_id: str) -> List[Dict]:
        """Get imaging series for a patient"""
        url = f"{self.api_url}/TCIA/query/getSeries"
        params = {
            'Collection': collection,
            'PatientID': patient_id
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def download_series(self, series_uid: str, output_dir: Path) -> List[Path]:
        """Download DICOM series"""
        url = f"{self.api_url}/TCIA/query/getImage"
        params = {'SeriesInstanceUID': series_uid}
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        response = self.session.get(url, params=params, stream=True)
        response.raise_for_status()
        
        # Save ZIP file
        zip_path = output_dir / f"{series_uid}.zip"
        with open(zip_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        # Extract DICOM files
        import zipfile
        dicom_files = []
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
            dicom_files = [output_dir / name for name in zip_ref.namelist() 
                          if name.endswith('.dcm')]
        
        zip_path.unlink()  # Remove ZIP
        return dicom_files
    
    def ingest_collection(self, collection: str, output_dir: Path, 
                         max_patients: int = None) -> Dict:
        """Ingest entire collection"""
        print(f"Ingesting collection: {collection}")
        
        patients = self.get_patients(collection)
        if max_patients:
            patients = patients[:max_patients]
        
        stats = {
            'collection': collection,
            'patients': 0,
            'series': 0,
            'files': 0
        }
        
        for patient_id in tqdm(patients, desc="Patients"):
            try:
                series_list = self.get_series(collection, patient_id)
                
                for series in series_list:
                    series_uid = series['SeriesInstanceUID']
                    patient_dir = output_dir / collection / patient_id
                    
                    files = self.download_series(series_uid, patient_dir)
                    
                    stats['series'] += 1
                    stats['files'] += len(files)
                
                stats['patients'] += 1
                
            except Exception as e:
                print(f"Error processing patient {patient_id}: {e}")
                continue
        
        return stats
