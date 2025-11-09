"""Expand disease database with additional diseases and details"""
import sys
import yaml
import json
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


def get_additional_diseases():
    """Return comprehensive list of additional diseases to add"""
    additional_diseases = {
        # GASTROINTESTINAL DISEASES (100+ new)
        'gastroenterology': {
            'inflammatory_bowel_disease': [
                "Crohn's Disease (Ileocolitis)",
                "Crohn's Disease (Ileitis)",
                "Crohn's Disease (Gastroduodenal)",
                "Crohn's Disease (Jejunoileitis)",
                "Ulcerative Colitis (Proctitis)",
                "Ulcerative Colitis (Left-sided)",
                "Ulcerative Colitis (Pancolitis)",
                "Microscopic Colitis",
                "Indeterminate Colitis"
            ],
            'liver_disease': [
                "Alcoholic Liver Disease",
                "Non-Alcoholic Fatty Liver Disease (NAFLD)",
                "Non-Alcoholic Steatohepatitis (NASH)",
                "Cirrhosis (Compensated)",
                "Cirrhosis (Decompensated)",
                "Primary Biliary Cholangitis",
                "Primary Sclerosing Cholangitis",
                "Autoimmune Hepatitis",
                "Wilson's Disease",
                "Hemochromatosis",
                "Alpha-1 Antitrypsin Deficiency",
                "Budd-Chiari Syndrome",
                "Portal Hypertension",
                "Hepatic Encephalopathy",
                "Spontaneous Bacterial Peritonitis"
            ],
            'peptic_disease': [
                "Gastric Ulcer",
                "Duodenal Ulcer",
                "Gastroesophageal Reflux Disease (GERD)",
                "Barrett's Esophagus",
                "Esophagitis",
                "Gastritis (H. pylori)",
                "Gastritis (Autoimmune)",
                "Zollinger-Ellison Syndrome"
            ],
            'pancreatic_disease': [
                "Acute Pancreatitis",
                "Chronic Pancreatitis",
                "Pancreatic Pseudocyst",
                "Pancreatic Insufficiency"
            ],
            'intestinal_disease': [
                "Celiac Disease",
                "Irritable Bowel Syndrome (IBS-D)",
                "Irritable Bowel Syndrome (IBS-C)",
                "Irritable Bowel Syndrome (IBS-M)",
                "Small Intestinal Bacterial Overgrowth (SIBO)",
                "Diverticulitis",
                "Diverticulosis",
                "Intestinal Obstruction",
                "Mesenteric Ischemia",
                "Ischemic Colitis"
            ]
        },
        
        # ENDOCRINE DISEASES (50+ new)
        'endocrinology': {
            'thyroid_disorders': [
                "Hypothyroidism (Primary)",
                "Hypothyroidism (Secondary)",
                "Hyperthyroidism (Graves' Disease)",
                "Hyperthyroidism (Toxic Multinodular Goiter)",
                "Hyperthyroidism (Toxic Adenoma)",
                "Hashimoto's Thyroiditis",
                "Subacute Thyroiditis",
                "Thyroid Nodule (Benign)",
                "Thyroid Cancer (Papillary)",
                "Thyroid Cancer (Follicular)",
                "Thyroid Cancer (Medullary)",
                "Thyroid Cancer (Anaplastic)"
            ],
            'adrenal_disorders': [
                "Addison's Disease",
                "Cushing's Syndrome",
                "Cushing's Disease",
                "Pheochromocytoma",
                "Primary Aldosteronism (Conn's Syndrome)",
                "Adrenal Insufficiency",
                "Congenital Adrenal Hyperplasia"
            ],
            'pituitary_disorders': [
                "Acromegaly",
                "Prolactinoma",
                "Growth Hormone Deficiency",
                "Diabetes Insipidus (Central)",
                "Diabetes Insipidus (Nephrogenic)",
                "Hypopituitarism",
                "Pituitary Apoplexy"
            ],
            'metabolic_disorders': [
                "Metabolic Syndrome",
                "Polycystic Ovary Syndrome (PCOS)",
                "Hyperparathyroidism (Primary)",
                "Hyperparathyroidism (Secondary)",
                "Hypoparathyroidism",
                "Osteoporosis",
                "Osteomalacia",
                "Paget's Disease of Bone"
            ]
        },
        
        # RHEUMATOLOGY (40+ new)
        'rheumatology': {
            'inflammatory_arthritis': [
                "Rheumatoid Arthritis (Seropositive)",
                "Rheumatoid Arthritis (Seronegative)",
                "Psoriatic Arthritis",
                "Ankylosing Spondylitis",
                "Reactive Arthritis",
                "Enteropathic Arthritis"
            ],
            'connective_tissue_disease': [
                "Systemic Lupus Erythematosus (SLE)",
                "Scleroderma (Diffuse)",
                "Scleroderma (Limited/CREST)",
                "Sjögren's Syndrome",
                "Mixed Connective Tissue Disease",
                "Polymyositis",
                "Dermatomyositis",
                "Inclusion Body Myositis"
            ],
            'vasculitis': [
                "Giant Cell Arteritis",
                "Takayasu Arteritis",
                "Polyarteritis Nodosa",
                "Granulomatosis with Polyangiitis (Wegener's)",
                "Microscopic Polyangiitis",
                "Eosinophilic Granulomatosis with Polyangiitis (Churg-Strauss)",
                "Henoch-Schönlein Purpura",
                "Behçet's Disease",
                "Kawasaki Disease"
            ],
            'crystal_arthropathy': [
                "Gout (Acute)",
                "Gout (Chronic Tophaceous)",
                "Pseudogout (CPPD)",
                "Calcium Pyrophosphate Deposition Disease"
            ]
        },
        
        # HEMATOLOGY (50+ new)
        'hematology': {
            'anemia': [
                "Iron Deficiency Anemia",
                "Vitamin B12 Deficiency Anemia",
                "Folate Deficiency Anemia",
                "Anemia of Chronic Disease",
                "Sickle Cell Anemia",
                "Thalassemia Major",
                "Thalassemia Minor",
                "Aplastic Anemia",
                "Hemolytic Anemia (Autoimmune)",
                "Hemolytic Anemia (Hereditary Spherocytosis)",
                "G6PD Deficiency",
                "Pernicious Anemia"
            ],
            'coagulation_disorders': [
                "Hemophilia A",
                "Hemophilia B",
                "Von Willebrand Disease",
                "Factor V Leiden",
                "Protein C Deficiency",
                "Protein S Deficiency",
                "Antithrombin Deficiency",
                "Antiphospholipid Syndrome",
                "Disseminated Intravascular Coagulation (DIC)",
                "Thrombotic Thrombocytopenic Purpura (TTP)",
                "Immune Thrombocytopenic Purpura (ITP)"
            ],
            'myeloproliferative': [
                "Polycythemia Vera",
                "Essential Thrombocythemia",
                "Primary Myelofibrosis",
                "Chronic Eosinophilic Leukemia"
            ],
            'plasma_cell_disorders': [
                "Multiple Myeloma",
                "Monoclonal Gammopathy of Undetermined Significance (MGUS)",
                "Waldenström Macroglobulinemia",
                "Amyloidosis (AL)"
            ]
        },
        
        # NEPHROLOGY (30+ new)
        'nephrology': {
            'glomerular_disease': [
                "IgA Nephropathy",
                "Minimal Change Disease",
                "Focal Segmental Glomerulosclerosis (FSGS)",
                "Membranous Nephropathy",
                "Membranoproliferative Glomerulonephritis",
                "Rapidly Progressive Glomerulonephritis",
                "Goodpasture Syndrome",
                "Alport Syndrome"
            ],
            'tubular_disease': [
                "Acute Tubular Necrosis",
                "Acute Interstitial Nephritis",
                "Fanconi Syndrome",
                "Renal Tubular Acidosis (Type 1)",
                "Renal Tubular Acidosis (Type 2)",
                "Renal Tubular Acidosis (Type 4)"
            ],
            'kidney_disease': [
                "Chronic Kidney Disease (Stage 1)",
                "Chronic Kidney Disease (Stage 2)",
                "Chronic Kidney Disease (Stage 3)",
                "Chronic Kidney Disease (Stage 4)",
                "Chronic Kidney Disease (Stage 5/ESRD)",
                "Diabetic Nephropathy",
                "Hypertensive Nephropathy",
                "Polycystic Kidney Disease (Autosomal Dominant)",
                "Polycystic Kidney Disease (Autosomal Recessive)",
                "Nephrotic Syndrome",
                "Nephritic Syndrome"
            ]
        },
        
        # PULMONOLOGY (30+ new)
        'pulmonology': {
            'obstructive_disease': [
                "Chronic Obstructive Pulmonary Disease (COPD)",
                "Chronic Bronchitis",
                "Emphysema (Centrilobular)",
                "Emphysema (Panlobular)",
                "Bronchiectasis",
                "Cystic Fibrosis"
            ],
            'restrictive_disease': [
                "Idiopathic Pulmonary Fibrosis",
                "Sarcoidosis (Pulmonary)",
                "Hypersensitivity Pneumonitis",
                "Asbestosis",
                "Silicosis",
                "Coal Worker's Pneumoconiosis"
            ],
            'vascular_disease': [
                "Pulmonary Embolism (Acute)",
                "Chronic Thromboembolic Pulmonary Hypertension",
                "Pulmonary Arterial Hypertension (Idiopathic)",
                "Pulmonary Arterial Hypertension (Associated)"
            ],
            'pleural_disease': [
                "Pleural Effusion (Transudative)",
                "Pleural Effusion (Exudative)",
                "Empyema",
                "Pneumothorax (Spontaneous)",
                "Pneumothorax (Tension)",
                "Hemothorax",
                "Chylothorax"
            ]
        },
        
        # IMMUNOLOGY (30+ new)
        'immunology': {
            'primary_immunodeficiency': [
                "Common Variable Immunodeficiency (CVID)",
                "Selective IgA Deficiency",
                "X-Linked Agammaglobulinemia",
                "Severe Combined Immunodeficiency (SCID)",
                "DiGeorge Syndrome",
                "Wiskott-Aldrich Syndrome",
                "Chronic Granulomatous Disease"
            ],
            'allergic_disease': [
                "Allergic Rhinitis (Seasonal)",
                "Allergic Rhinitis (Perennial)",
                "Atopic Dermatitis",
                "Food Allergy (IgE-mediated)",
                "Anaphylaxis",
                "Urticaria (Chronic)",
                "Angioedema (Hereditary)",
                "Angioedema (Acquired)"
            ],
            'autoimmune_disease': [
                "Systemic Lupus Erythematosus",
                "Antiphospholipid Syndrome",
                "Systemic Sclerosis",
                "Polymyalgia Rheumatica",
                "Sarcoidosis (Systemic)"
            ]
        },
        
        # UROLOGY (20+ new)
        'urology': {
            'prostate_disease': [
                "Benign Prostatic Hyperplasia (BPH)",
                "Prostatitis (Acute Bacterial)",
                "Prostatitis (Chronic Bacterial)",
                "Prostatitis (Chronic Pelvic Pain Syndrome)"
            ],
            'urinary_tract': [
                "Urinary Tract Infection (Cystitis)",
                "Pyelonephritis (Acute)",
                "Pyelonephritis (Chronic)",
                "Urethritis (Gonococcal)",
                "Urethritis (Non-gonococcal)",
                "Urinary Incontinence (Stress)",
                "Urinary Incontinence (Urge)",
                "Urinary Incontinence (Overflow)",
                "Neurogenic Bladder",
                "Interstitial Cystitis"
            ],
            'stone_disease': [
                "Kidney Stones (Calcium Oxalate)",
                "Kidney Stones (Uric Acid)",
                "Kidney Stones (Struvite)",
                "Kidney Stones (Cystine)"
            ]
        },
        
        # GYNECOLOGY (25+ new)
        'gynecology': {
            'menstrual_disorders': [
                "Amenorrhea (Primary)",
                "Amenorrhea (Secondary)",
                "Dysmenorrhea (Primary)",
                "Dysmenorrhea (Secondary)",
                "Menorrhagia",
                "Oligomenorrhea",
                "Premenstrual Syndrome (PMS)",
                "Premenstrual Dysphoric Disorder (PMDD)"
            ],
            'reproductive_disorders': [
                "Endometriosis",
                "Adenomyosis",
                "Uterine Fibroids (Leiomyoma)",
                "Ovarian Cysts (Functional)",
                "Ovarian Cysts (Dermoid)",
                "Pelvic Inflammatory Disease",
                "Ectopic Pregnancy"
            ],
            'menopause': [
                "Perimenopause",
                "Menopause",
                "Premature Ovarian Insufficiency"
            ]
        }
    }
    
    return additional_diseases


