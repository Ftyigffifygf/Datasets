"""Search datasets by medical condition"""
import sys
import argparse
from pathlib import Path
import yaml
sys.path.append(str(Path(__file__).parent.parent / "src"))


def search_condition(condition_query, datasets):
    """Search for datasets containing a specific condition"""
    results = []
    
    for category, dataset_list in datasets.items():
        for dataset_name, info in dataset_list.items():
            conditions = info.get('conditions', info.get('cancer_types', []))
            
            # Check if condition matches
            matched = False
            if isinstance(conditions, list):
                for cond in conditions:
                    if condition_query.lower() in cond.lower():
                        matched = True
                        break
            elif isinstance(conditions, str):
                if condition_query.lower() in conditions.lower():
                    matched = True
            
            if matched:
                size_gb = info.get('size_gb', 0)
                size_tb = info.get('size_tb', 0)
                if size_tb:
                    size_gb = size_tb * 1000
                
                results.append({
                    'dataset': dataset_name,
                    'category': category,
                    'size_gb': size_gb,
                    'samples': info.get('samples', 'N/A'),
                    'modality': info.get('modality', 'N/A'),
                    'url': info.get('url', 'N/A'),
                    'conditions': conditions
                })
    
    return results


def main():
    parser = argparse.ArgumentParser(description="Search datasets by medical condition")
    parser.add_argument("condition", type=str, help="Medical condition to search for")
    parser.add_argument("--show-all", action="store_true", 
                       help="Show all conditions in matching datasets")
    
    args = parser.parse_args()
    
    # Load datasets
    with open("config/disease_datasets.yaml") as f:
        datasets = yaml.safe_load(f)
    
    print("=" * 80)
    print(f"SEARCHING FOR: {args.condition}")
    print("=" * 80)
    
    results = search_condition(args.condition, datasets)
    
    if not results:
        print(f"\nNo datasets found for condition: {args.condition}")
        print("\nTry searching for:")
        print("  - Cancer types: melanoma, breast, lung, brain")
        print("  - Respiratory: pneumonia, covid, tuberculosis")
        print("  - Neurological: alzheimer, parkinson, stroke")
        print("  - Cardiac: arrhythmia, heart failure, infarction")
        return
    
    print(f"\nFound {len(results)} dataset(s):\n")
    
    for i, result in enumerate(results, 1):
        print(f"{i}. {result['dataset'].upper()}")
        print(f"   Category: {result['category']}")
        
        size_str = f"{result['size_gb']/1000:.1f} TB" if result['size_gb'] >= 1000 else f"{result['size_gb']} GB"
        print(f"   Size: {size_str}")
        
        if result['samples'] != 'N/A':
            print(f"   Samples: {result['samples']:,}")
        
        print(f"   Modality: {result['modality']}")
        
        if args.show_all:
            print(f"   All Conditions: {result['conditions']}")
        
        print(f"   URL: {result['url']}")
        print()
    
    # Summary
    total_size = sum(r['size_gb'] for r in results)
    total_samples = sum(r['samples'] for r in results if isinstance(r['samples'], int))
    
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total Datasets: {len(results)}")
    print(f"Total Size: {total_size/1000:.1f} TB" if total_size >= 1000 else f"Total Size: {total_size} GB")
    if total_samples:
        print(f"Total Samples: {total_samples:,}")
    
    print("\nCategories:")
    categories = {}
    for r in results:
        cat = r['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    for cat, count in categories.items():
        print(f"  - {cat}: {count} dataset(s)")
    
    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()
