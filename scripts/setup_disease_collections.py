"""Setup disease-specific collections and create disease index"""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from storage.disease_vector_db import DiseaseVectorDB
from ingest.disease_specific_ingester import DiseaseSpecificIngester


def main():
    print("=" * 70)
    print("Medical Disease Vector Database - Setup")
    print("=" * 70)
    
    # Initialize
    vector_db = DiseaseVectorDB()
    ingester = DiseaseSpecificIngester()
    
    # Create disease-specific collections
    print("\n1. Creating disease-specific collections...")
    collections = vector_db.create_all_disease_collections()
    print(f"   Created {len(collections)} collections:")
    for col in collections:
        print(f"   - {col}")
    
    # Create disease index
    print("\n2. Creating disease-condition index...")
    index_path = Path("data/disease_index.csv")
    index_path.parent.mkdir(parents=True, exist_ok=True)
    
    df = ingester.create_disease_index(index_path)
    print(f"   Created index with {len(df)} entries")
    print(f"   Saved to: {index_path}")
    
    # Get statistics
    print("\n3. Dataset statistics:")
    stats = ingester.get_dataset_stats()
    print(f"   Total categories: {stats['total_categories']}")
    print(f"   Total datasets: {stats['total_datasets']}")
    print("\n   By category:")
    for category, info in stats['by_category'].items():
        print(f"   - {category}: {info['count']} datasets")
    
    print("\n" + "=" * 70)
    print("Setup complete!")
    print("\nAvailable disease categories:")
    print("  - respiratory (Pneumonia, COVID-19, Tuberculosis, etc.)")
    print("  - neurological (Alzheimer's, Brain Tumors, etc.)")
    print("  - cardiovascular (Arrhythmia, Heart Disease, etc.)")
    print("  - cancer (30+ cancer types)")
    print("  - dermatology (Melanoma, Skin Lesions, etc.)")
    print("  - infectious (COVID-19, Malaria, TB, etc.)")
    print("  - diabetes (Diabetic Retinopathy, etc.)")
    print("  - general (Multi-disease datasets)")
    print("\nNext steps:")
    print("  1. Start API: python src/api/disease_query_api.py")
    print("  2. View disease index: cat data/disease_index.csv")
    print("  3. Ingest data: python scripts/ingest_disease_data.py")
    print("=" * 70)


if __name__ == "__main__":
    main()
