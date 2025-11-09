"""Generate comprehensive individual disease database"""
import sys
import yaml
import json
from pathlib import Path
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


def extract_all_diseases(taxonomy, mapping, datasets):
    """Extract every individual disease with complete information"""
    all_diseases = {}
    disease_id = 1
    
    def process_taxonomy(data, category='', parent='', level=0):
        nonlocal disease_id
        
        if isinstance(data, dict):
            for key, value in data.items():
                full_path = f"{parent}/{key}" if parent else key
                
                if isinstance(value, list):
                    # List of disease names
                    for disease in value:
                        disease_key = f"disease_{disease_id:04d}"
                        disease_id += 1
                        
                        all_diseases[disease_key] = {
                            'id': disease_key,
                            'name': disease,
                            'category': category or key,
                            'parent': parent,
                            'level': level,
                            'type': 'subtype',
                            'search_terms': [
                                disease.lower(),
                                disease.lower().replace(' ', '_'),
                                disease.lower().replace('(', '').replace(')', '')
                            ]
                        }
                elif isinstance(value, dict):
                    process_taxonomy(value, category or key, full_path, level + 1)
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, str):
                    disease_key = f"disease_{disease_id:04d}"
                    disease_id += 1
                    
                    all_diseases[disease_key] = {
                        'id': disease_key,
                        'name': item,
                        'category': category,
                        'parent': parent,
                        'level': level,
                        'type': 'subtype',
                        'search_terms': [
                            item.lower(),
                            item.lower().replace(' ', '_')
                        ]
                    }
    
    # Process taxonomy
    for category, diseases_data in taxonomy.items():
        process_taxonomy(diseases_data, category)
    
    # Add diseases from mapping with dataset information
    for disease_key, disease_info in mapping.items():
        if isinstance(disease_info, dict):
            # Check if it has datasets directly
            if 'datasets' in disease_info:
                did = f"disease_{disease_id:04d}"
                disease_id += 1
                
                all_diseases[did] = {
                    'id': did,
                    'name': disease_key.replace('_', ' ').title(),
                    'category': 'mapped',
                    'type': 'mapped',
                    'has_datasets': True,
                    'datasets': disease_info['datasets'],
                    'samples': disease_info.get('samples', 'N/A'),
                    'modalities': disease_info.get('modalities', []),
                    'search_terms': [disease_key, disease_key.replace('_', ' ')]
                }
            else:
                # Has subtypes
                for subtype_key, subtype_info in disease_info.items():
                    if isinstance(subtype_info, dict) and 'datasets' in subtype_info:
                        did = f"disease_{disease_id:04d}"
                        disease_id += 1
                        
                        all_diseases[did] = {
                            'id': did,
                            'name': subtype_key.replace('_', ' ').title(),
                            'category': disease_key,
                            'parent': disease_key,
                            'type': 'mapped_subtype',
                            'has_datasets': True,
                            'datasets': subtype_info['datasets'],
                            'samples': subtype_info.get('samples', 'N/A'),
                            'modalities': subtype_info.get('modalities', []),
                            'search_terms': [
                                subtype_key,
                                subtype_key.replace('_', ' '),
                                f"{disease_key}_{subtype_key}"
                            ]
                        }
    
    return all_diseases


def add_clinical_information(all_diseases):
    """Add clinical information to diseases"""
    clinical_db = {
        'Superficial Spreading Melanoma': {
            'prevalence': '70% of melanomas',
            'characteristics': 'Horizontal growth phase before vertical invasion',
            'prognosis': 'Better than nodular melanoma',
            'common_sites': 'Trunk (men), Legs (women)',
            'age_group': 'Middle-aged adults',
            'risk_factors': ['UV exposure', 'Fair skin', 'Multiple nevi']
        },
        'Nodular Melanoma': {
            'prevalence': '15% of melanomas',
            'characteristics': 'Vertical growth from onset, most aggressive',
            'prognosis': 'Poor if not caught early',
            'common_sites': 'Any body site',
            'age_group': 'Older adults',
            'risk_factors': ['UV exposure', 'Fair skin', 'Previous melanoma']
        },
        'Invasive Ductal Carcinoma': {
            'prevalence': '80% of breast cancers',
            'characteristics': 'Originates in milk ducts, can spread',
            'prognosis': 'Depends on stage and molecular subtype',
            'treatment': 'Surgery + chemotherapy + radiation',
            'molecular_subtypes': ['Luminal A', 'Luminal B', 'HER2+', 'Triple Negative']
        },
        'Triple Negative': {
            'prevalence': '15% of breast cancers',
            'characteristics': 'ER-, PR-, HER2-',
            'prognosis': 'Most aggressive breast cancer',
            'treatment': 'Chemotherapy (limited targeted options)',
            'risk_factors': ['BRCA1 mutation', 'Younger age', 'African ancestry']
        },
        'Glioblastoma': {
            'prevalence': 'Most common malignant brain tumor',
            'characteristics': 'Grade IV astrocytoma, highly infiltrative',
            'prognosis': 'Median survival 15 months',
            'treatment': 'Surgery + radiation + temozolomide',
            'molecular_markers': ['IDH status', 'MGMT methylation']
        },
        'Atrial Fibrillation': {
            'prevalence': 'Most common arrhythmia, 2-4% of adults',
            'characteristics': 'Irregular, rapid atrial activity',
            'complications': '5x increased stroke risk',
            'treatment': 'Rate/rhythm control + anticoagulation',
            'types': ['Paroxysmal', 'Persistent', 'Permanent']
        },
        'STEMI': {
            'full_name': 'ST-Elevation Myocardial Infarction',
            'characteristics': 'Complete coronary artery occlusion',
            'urgency': 'Medical emergency - time is muscle',
            'treatment': 'Immediate reperfusion (PCI or thrombolysis)',
            'goal': 'Door-to-balloon time <90 minutes'
        },
        'Pneumococcal': {
            'full_name': 'Pneumococcal Pneumonia',
            'organism': 'Streptococcus pneumoniae',
            'prevalence': 'Most common bacterial pneumonia',
            'prevention': 'Vaccines available (PCV13, PPSV23)',
            'treatment': 'Beta-lactam antibiotics'
        },
        'MDR-TB': {
            'full_name': 'Multi-Drug Resistant Tuberculosis',
            'definition': 'Resistant to isoniazid and rifampicin',
            'treatment_duration': '18-24 months',
            'treatment': 'Second-line drugs with more side effects',
            'global_burden': '3.3% of new TB cases'
        }
    }
    
    for disease_id, disease_info in all_diseases.items():
        disease_name = disease_info['name']
        if disease_name in clinical_db:
            disease_info['clinical'] = clinical_db[disease_name]
    
    return all_diseases


