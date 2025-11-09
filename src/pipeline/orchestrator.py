"""Main orchestration pipeline for data ingestion and embedding"""
import argparse
from pathlib import Path
import yaml
import sys
sys.path.append(str(Path(__file__).parent.parent))

from storage.vector_db import MedicalVectorDB
from embeddings.imaging_embedder import MedicalImagingEmbedder
from embeddings.ehr_embedder import EHREmbedder
from embeddings.genomics_embedder import GenomicsEmbedder
from ingest.tcia_ingester import TCIAIngester
from ingest.genomics_ingester import GenomicsIngester
from ingest.mimic_ingester import MIMICIngester


class MedicalDataPipeline:
    def __init__(self, config_path: str = "config/vector_config.yaml"):
        self.vector_db = MedicalVectorDB(config_path)
        
        # Initialize embedders
        self.imaging_embedder = MedicalImagingEmbedder()
        self.ehr_embedder = EHREmbedder()
        self.genomics_embedder = GenomicsEmbedder()
        
        # Initialize ingesters
        self.tcia_ingester = TCIAIngester()
        self.genomics_ingester = GenomicsIngester()
        
    def setup_collections(self):
        """Create vector database collections"""
        print("Setting up collections...")
        self.vector_db.create_collection("medical_imaging", "medical_imaging")
        self.vector_db.create_collection("genomics", "genomics")
        self.vector_db.create_collection("ehr_clinical", "ehr_clinical")
        
    def ingest_tcia(self, output_dir: Path, collections: list = None, 
                    max_patients: int = 10):
        """Ingest TCIA imaging data"""
        print("\n=== Ingesting TCIA Data ===")
        
        if not collections:
            collections = self.tcia_ingester.get_collections()[:5]  # First 5
        
        for collection in collections:
            print(f"\nProcessing collection: {collection}")
            stats = self.tcia_ingester.ingest_collection(
                collection, output_dir, max_patients=max_patients
            )
            print(f"Stats: {stats}")
    
    def ingest_genomics(self, output_dir: Path, max_files: int = 100):
        """Ingest genomics data"""
        print("\n=== Ingesting Genomics Data ===")
        
        stats = self.genomics_ingester.ingest_1000genomes(
            output_dir, max_files=max_files
        )
        print(f"1000 Genomes stats: {stats}")
        
        stats = self.genomics_ingester.ingest_gdc(
            output_dir, max_files=max_files
        )
        print(f"GDC stats: {stats}")
    
    def ingest_mimic(self, mimic_dir: Path, max_patients: int = 1000):
        """Ingest MIMIC EHR data"""
        print("\n=== Ingesting MIMIC Data ===")
        
        mimic_ingester = MIMICIngester(mimic_dir)
        
        stats = mimic_ingester.ingest_to_vectordb(
            self.ehr_embedder,
            self.vector_db,
            "ehr_clinical",
            max_patients=max_patients
        )
        print(f"MIMIC stats: {stats}")
    
    def run_full_pipeline(self, data_dir: Path, mimic_dir: Path = None):
        """Run complete ingestion pipeline"""
        print("Starting Medical Vector DB Pipeline")
        print("=" * 50)
        
        # Setup
        self.setup_collections()
        
        # Ingest imaging
        imaging_dir = data_dir / "imaging"
        self.ingest_tcia(imaging_dir, max_patients=5)
        
        # Ingest genomics
        genomics_dir = data_dir / "genomics"
        self.ingest_genomics(genomics_dir, max_files=50)
        
        # Ingest EHR (if MIMIC available)
        if mimic_dir and mimic_dir.exists():
            self.ingest_mimic(mimic_dir, max_patients=500)
        
        print("\n" + "=" * 50)
        print("Pipeline complete!")


def main():
    parser = argparse.ArgumentParser(description="Medical Vector DB Pipeline")
    parser.add_argument("--data-dir", type=Path, default=Path("data"),
                       help="Output directory for downloaded data")
    parser.add_argument("--mimic-dir", type=Path, default=None,
                       help="Path to MIMIC-IV data directory")
    parser.add_argument("--setup-only", action="store_true",
                       help="Only setup collections, don't ingest data")
    
    args = parser.parse_args()
    
    pipeline = MedicalDataPipeline()
    
    if args.setup_only:
        pipeline.setup_collections()
    else:
        pipeline.run_full_pipeline(args.data_dir, args.mimic_dir)


if __name__ == "__main__":
    main()
