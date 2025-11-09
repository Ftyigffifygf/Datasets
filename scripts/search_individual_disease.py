"""Search for individual diseases with complete details"""
import sys
import argparse
from pathlib import Path
import yaml
from typing import Dict, List
sys.path.append(str(Path(__file__).parent.parent / "src"))


def load_all_data():
    """Load all configuration files"""
    with open("config/disease_taxonomy.yaml") as f:
        taxonomy = yaml.safe_load(f)
    
    with open("config/disease_to_dataset_mapping.yaml") as f:
        mapping = yaml.safe_load(f)
    
    with open("config/disease_datasets.yaml") as f:
        datasets = yaml.safe_load(f)
    
    return taxonomy, mapping, datasets


def create_disease_index(taxonomy, mapping):
    """Create searchable index of all individual diseases"""
    index = {}
    
    def extract_diseases(data, category='', parent=''):
        if isinstance(data, dict):
            for key, value in data.items():
                full_path = f"{parent}/{key}" if parent else key
                
                if isinstance(value, list):
                    # List of disease names
                    for disease in value:
                        disease_key = disease.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_')
                        index[disease_key] = {
                            'name': disease,
                            'category': category or key,
                            'parent': parent,
                            'type': 'subtype'
                        }
                elif isinstance(value, dict):
                    extract_diseases(value, category or key, full_path)
                else:
                    disease_key = str(value).lower().replace(' ', '_')
                    index[disease_key] = {
                        'name': str(value),
                        'category': category or key,
                        'parent': parent,
                        'type': 'subtype'
                    }
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, str):
                    disease_key = item.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_')
                    index[disease_key] = {
                        'name': item,
                        'category': category,
                        'parent': parent,
                        'type': 'subtype'
                    }
    
    for category, diseases in taxonomy.items():
        extract_diseases(diseases, category)
    
    # Add diseases from mapping
    for disease_key, disease_info in mapping.items():
        if disease_key not in index:
            index[disease_key] = {
                'name': disease_key.replace('_', ' ').title(),
                'category': 'mapped',
                'has_datasets': True,
                'type': 'mapped'
            }
        
        # Add subtypes from mapping
        if isinstance(disease_info, dict):
            for subtype_key, subtype_info in disease_info.items():
                if isinstance(subtype_info, dict) and 'datasets' in subtype_info:
                    full_key = f"{disease_key}_{subtype_key}"
                    index[full_key] = {
                        'name': subtype_key.replace('_', ' ').title(),
                        'category': disease_key,
                        'parent': disease_key,
                        'has_datasets': True,
                        'datasets': subtype_info.get('datasets', []),
                        'samples': subtype_info.get('samples', 'N/A'),
                        'modalities': subtype_info.get('modalities', []),
                        'type': 'mapped_subtype'
                    }
    
    return index


def search_disease(query: str, index: Dict, mapping: Dict, datasets: Dict):
    """Search for a specific disease"""
    query_key = query.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_')
    
    # Direct match
    if query_key in index:
        return display_disease_details(query_key, index[query_key], mapping, datasets)
    
    # Partial match
    matches = []
    for key, info in index.items():
        if query.lower() in key.lower() or query.lower() in info['name'].lower():
            matches.append((key, info))
    
    if len(matches) == 1:
        return display_disease_details(matches[0][0], matches[0][1], mapping, datasets)
    elif len(matches) > 1:
        print(f"\n{'='*80}")
        print(f"Multiple matches found for: {query}")
        print(f"{'='*80}\n")
        for i, (key, info) in enumerate(matches[:20], 1):
            print(f"{i}. {info['name']} ({info['category']})")
        print(f"\nPlease be more specific or use exact name.")
        return None
    else:
        print(f"\nNo disease found matching: {query}")
        print("\nTry:")
        print("  python scripts/search_individual_disease.py --list-all")
        return None


