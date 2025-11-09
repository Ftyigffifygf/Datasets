"""Ingest disease-specific datasets into vector database"""
import sys
import argparse
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "src"))

from ingest.disease_specific_ingester import DiseaseSpecificIngester
from storage.disease_vector_db import DiseaseVectorDB
from embeddings.imaging_embedder import MedicalImagingEmbedder
from embeddings.ehr_embedder import EHREmbedder


def main():
    parser = argparse.ArgumentParser(description="Ingest disease-specific datasets")
    parser.add_argument("--category", type=str, 
                       choices=['respiratory', 'neurological', 'cardiovascular',
                               'cancer', 'dermatology', 'infectious', 'diabetes', 'all'],
                       default='all',
                       help="Disease category to ingest")
    parser.add_argument("--dataset", type=str,
                       help="Specific dataset name (e.g., 'nih_chest_xray14')")
    parser.add_argument("--output-dir", type=Path, default=Path("data/disease_data"),
                       help="Output directory for downloaded data")
    parser.add_argument("--max-samples", type=int, default=1000,
                       help="Maximum samples to ingest per dataset")
    
    args = parser.parse_args()
    
    print("=" * 70)
    print("Disease-Specific Data Ingestion")
    print("=" * 70)
    
    # Initialize
    ingester = DiseaseSpecificIngester()
    vector_db = DiseaseVectorDB()
    
    # Get available datasets
    if args.category == 'all':
        datasets = ingester.list_datasets_by_category()
    else:
        datasets = ingester.list_datasets_by_category(args.category)
    
    print(f"\nTarget category: {args.category}")
    print(f"Output directory: {args.output_dir}")
    print(f"Max samples per dataset: {args.max_samples}")
    
    # Ingest datasets
    results = []
    
    for category, dataset_list in datasets.items():
        print(f"\n{'='*70}")
        print(f"Category: {category.upper()}")
        print(f"{'='*70}")
        
        for dataset_name, info in dataset_list.items():
            if args.dataset and dataset_name != args.dataset:
                continue
            
            print(f"\nDataset: {dataset_name}")
            print(f"  URL: {info.get('url', 'N/A')}")
            print(f"  Conditions: {info.get('conditions', 'N/A')}")
            print(f"  Modality: {info.get('modality', 'N/A')}")
            
            # Call appropriate ingestion method
            try:
                if dataset_name == 'nih_chest_xray14':
                    stats = ingester.ingest_nih_chest_xray(
                        args.output_dir / category / dataset_name,
                        max_images=args.max_samples
                    )
                elif dataset_name == 'chexpert':
                    stats = ingester.ingest_chexpert(
                        args.output_dir / category / dataset_name,
                        max_images=args.max_samples
                    )
                elif dataset_name == 'brats':
                    stats = ingester.ingest_brats(
                        args.output_dir / category / dataset_name
                    )
                elif dataset_name == 'mit_bih_arrhythmia':
                    stats = ingester.ingest_mit_bih(
                        args.output_dir / category / dataset_name
                    )
                elif dataset_name == 'ham10000':
                    stats = ingester.ingest_ham10000(
                        args.output_dir / category / dataset_name
                    )
                else:
                    stats = {
                        'dataset': dataset_name,
                        'status': 'not_implemented',
                        'message': 'Ingestion method not yet implemented'
                    }
                
                results.append(stats)
                print(f"  Status: {stats.get('status', 'unknown')}")
                
            except Exception as e:
                print(f"  Error: {e}")
                results.append({
                    'dataset': dataset_name,
                    'status': 'error',
                    'message': str(e)
                })
    
    # Summary
    print(f"\n{'='*70}")
    print("Ingestion Summary")
    print(f"{'='*70}")
    
    for result in results:
        print(f"{result.get('dataset', 'unknown')}: {result.get('status', 'unknown')}")
    
    print(f"\n{'='*70}")
    print("Complete!")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