def generate_markdown_files(all_diseases, output_dir):
    """Generate individual markdown file for each disease"""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Group by category
    by_category = {}
    for disease_id, disease_info in all_diseases.items():
        category = disease_info['category']
        if category not in by_category:
            by_category[category] = []
        by_category[category].append((disease_id, disease_info))
    
    # Generate index file
    with open(output_dir / "INDEX.md", 'w') as f:
        f.write("# Individual Disease Database\n\n")
        f.write(f"Total Diseases: {len(all_diseases)}\n\n")
        
        for category in sorted(by_category.keys()):
            f.write(f"\n## {category.upper().replace('_', ' ')}\n\n")
            diseases = sorted(by_category[category], key=lambda x: x[1]['name'])
            
            for disease_id, disease_info in diseases[:100]:  # Limit per category
                disease_name = disease_info['name']
                filename = disease_id + ".md"
                f.write(f"- [{disease_name}]({filename})\n")
    
    # Generate individual files
    count = 0
    for disease_id, disease_info in all_diseases.items():
        filename = output_dir / f"{disease_id}.md"
        
        with open(filename, 'w') as f:
            f.write(f"# {disease_info['name']}\n\n")
            
            f.write("## Basic Information\n\n")
            f.write(f"- **ID**: {disease_info['id']}\n")
            f.write(f"- **Category**: {disease_info['category']}\n")
            if disease_info.get('parent'):
                f.write(f"- **Parent**: {disease_info['parent']}\n")
            f.write(f"- **Type**: {disease_info['type']}\n")
            
            if disease_info.get('clinical'):
                f.write("\n## Clinical Information\n\n")
                for key, value in disease_info['clinical'].items():
                    f.write(f"- **{key.replace('_', ' ').title()}**: {value}\n")
            
            if disease_info.get('has_datasets'):
                f.write("\n## Available Datasets\n\n")
                f.write(f"- **Datasets**: {', '.join(disease_info['datasets'])}\n")
                f.write(f"- **Samples**: {disease_info['samples']}\n")
                f.write(f"- **Modalities**: {disease_info['modalities']}\n")
            
            f.write("\n## Search Terms\n\n")
            for term in disease_info['search_terms']:
                f.write(f"- {term}\n")
        
        count += 1
        if count % 100 == 0:
            print(f"Generated {count} files...")
    
    print(f"\nTotal files generated: {count}")
    return count


def main():
    print("Loading data...")
    taxonomy, mapping, datasets = load_all_data()
    
    print("Extracting all diseases...")
    all_diseases = extract_all_diseases(taxonomy, mapping, datasets)
    
    print(f"Found {len(all_diseases)} individual diseases")
    
    print("Adding clinical information...")
    all_diseases = add_clinical_information(all_diseases)
    
    # Save as JSON
    print("Saving disease database...")
    with open("data/disease_database.json", 'w') as f:
        json.dump(all_diseases, f, indent=2)
    
    print("Saved to: data/disease_database.json")
    
    # Generate markdown files
    print("\nGenerating individual markdown files...")
    count = generate_markdown_files(all_diseases, "docs/diseases")
    
    print(f"\n{'='*80}")
    print(f"Disease Database Generated Successfully!")
    print(f"{'='*80}")
    print(f"Total Diseases: {len(all_diseases)}")
    print(f"JSON Database: data/disease_database.json")
    print(f"Markdown Files: docs/diseases/ ({count} files)")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
