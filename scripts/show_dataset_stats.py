"""Display comprehensive statistics about all available datasets"""
import sys
from pathlib import Path
import yaml
sys.path.append(str(Path(__file__).parent.parent / "src"))


def format_size(size_gb):
    """Format size in human-readable format"""
    if size_gb >= 1000:
        return f"{size_gb/1000:.1f} TB"
    return f"{size_gb} GB"


def main():
    # Load disease datasets
    with open("config/disease_datasets.yaml") as f:
        datasets = yaml.safe_load(f)
    
    print("=" * 80)
    print("MEDICAL VECTOR DATABASE - COMPLETE DATASET CATALOG")
    print("=" * 80)
    
    total_datasets = 0
    total_size_gb = 0
    total_samples = 0
    categories_summary = {}
    
    for category, dataset_list in datasets.items():
        category_size = 0
        category_datasets = 0
        category_samples = 0
        
        print(f"\n{'='*80}")
        print(f"📁 {category.upper().replace('_', ' ')}")
        print(f"{'='*80}")
        
        for dataset_name, info in dataset_list.items():
            category_datasets += 1
            total_datasets += 1
            
            # Calculate size
            size_gb = info.get('size_gb', 0)
            size_tb = info.get('size_tb', 0)
            size_mb = info.get('size_mb', 0)
            
            if size_tb:
                size_gb = size_tb * 1000
            elif size_mb:
                size_gb = size_mb / 1000
            
            category_size += size_gb
            total_size_gb += size_gb
            
            # Get samples
            samples = info.get('samples', 0)
            if isinstance(samples, int):
                category_samples += samples
                total_samples += samples
            
            # Get conditions
            conditions = info.get('conditions', info.get('cancer_types', []))
            if isinstance(conditions, list):
                condition_str = f"{len(conditions)} conditions"
            elif isinstance(conditions, int):
                condition_str = f"{conditions} conditions"
            else:
                condition_str = str(conditions)
            
            # Display dataset
            print(f"\n  {dataset_name}")
            print(f"    Size: {format_size(size_gb)}")
            if samples:
                print(f"    Samples: {samples:,}")
            print(f"    Conditions: {condition_str}")
            print(f"    Modality: {info.get('modality', 'N/A')}")
            if info.get('access'):
                print(f"    Access: {info['access']}")
            print(f"    URL: {info.get('url', 'N/A')}")
        
        categories_summary[category] = {
            'datasets': category_datasets,
            'size_gb': category_size,
            'samples': category_samples
        }
    
    # Summary
    print(f"\n{'='*80}")
    print("📊 SUMMARY STATISTICS")
    print(f"{'='*80}")
    
    print(f"\nTotal Categories: {len(datasets)}")
    print(f"Total Datasets: {total_datasets}")
    print(f"Total Size: {format_size(total_size_gb)}")
    print(f"Total Samples: {total_samples:,}")
    
    print(f"\n{'='*80}")
    print("BY CATEGORY")
    print(f"{'='*80}")
    
    # Sort by size
    sorted_categories = sorted(categories_summary.items(), 
                              key=lambda x: x[1]['size_gb'], 
                              reverse=True)
    
    for category, stats in sorted_categories:
        print(f"\n{category.upper().replace('_', ' ')}")
        print(f"  Datasets: {stats['datasets']}")
        print(f"  Size: {format_size(stats['size_gb'])}")
        if stats['samples']:
            print(f"  Samples: {stats['samples']:,}")
    
    print(f"\n{'='*80}")
    print("🎯 QUICK ACCESS GUIDE")
    print(f"{'='*80}")
    
    print("\nLargest Datasets (>1 TB):")
    large_datasets = []
    for category, dataset_list in datasets.items():
        for dataset_name, info in dataset_list.items():
            size_gb = info.get('size_gb', 0)
            size_tb = info.get('size_tb', 0)
            if size_tb:
                size_gb = size_tb * 1000
            if size_gb >= 1000:
                large_datasets.append((dataset_name, size_gb, category))
    
    large_datasets.sort(key=lambda x: x[1], reverse=True)
    for name, size, cat in large_datasets[:10]:
        print(f"  - {name} ({cat}): {format_size(size)}")
    
    print("\nMost Samples:")
    sample_datasets = []
    for category, dataset_list in datasets.items():
        for dataset_name, info in dataset_list.items():
            samples = info.get('samples', 0)
            if isinstance(samples, int) and samples > 0:
                sample_datasets.append((dataset_name, samples, category))
    
    sample_datasets.sort(key=lambda x: x[1], reverse=True)
    for name, samples, cat in sample_datasets[:10]:
        print(f"  - {name} ({cat}): {samples:,} samples")
    
    print(f"\n{'='*80}")
    print("✅ Setup complete! Use these commands:")
    print(f"{'='*80}")
    print("\n  python scripts/setup_disease_collections.py")
    print("  python scripts/ingest_disease_data.py --category respiratory")
    print("  python src/api/disease_query_api.py")
    print(f"\n{'='*80}\n")


if __name__ == "__main__":
    main()