def display_disease_details(disease_key: str, disease_info: Dict, mapping: Dict, datasets: Dict):
    """Display complete details for a disease"""
    print(f"\n{'='*80}")
    print(f"DISEASE: {disease_info['name'].upper()}")
    print(f"{'='*80}\n")
    
    # Basic Information
    print("📋 BASIC INFORMATION")
    print(f"   Name: {disease_info['name']}")
    print(f"   Category: {disease_info['category']}")
    if disease_info.get('parent'):
        print(f"   Parent: {disease_info['parent']}")
    print(f"   Type: {disease_info['type']}")
    
    # Dataset Information
    if disease_info.get('has_datasets'):
        print(f"\n💾 AVAILABLE DATASETS")
        
        if 'datasets' in disease_info:
            print(f"   Datasets: {', '.join(disease_info['datasets'])}")
            print(f"   Samples: {disease_info.get('samples', 'N/A')}")
            print(f"   Modalities: {disease_info.get('modalities', 'N/A')}")
            
            # Get dataset details
            print(f"\n📊 DATASET DETAILS")
            for dataset_name in disease_info['datasets']:
                for category, dataset_list in datasets.items():
                    if dataset_name in dataset_list:
                        ds_info = dataset_list[dataset_name]
                        size_gb = ds_info.get('size_gb', 0)
                        size_tb = ds_info.get('size_tb', 0)
                        if size_tb:
                            size_str = f"{size_tb} TB"
                        else:
                            size_str = f"{size_gb} GB"
                        
                        print(f"\n   {dataset_name}:")
                        print(f"      Size: {size_str}")
                        print(f"      Samples: {ds_info.get('samples', 'N/A')}")
                        print(f"      Modality: {ds_info.get('modality', 'N/A')}")
                        print(f"      URL: {ds_info.get('url', 'N/A')}")
                        if ds_info.get('access'):
                            print(f"      Access: {ds_info['access']}")
    
    # Search in mapping for related information
    print(f"\n🔍 RELATED INFORMATION")
    
    # Find in mapping
    found_in_mapping = False
    for map_key, map_info in mapping.items():
        if disease_key in map_key or map_key in disease_key:
            found_in_mapping = True
            
            if isinstance(map_info, dict):
                if 'datasets' in map_info:
                    print(f"\n   Main Disease: {map_key.replace('_', ' ').title()}")
                    print(f"   Datasets: {', '.join(map_info['datasets'])}")
                    print(f"   Samples: {map_info.get('samples', 'N/A')}")
                else:
                    # Has subtypes
                    print(f"\n   Disease Group: {map_key.replace('_', ' ').title()}")
                    print(f"   Subtypes:")
                    for subtype_key, subtype_info in map_info.items():
                        if isinstance(subtype_info, dict) and 'datasets' in subtype_info:
                            print(f"      • {subtype_key.replace('_', ' ').title()}")
                            print(f"        Datasets: {', '.join(subtype_info['datasets'])}")
                            print(f"        Samples: {subtype_info.get('samples', 'N/A')}")
    
    if not found_in_mapping:
        print("   No additional mapping information available")
    
    # Clinical Notes
    print(f"\n📝 CLINICAL NOTES")
    clinical_notes = get_clinical_notes(disease_info['name'])
    if clinical_notes:
        for note in clinical_notes:
            print(f"   • {note}")
    else:
        print("   No clinical notes available")
    
    print(f"\n{'='*80}\n")
    
    return disease_info


