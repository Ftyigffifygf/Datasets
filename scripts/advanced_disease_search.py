"""Advanced disease search with complete clinical details"""
import sys
import argparse
from pathlib import Path
import yaml
import json
from typing import Dict, List
sys.path.append(str(Path(__file__).parent.parent / "src"))


def load_all_data():
    """Load all configuration and clinical data"""
    with open("config/disease_taxonomy.yaml") as f:
        taxonomy = yaml.safe_load(f)
    
    with open("config/disease_to_dataset_mapping.yaml") as f:
        mapping = yaml.safe_load(f)
    
    with open("config/disease_datasets.yaml") as f:
        datasets = yaml.safe_load(f)
    
    with open("config/disease_clinical_details.yaml") as f:
        clinical = yaml.safe_load(f)
    
    # Load disease database if exists
    db_path = Path("data/disease_database.json")
    disease_db = {}
    if db_path.exists():
        with open(db_path) as f:
            disease_db = json.load(f)
    
    return taxonomy, mapping, datasets, clinical, disease_db


def search_disease_advanced(query: str, clinical_data: Dict):
    """Advanced search with clinical details"""
    query_lower = query.lower().replace(' ', '_').replace('-', '_')
    
    results = []
    
    for category, diseases in clinical_data.items():
        for disease_key, disease_info in diseases.items():
            if query_lower in disease_key or query_lower in disease_info.get('full_name', '').lower():
                results.append({
                    'key': disease_key,
                    'category': category,
                    'info': disease_info
                })
    
    return results


def display_clinical_details(disease_key: str, disease_info: Dict, datasets: Dict):
    """Display complete clinical details"""
    print(f"\n{'='*80}")
    print(f"DISEASE: {disease_info.get('full_name', disease_key).upper()}")
    print(f"{'='*80}\n")
    
    # Basic Information
    print("📋 BASIC INFORMATION")
    print(f"   Full Name: {disease_info.get('full_name', 'N/A')}")
    if disease_info.get('icd10'):
        print(f"   ICD-10 Code: {disease_info['icd10']}")
    if disease_info.get('prevalence'):
        print(f"   Prevalence: {disease_info['prevalence']}")
    if disease_info.get('definition'):
        print(f"   Definition: {disease_info['definition']}")
    
    # Symptoms
    if disease_info.get('symptoms'):
        print(f"\n🩺 SYMPTOMS")
        for symptom in disease_info['symptoms']:
            print(f"   • {symptom}")
    
    # Risk Factors
    if disease_info.get('risk_factors'):
        print(f"\n⚠️  RISK FACTORS")
        for risk in disease_info['risk_factors']:
            print(f"   • {risk}")
    
    # Diagnosis
    if disease_info.get('diagnosis'):
        print(f"\n🔬 DIAGNOSIS")
        if isinstance(disease_info['diagnosis'], list):
            for method in disease_info['diagnosis']:
                print(f"   • {method}")
        elif isinstance(disease_info['diagnosis'], dict):
            for key, value in disease_info['diagnosis'].items():
                print(f"   • {key.replace('_', ' ').title()}: {value}")
    
    # Biomarkers
    if disease_info.get('biomarkers'):
        print(f"\n🧬 BIOMARKERS")
        if isinstance(disease_info['biomarkers'], list):
            for marker in disease_info['biomarkers']:
                print(f"   • {marker}")
        elif isinstance(disease_info['biomarkers'], dict):
            for key, value in disease_info['biomarkers'].items():
                print(f"   • {key}: {value}")
    
    # Staging
    if disease_info.get('staging'):
        print(f"\n📊 STAGING")
        for stage, description in disease_info['staging'].items():
            print(f"   • {stage.replace('_', ' ').title()}: {description}")
    
    # Treatment
    if disease_info.get('treatment'):
        print(f"\n💊 TREATMENT")
        treatment = disease_info['treatment']
        if isinstance(treatment, dict):
            for key, value in treatment.items():
                print(f"   • {key.replace('_', ' ').title()}: {value}")
        else:
            print(f"   {treatment}")
    
    # Prognosis
    if disease_info.get('prognosis'):
        print(f"\n📈 PROGNOSIS")
        prognosis = disease_info['prognosis']
        if isinstance(prognosis, dict):
            for key, value in prognosis.items():
                if isinstance(value, dict):
                    print(f"   {key.replace('_', ' ').title()}:")
                    for subkey, subvalue in value.items():
                        print(f"      • {subkey.replace('_', ' ').title()}: {subvalue}")
                else:
                    print(f"   • {key.replace('_', ' ').title()}: {value}")
    
    # Prevention
    if disease_info.get('prevention'):
        print(f"\n🛡️  PREVENTION")
        if isinstance(disease_info['prevention'], list):
            for measure in disease_info['prevention']:
                print(f"   • {measure}")
        elif isinstance(disease_info['prevention'], dict):
            for key, value in disease_info['prevention'].items():
                print(f"   • {key.replace('_', ' ').title()}: {value}")
    
    # Complications
    if disease_info.get('complications'):
        print(f"\n⚡ COMPLICATIONS")
        if isinstance(disease_info['complications'], list):
            for comp in disease_info['complications']:
                print(f"   • {comp}")
        elif isinstance(disease_info['complications'], dict):
            for key, value in disease_info['complications'].items():
                print(f"   • {key.replace('_', ' ').title()}: {value}")
    
    # Available Datasets
    if disease_info.get('datasets'):
        print(f"\n💾 AVAILABLE DATASETS")
        for dataset_name in disease_info['datasets']:
            # Find dataset details
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
    
    print(f"\n{'='*80}\n")


