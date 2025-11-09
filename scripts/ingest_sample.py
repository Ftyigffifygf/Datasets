"""Sample script to ingest a small subset of data for testing"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from pipeline.orchestrator import MedicalDataPipeline


def main():
    print("Running sample data ingestion...")
    print("This will download a small subset for testing")
    print("=" * 60)
    
    pipeline = MedicalDataPipeline()
    
    # Setup collections
    pipeline.setup_collections()
    
    # Ingest small sample from TCIA
    print("\nIngesting sample TCIA data (2 patients per collection)...")
    imaging_dir = Path("data/imaging")
    pipeline.ingest_tcia(imaging_dir, max_patients=2)
    
    print("\n" + "=" * 60)
    print("Sample ingestion complete!")
    print("\nYou can now:")
    print("  1. Start the API: python src/api/query_api.py")
    print("  2. Query via: curl http://localhost:8000/search/text")
    print("  3. View docs: http://localhost:8000/docs")


if __name__ == "__main__":
    main()