def get_clinical_notes(disease_name: str) -> List[str]:
    """Get clinical notes for specific diseases"""
    notes_db = {
        'Superficial Spreading Melanoma': [
            'Most common melanoma type (70%)',
            'Horizontal growth phase before vertical invasion',
            'Better prognosis than nodular melanoma',
            'Often appears on trunk in men, legs in women'
        ],
        'Nodular Melanoma': [
            'Second most common melanoma (15%)',
            'Most aggressive melanoma type',
            'Vertical growth from onset',
            'Rapid progression, poor prognosis if not caught early'
        ],
        'Invasive Ductal Carcinoma': [
            'Most common breast cancer type (80%)',
            'Originates in milk ducts',
            'Can spread to lymph nodes and other organs',
            'Treatment depends on molecular subtype'
        ],
        'Triple Negative': [
            'ER-, PR-, HER2- breast cancer (15%)',
            'Most aggressive breast cancer subtype',
            'Limited targeted therapy options',
            'Higher recurrence rate',
            'More common in younger women and BRCA1 carriers'
        ],
        'Glioblastoma': [
            'Most aggressive brain tumor (Grade IV)',
            'Median survival: 15 months',
            'Highly infiltrative, difficult to remove completely',
            'Standard treatment: Surgery + radiation + chemotherapy'
        ],
        'Atrial Fibrillation': [
            'Most common arrhythmia',
            'Irregular, rapid heart rate',
            'Increases stroke risk 5-fold',
            'Treatment: Rate/rhythm control + anticoagulation'
        ],
        'STEMI': [
            'ST-Elevation Myocardial Infarction',
            'Complete coronary artery blockage',
            'Medical emergency - time is muscle',
            'Treatment: Immediate reperfusion (PCI or thrombolysis)'
        ],
        'Proliferative DR': [
            'Advanced diabetic retinopathy',
            'Neovascularization present',
            'High risk of vision loss',
            'Treatment: Laser photocoagulation or anti-VEGF injections'
        ],
        'Pneumococcal': [
            'Most common bacterial pneumonia',
            'Caused by Streptococcus pneumoniae',
            'Vaccine available (PCV13, PPSV23)',
            'Treatment: Beta-lactam antibiotics'
        ],
        'MDR-TB': [
            'Multi-drug resistant tuberculosis',
            'Resistant to isoniazid and rifampicin',
            'Requires 18-24 months of treatment',
            'Second-line drugs with more side effects'
        ]
    }
    
    return notes_db.get(disease_name, [])


def list_all_diseases(index: Dict):
    """List all searchable diseases"""
    print(f"\n{'='*80}")
    print("ALL SEARCHABLE DISEASES")
    print(f"{'='*80}\n")
    
    # Group by category
    by_category = {}
    for key, info in index.items():
        category = info['category']
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(info['name'])
    
    for category in sorted(by_category.keys()):
        print(f"\n📁 {category.upper().replace('_', ' ')}")
        diseases = sorted(set(by_category[category]))
        for disease in diseases[:50]:  # Limit to 50 per category
            print(f"   • {disease}")
        if len(diseases) > 50:
            print(f"   ... and {len(diseases) - 50} more")
    
    print(f"\n{'='*80}")
    print(f"Total: {len(index)} searchable diseases")
    print(f"{'='*80}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Search for individual diseases with complete details"
    )
    parser.add_argument("disease", nargs='?', type=str,
                       help="Disease name to search for")
    parser.add_argument("--list-all", action="store_true",
                       help="List all searchable diseases")
    parser.add_argument("--category", type=str,
                       help="Filter by category")
    
    args = parser.parse_args()
    
    # Load data
    taxonomy, mapping, datasets = load_all_data()
    
    # Create index
    print("Building disease index...")
    index = create_disease_index(taxonomy, mapping)
    print(f"Indexed {len(index)} diseases\n")
    
    if args.list_all:
        list_all_diseases(index)
        return
    
    if not args.disease:
        print("Usage: python scripts/search_individual_disease.py <disease_name>")
        print("\nExamples:")
        print("  python scripts/search_individual_disease.py 'nodular melanoma'")
        print("  python scripts/search_individual_disease.py 'triple negative'")
        print("  python scripts/search_individual_disease.py 'glioblastoma'")
        print("  python scripts/search_individual_disease.py 'atrial fibrillation'")
        print("  python scripts/search_individual_disease.py 'STEMI'")
        print("  python scripts/search_individual_disease.py --list-all")
        return
    
    # Search for disease
    search_disease(args.disease, index, mapping, datasets)


if __name__ == "__main__":
    main()