def compare_diseases(disease_keys: List[str], clinical_data: Dict):
    """Compare multiple diseases side by side"""
    print(f"\n{'='*80}")
    print("DISEASE COMPARISON")
    print(f"{'='*80}\n")
    
    diseases = []
    for key in disease_keys:
        for category, disease_list in clinical_data.items():
            if key in disease_list:
                diseases.append({
                    'key': key,
                    'info': disease_list[key]
                })
    
    if len(diseases) < 2:
        print("Need at least 2 diseases to compare")
        return
    
    # Compare key attributes
    attributes = ['prevalence', 'mortality_rate', 'five_year_survival', 'treatment']
    
    for attr in attributes:
        print(f"\n{attr.replace('_', ' ').upper()}:")
        for disease in diseases:
            name = disease['info'].get('full_name', disease['key'])
            value = disease['info'].get(attr, 'N/A')
            
            # Handle nested attributes
            if attr == 'five_year_survival' and disease['info'].get('prognosis'):
                value = disease['info']['prognosis'].get('five_year_survival', 'N/A')
            
            print(f"   {name}: {value}")


def list_diseases_by_category(clinical_data: Dict):
    """List all diseases with clinical details"""
    print(f"\n{'='*80}")
    print("DISEASES WITH CLINICAL DETAILS")
    print(f"{'='*80}\n")
    
    total = 0
    for category in sorted(clinical_data.keys()):
        diseases = clinical_data[category]
        print(f"\n📁 {category.upper().replace('_', ' ')} ({len(diseases)} diseases)")
        
        for disease_key, disease_info in diseases.items():
            full_name = disease_info.get('full_name', disease_key)
            icd10 = disease_info.get('icd10', 'N/A')
            print(f"   • {full_name} (ICD-10: {icd10})")
            total += 1
    
    print(f"\n{'='*80}")
    print(f"Total: {total} diseases with clinical details")
    print(f"{'='*80}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Advanced disease search with complete clinical details"
    )
    parser.add_argument("disease", nargs='?', type=str,
                       help="Disease name to search for")
    parser.add_argument("--compare", nargs='+',
                       help="Compare multiple diseases")
    parser.add_argument("--list-all", action="store_true",
                       help="List all diseases with clinical details")
    parser.add_argument("--category", type=str,
                       help="Filter by category")
    
    args = parser.parse_args()
    
    # Load data
    print("Loading clinical data...")
    taxonomy, mapping, datasets, clinical, disease_db = load_all_data()
    
    if args.list_all:
        list_diseases_by_category(clinical)
        return
    
    if args.compare:
        compare_diseases(args.compare, clinical)
        return
    
    if not args.disease:
        print("Usage: python scripts/advanced_disease_search.py <disease_name>")
        print("\nExamples:")
        print("  python scripts/advanced_disease_search.py 'nodular melanoma'")
        print("  python scripts/advanced_disease_search.py 'triple negative'")
        print("  python scripts/advanced_disease_search.py 'glioblastoma'")
        print("  python scripts/advanced_disease_search.py 'atrial fibrillation'")
        print("  python scripts/advanced_disease_search.py 'STEMI'")
        print("  python scripts/advanced_disease_search.py --list-all")
        print("\nCompare diseases:")
        print("  python scripts/advanced_disease_search.py --compare nodular_melanoma superficial_spreading_melanoma")
        return
    
    # Search for disease
    results = search_disease_advanced(args.disease, clinical)
    
    if len(results) == 0:
        print(f"\nNo clinical details found for: {args.disease}")
        print("Try: python scripts/advanced_disease_search.py --list-all")
    elif len(results) == 1:
        display_clinical_details(results[0]['key'], results[0]['info'], datasets)
    else:
        print(f"\nMultiple matches found:")
        for i, result in enumerate(results, 1):
            print(f"{i}. {result['info'].get('full_name', result['key'])}")
        print("\nPlease be more specific")


if __name__ == "__main__":
    main()
