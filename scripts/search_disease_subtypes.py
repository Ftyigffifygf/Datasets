"""Search for datasets by specific disease subtypes"""
import sys
import argparse
from pathlib import Path
import yaml
from typing import Dict, List
sys.path.append(str(Path(__file__).parent.parent / "src"))


def load_taxonomy():
    """Load disease taxonomy"""
    with open("config/disease_taxonomy.yaml") as f:
        return yaml.safe_load(f)


def load_mapping():
    """Load disease to dataset mapping"""
    with open("config/disease_to_dataset_mapping.yaml") as f:
        return yaml.safe_load(f)


def flatten_taxonomy(taxonomy, parent_key='', sep='_'):
    """Flatten nested taxonomy into searchable list"""
    items = []
    for k, v in taxonomy.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_taxonomy(v, new_key, sep=sep))
        elif isinstance(v, list):
            for item in v:
                items.append((new_key, item))
        else:
            items.append((new_key, v))
    return items


def search_disease(query: str, taxonomy: Dict, mapping: Dict):
    """Search for disease and its subtypes"""
    query_lower = query.lower()
    results = []
    
    # Flatten taxonomy for searching
    flat_taxonomy = flatten_taxonomy(taxonomy)
    
    # Search in taxonomy
    for category, disease in flat_taxonomy:
        if isinstance(disease, str) and query_lower in disease.lower():
            results.append({
                'category': category,
                'disease': disease,
                'type': 'subtype'
            })
    
    # Search in mapping
    for disease_key, disease_info in mapping.items():
        if query_lower in disease_key.lower():
            results.append({
                'disease': disease_key,
                'info': disease_info,
                'type': 'mapped'
            })
        
        # Search in nested subtypes
        if isinstance(disease_info, dict):
            for subtype_key, subtype_info in disease_info.items():
                if query_lower in subtype_key.lower():
                    results.append({
                        'disease': disease_key,
                        'subtype': subtype_key,
                        'info': subtype_info,
                        'type': 'mapped_subtype'
                    })
    
    return results


def display_disease_tree(disease_name: str, taxonomy: Dict):
    """Display disease hierarchy tree"""
    print(f"\n{'='*80}")
    print(f"DISEASE TAXONOMY: {disease_name.upper()}")
    print(f"{'='*80}\n")
    
    def print_tree(data, indent=0):
        if isinstance(data, dict):
            for key, value in data.items():
                print("  " * indent + f"├─ {key}")
                print_tree(value, indent + 1)
        elif isinstance(data, list):
            for item in data:
                print("  " * indent + f"  • {item}")
        else:
            print("  " * indent + f"  {data}")
    
    # Find disease in taxonomy
    for category, diseases in taxonomy.items():
        if disease_name.lower() in category.lower():
            print(f"📁 {category.upper()}")
            print_tree(diseases, 1)
            return
        
        if isinstance(diseases, dict):
            for disease_key, disease_data in diseases.items():
                if disease_name.lower() in disease_key.lower():
                    print(f"📁 {category.upper()} → {disease_key}")
                    print_tree(disease_data, 1)
                    return


def display_datasets_for_disease(disease_name: str, mapping: Dict):
    """Display available datasets for disease"""
    print(f"\n{'='*80}")
    print(f"AVAILABLE DATASETS: {disease_name.upper()}")
    print(f"{'='*80}\n")
    
    found = False
    
    for disease_key, disease_info in mapping.items():
        if disease_name.lower() in disease_key.lower():
            found = True
            
            if isinstance(disease_info, dict):
                # Check if it has datasets directly
                if 'datasets' in disease_info:
                    print(f"🔬 {disease_key}")
                    print(f"   Datasets: {', '.join(disease_info['datasets'])}")
                    print(f"   Samples: {disease_info.get('samples', 'N/A')}")
                    print(f"   Modalities: {disease_info.get('modalities', 'N/A')}")
                    print()
                else:
                    # Has subtypes
                    print(f"🔬 {disease_key}")
                    for subtype_key, subtype_info in disease_info.items():
                        if isinstance(subtype_info, dict) and 'datasets' in subtype_info:
                            print(f"\n   ├─ {subtype_key}")
                            print(f"   │  Datasets: {', '.join(subtype_info['datasets'])}")
                            print(f"   │  Samples: {subtype_info.get('samples', 'N/A')}")
                            print(f"   │  Modalities: {subtype_info.get('modalities', 'N/A')}")
                    print()
    
    if not found:
        print(f"No datasets found for: {disease_name}")
        print("\nTry searching for:")
        print("  - Cancer types: melanoma, breast_cancer, lung_cancer")
        print("  - Neurological: alzheimers, parkinsons, stroke")
        print("  - Cardiac: arrhythmias, heart_failure, myocardial_infarction")
        print("  - Respiratory: pneumonia, tuberculosis, copd")


def list_all_diseases(taxonomy: Dict):
    """List all diseases in taxonomy"""
    print(f"\n{'='*80}")
    print("ALL DISEASES IN TAXONOMY")
    print(f"{'='*80}\n")
    
    for category, diseases in taxonomy.items():
        print(f"\n📁 {category.upper()}")
        
        if isinstance(diseases, dict):
            for disease_key in diseases.keys():
                print(f"   • {disease_key}")


def main():
    parser = argparse.ArgumentParser(
        description="Search for specific disease subtypes and available datasets"
    )
    parser.add_argument("disease", nargs='?', type=str, 
                       help="Disease name to search for")
    parser.add_argument("--tree", action="store_true",
                       help="Show disease taxonomy tree")
    parser.add_argument("--datasets", action="store_true",
                       help="Show available datasets")
    parser.add_argument("--list-all", action="store_true",
                       help="List all diseases in taxonomy")
    
    args = parser.parse_args()
    
    # Load data
    taxonomy = load_taxonomy()
    mapping = load_mapping()
    
    if args.list_all:
        list_all_diseases(taxonomy)
        return
    
    if not args.disease:
        print("Usage: python scripts/search_disease_subtypes.py <disease_name>")
        print("\nExamples:")
        print("  python scripts/search_disease_subtypes.py melanoma --tree --datasets")
        print("  python scripts/search_disease_subtypes.py breast_cancer --datasets")
        print("  python scripts/search_disease_subtypes.py pneumonia --tree")
        print("  python scripts/search_disease_subtypes.py --list-all")
        return
    
    disease = args.disease
    
    # Show taxonomy tree
    if args.tree or (not args.datasets):
        display_disease_tree(disease, taxonomy)
    
    # Show datasets
    if args.datasets or (not args.tree):
        display_datasets_for_disease(disease, mapping)
    
    # Search results
    results = search_disease(disease, taxonomy, mapping)
    
    if results:
        print(f"\n{'='*80}")
        print(f"SEARCH RESULTS FOR: {disease}")
        print(f"{'='*80}\n")
        print(f"Found {len(results)} matches\n")
        
        # Group by type
        subtypes = [r for r in results if r['type'] == 'subtype']
        mapped = [r for r in results if r['type'] in ['mapped', 'mapped_subtype']]
        
        if subtypes:
            print("📋 Disease Subtypes:")
            for r in subtypes[:10]:
                print(f"   • {r['disease']}")
        
        if mapped:
            print(f"\n💾 Datasets Available:")
            for r in mapped[:10]:
                if 'info' in r and isinstance(r['info'], dict):
                    if 'datasets' in r['info']:
                        print(f"   • {r['disease']}: {len(r['info']['datasets'])} datasets")


if __name__ == "__main__":
    main()
