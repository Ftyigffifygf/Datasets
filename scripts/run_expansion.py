"""Run database expansion"""
import json
from pathlib import Path

# Load existing database
db_path = Path("data/disease_database.json")
with open(db_path) as f:
    disease_db = json.load(f)

print(f"Starting with {len(disease_db)} diseases")

# Find next ID
max_id = max([int(k.split('_')[1]) for k in disease_db.keys() if k.startswith('disease_')])
next_id = max_id + 1

# Add new diseases
new_diseases = {
    'gastroenterology': {
        'inflammatory_bowel_disease': [
            "Crohn's Disease (Ileocolitis)", "Crohn's Disease (Ileitis)",
            "Ulcerative Colitis (Proctitis)", "Ulcerative Colitis (Pancolitis)",
            "Microscopic Colitis"
        ],
        'liver_disease': [
            "Alcoholic Liver Disease", "Non-Alcoholic Fatty Liver Disease (NAFLD)",
            "Cirrhosis (Compensated)", "Cirrhosis (Decompensated)",
            "Primary Biliary Cholangitis", "Autoimmune Hepatitis",
            "Wilson's Disease", "Hemochromatosis"
        ],
        'peptic_disease': [
            "Gastric Ulcer", "Duodenal Ulcer",
            "Gastroesophageal Reflux Disease (GERD)", "Barrett's Esophagus"
        ]
    },
    'endocrinology': {
        'thyroid_disorders': [
            "Hypothyroidism (Primary)", "Hyperthyroidism (Graves' Disease)",
            "Hashimoto's Thyroiditis", "Thyroid Cancer (Papillary)"
        ],
        'adrenal_disorders': [
            "Addison's Disease", "Cushing's Syndrome", "Pheochromocytoma"
        ]
    },
    'rheumatology': {
        'inflammatory_arthritis': [
            "Rheumatoid Arthritis (Seropositive)", "Psoriatic Arthritis",
            "Ankylosing Spondylitis"
        ],
        'connective_tissue_disease': [
            "Systemic Lupus Erythematosus (SLE)", "Scleroderma (Diffuse)",
            "Sjögren's Syndrome", "Polymyositis"
        ]
    },
    'hematology': {
        'anemia': [
            "Iron Deficiency Anemia", "Vitamin B12 Deficiency Anemia",
            "Sickle Cell Anemia", "Thalassemia Major"
        ],
        'coagulation_disorders': [
            "Hemophilia A", "Von Willebrand Disease",
            "Antiphospholipid Syndrome", "Immune Thrombocytopenic Purpura (ITP)"
        ]
    },
    'nephrology': {
        'glomerular_disease': [
            "IgA Nephropathy", "Minimal Change Disease",
            "Focal Segmental Glomerulosclerosis (FSGS)", "Membranous Nephropathy"
        ],
        'kidney_disease': [
            "Chronic Kidney Disease (Stage 3)", "Chronic Kidney Disease (Stage 4)",
            "Diabetic Nephropathy", "Polycystic Kidney Disease"
        ]
    }
}

added = 0
for category, subcategories in new_diseases.items():
    for subcategory, diseases in subcategories.items():
        for disease_name in diseases:
            disease_id = f"disease_{next_id:04d}"
            disease_db[disease_id] = {
                'id': disease_id,
                'name': disease_name,
                'category': category,
                'parent': subcategory,
                'type': 'subtype'
            }
            next_id += 1
            added += 1

# Save
with open(db_path, 'w') as f:
    json.dump(disease_db, f, indent=2)

print(f"Added {added} new diseases")
print(f"Total now: {len(disease_db)} diseases")
