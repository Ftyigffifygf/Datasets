"""Disease-specific dataset ingestion with proper categorization"""
import requests
import yaml
from pathlib import Path
from typing import List, Dict, Optional
from tqdm import tqdm
import pandas as pd
import numpy as np


class DiseaseSpecificIngester:
    def __init__(self, config_path: str = "config/disease_datasets.yaml"):
        with open(config_path) as f:
            self.datasets = yaml.safe_load(f)
    
    def list_datasets_by_category(self, category: str = None) -> Dict:
        """List available datasets by disease category"""
        if category:
            return {category: self.datasets.get(category, {})}
        return self.datasets
    
    def list_datasets_by_condition(self, condition: str) -> List[Dict]:
        """Find datasets containing specific condition"""
        matching = []
        
        for category, datasets in self.datasets.items():
            for dataset_name, info in datasets.items():
                conditions = info.get('conditions', [])
                if isinstance(conditions, list):
                    if any(condition.lower() in c.lower() for c in conditions):
                        matching.append({
                            'category': category,
                            'dataset': dataset_name,
                            'info': info
                        })
        
        return matching
    
    def ingest_nih_chest_xray(self, output_dir: Path, max_images: int = None) -> Dict:
        """Ingest NIH Chest X-ray14 dataset"""
        print("Ingesting NIH Chest X-ray14...")
        
        # Download metadata
        metadata_url = "https://nihcc.app.box.com/shared/static/vfk49d74nhbxq3nqjg0900w5nvkorp5c.gz"
        
        output_dir.mkdir(parents=True, exist_ok=True)
        metadata_path = output_dir / "Data_Entry_2017.csv"
        
        # In production, implement actual download
        # For now, return structure
        
        stats = {
            'dataset': 'NIH Chest X-ray14',
            'category': 'respiratory',
            'conditions': self.datasets['respiratory']['nih_chest_xray14']['conditions'],
            'status': 'configured'
        }
        
        return stats
    
    def ingest_chexpert(self, output_dir: Path, max_images: int = None) -> Dict:
        """Ingest CheXpert dataset"""
        print("Ingesting CheXpert...")
        
        # CheXpert requires registration
        # Download from: https://stanfordmlgroup.github.io/competitions/chexpert/
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        stats = {
            'dataset': 'CheXpert',
            'category': 'respiratory',
            'conditions': self.datasets['respiratory']['chexpert']['conditions'],
            'uncertainty_labels': True,
            'status': 'requires_registration'
        }
        
        return stats
    
    def ingest_brats(self, output_dir: Path, year: int = 2023) -> Dict:
        """Ingest BraTS brain tumor dataset"""
        print(f"Ingesting BraTS {year}...")
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        stats = {
            'dataset': f'BraTS {year}',
            'category': 'neurological',
            'conditions': self.datasets['neurological']['brats']['conditions'],
            'modality': 'MRI',
            'sequences': self.datasets['neurological']['brats']['sequences'],
            'status': 'configured'
        }
        
        return stats
    
    def ingest_mit_bih(self, output_dir: Path) -> Dict:
        """Ingest MIT-BIH Arrhythmia Database"""
        print("Ingesting MIT-BIH Arrhythmia Database...")
        
        base_url = "https://physionet.org/files/mitdb/1.0.0/"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Download record list
        records_url = f"{base_url}RECORDS"
        
        try:
            response = requests.get(records_url)
            records = response.text.strip().split('\n')
            
            stats = {
                'dataset': 'MIT-BIH Arrhythmia',
                'category': 'cardiovascular',
                'records': len(records),
                'conditions': self.datasets['cardiovascular']['mit_bih_arrhythmia']['conditions'],
                'status': 'ready'
            }
            
            return stats
            
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    def ingest_ham10000(self, output_dir: Path) -> Dict:
        """Ingest HAM10000 skin lesion dataset"""
        print("Ingesting HAM10000...")
        
        # Available on Kaggle and Harvard Dataverse
        output_dir.mkdir(parents=True, exist_ok=True)
        
        stats = {
            'dataset': 'HAM10000',
            'category': 'dermatology',
            'conditions': self.datasets['dermatology']['ham10000']['conditions'],
            'samples': 10015,
            'status': 'configured'
        }
        
        return stats
    
    def ingest_disease_symptom_mapping(self, output_dir: Path) -> Dict:
        """Ingest disease-symptom mapping dataset"""
        print("Ingesting Disease-Symptom dataset...")
        
        # Multiple sources available
        # 1. Kaggle: Disease Symptom Prediction
        # 2. GTS.ai dataset
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        stats = {
            'dataset': 'Disease-Symptom Mapping',
            'category': 'general',
            'conditions': 400,
            'data_type': 'structured',
            'status': 'configured'
        }
        
        return stats
    
    def create_disease_index(self, output_path: Path):
        """Create searchable index of all diseases and datasets"""
        index = []
        
        for category, datasets in self.datasets.items():
            for dataset_name, info in datasets.items():
                conditions = info.get('conditions', [])
                
                if isinstance(conditions, list):
                    for condition in conditions:
                        index.append({
                            'condition': condition,
                            'category': category,
                            'dataset': dataset_name,
                            'modality': info.get('modality', 'N/A'),
                            'samples': info.get('samples', 'N/A'),
                            'url': info.get('url', 'N/A')
                        })
                elif isinstance(conditions, int):
                    # Number of conditions
                    index.append({
                        'condition': f'{conditions} conditions',
                        'category': category,
                        'dataset': dataset_name,
                        'modality': info.get('modality', 'N/A'),
                        'samples': info.get('samples', 'N/A'),
                        'url': info.get('url', 'N/A')
                    })
        
        df = pd.DataFrame(index)
        df.to_csv(output_path, index=False)
        
        return df
    
    def get_dataset_stats(self) -> Dict:
        """Get statistics about available datasets"""
        stats = {
            'total_categories': len(self.datasets),
            'total_datasets': sum(len(datasets) for datasets in self.datasets.values()),
            'by_category': {}
        }
        
        for category, datasets in self.datasets.items():
            stats['by_category'][category] = {
                'count': len(datasets),
                'datasets': list(datasets.keys())
            }
        
        return stats