def expand_database():
    """Expand the disease database with additional diseases"""
    print("=" * 80)
    print("EXPANDING DISEASE DATABASE")
    print("=" * 80)
    
    # Load existing database
    db_path = Path("data/disease_database.json")
    if db_path.exists():
        with open(db_path) as f:
            disease_db = json.load(f)
        print(f"\nLoaded {len(disease_db)} existing diseases")
        starting_count = len(disease_db)
        
        # Find next available ID
        max_id = 0
        for key in disease_db.keys():
            if key.startswith('disease_'):
                try:
                    num = int(key.split('_')[1])
                    max_id = max(max_id, num)
                except:
                    pass
        next_id = max_id + 1
    else:
        print("\nNo existing database found, creating new one")
        disease_db = {}
        starting_count = 0
        next_id = 1
    
    # Get additional diseases
    additional_diseases = get_additional_diseases()
    
    # Add new diseases
    added_count = 0
    for category, subcategories in additional_diseases.items():
        print(f"\nAdding {category} diseases...")
        
        for subcategory, diseases in subcategories.items():
            for disease_name in diseases:
                disease_id = f"disease_{next_id:04d}"
                
                disease_db[disease_id] = {
                    'id': disease_id,
                    'name': disease_name,
                    'category': category,
                    'parent': subcategory,
                    'type': 'subtype',
                    'search_terms': [
                        disease_name.lower(),
                        disease_name.lower().replace(' ', '_'),
                        disease_name.lower().replace('(', '').replace(')', '').replace("'", '')
                    ]
                }
                
                next_id += 1
                added_count += 1
        
        print(f"  Added {len([d for sc in subcategories.values() for d in sc])} diseases")
    
    # Save updated database
    print(f"\nSaving database...")
    with open(db_path, 'w') as f:
        json.dump(disease_db, f, indent=2)
    
    print(f"\n{'=' * 80}")
    print("DATABASE EXPANSION COMPLETE")
    print(f"{'=' * 80}")
    print(f"Starting diseases: {starting_count}")
    print(f"Added diseases: {added_count}")
    print(f"Total diseases: {len(disease_db)}")
    print(f"{'=' * 80}\n")
    
    # Show breakdown by category
    print("BREAKDOWN BY CATEGORY:")
    category_counts = {}
    for disease in disease_db.values():
        cat = disease.get('category', 'unknown')
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    for category in sorted(category_counts.keys()):
        print(f"  {category}: {category_counts[category]} diseases")
    
    return disease_db


def main():
    """Main function"""
    expand_database()


if __name__ == "__main__":
    main()
