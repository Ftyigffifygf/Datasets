"""Ingest genomics data from various sources"""
import boto3
from pathlib import Path
import requests
from typing import List, Dict
from tqdm import tqdm


class GenomicsIngester:
    def __init__(self):
        self.s3_client = boto3.client('s3', region_name='us-east-1')
        
    def list_1000genomes_files(self, prefix: str = "1000genomes/") -> List[str]:
        """List files from 1000 Genomes S3 bucket"""
        bucket = "1000genomes"
        
        paginator = self.s3_client.get_paginator('list_objects_v2')
        pages = paginator.paginate(Bucket=bucket, Prefix=prefix)
        
        files = []
        for page in pages:
            if 'Contents' in page:
                for obj in page['Contents']:
                    files.append(obj['Key'])
        
        return files
    
    def download_from_s3(self, bucket: str, key: str, output_path: Path):
        """Download file from S3"""
        output_path.parent.mkdir(parents=True, exist_ok=True)
        self.s3_client.download_file(bucket, key, str(output_path))
    
    def ingest_1000genomes(self, output_dir: Path, file_types: List[str] = ['.vcf.gz', '.bam'],
                          max_files: int = None) -> Dict:
        """Ingest 1000 Genomes data"""
        print("Ingesting 1000 Genomes Project data...")
        
        files = self.list_1000genomes_files()
        
        # Filter by file type
        filtered_files = [f for f in files if any(f.endswith(ext) for ext in file_types)]
        
        if max_files:
            filtered_files = filtered_files[:max_files]
        
        stats = {'downloaded': 0, 'failed': 0, 'total_size': 0}
        
        for file_key in tqdm(filtered_files, desc="Downloading"):
            try:
                output_path = output_dir / file_key
                self.download_from_s3("1000genomes", file_key, output_path)
                
                stats['downloaded'] += 1
                stats['total_size'] += output_path.stat().st_size
                
            except Exception as e:
                print(f"Error downloading {file_key}: {e}")
                stats['failed'] += 1
        
        return stats
    
    def ingest_gdc(self, output_dir: Path, project_id: str = "TCGA-BRCA",
                   max_files: int = 100) -> Dict:
        """Ingest data from Genomic Data Commons"""
        api_url = "https://api.gdc.cancer.gov"
        
        # Query for files
        filters = {
            "op": "and",
            "content": [
                {"op": "in", "content": {"field": "cases.project.project_id", "value": [project_id]}},
                {"op": "in", "content": {"field": "files.data_type", "value": ["Gene Expression Quantification"]}}
            ]
        }
        
        params = {
            "filters": str(filters),
            "fields": "file_id,file_name,file_size",
            "size": max_files
        }
        
        response = requests.get(f"{api_url}/files", params=params)
        response.raise_for_status()
        
        files = response.json()['data']['hits']
        
        stats = {'downloaded': 0, 'failed': 0}
        
        for file_info in tqdm(files, desc="Downloading GDC files"):
            try:
                file_id = file_info['file_id']
                file_name = file_info['file_name']
                
                download_url = f"{api_url}/data/{file_id}"
                response = requests.get(download_url, stream=True)
                response.raise_for_status()
                
                output_path = output_dir / project_id / file_name
                output_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                
                stats['downloaded'] += 1
                
            except Exception as e:
                print(f"Error downloading {file_name}: {e}")
                stats['failed'] += 1
        
        return stats
