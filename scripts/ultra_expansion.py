"""Ultra-wide database expansion - Add 1000+ more diseases"""
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

# Ultra-wide disease expansion
ultra_diseases = {
    'gastroenterology_expanded': {
        'esophageal_disorders': [
            "Achalasia", "Esophageal Spasm (Diffuse)", "Esophageal Stricture",
            "Esophageal Varices", "Mallory-Weiss Tear", "Boerhaave Syndrome",
            "Esophageal Cancer (Adenocarcinoma)", "Esophageal Cancer (Squamous Cell)",
            "Eosinophilic Esophagitis", "Zenker's Diverticulum"
        ],
        'stomach_disorders': [
            "Gastric Cancer (Intestinal Type)", "Gastric Cancer (Diffuse Type)",
            "Gastric Lymphoma (MALT)", "Gastric Polyps", "Gastroparesis",
            "Gastric Outlet Obstruction", "Ménétrier's Disease"
        ],
        'small_intestine': [
            "Small Bowel Obstruction", "Ileus", "Meckel's Diverticulum",
            "Whipple's Disease", "Tropical Sprue", "Lactose Intolerance",
            "Fructose Malabsorption", "Small Intestinal Lymphoma"
        ],
        'colon_disorders': [
            "Colonic Polyps (Adenomatous)", "Colonic Polyps (Hyperplastic)",
            "Familial Adenomatous Polyposis", "Lynch Syndrome",
            "Pseudomembranous Colitis", "Ischemic Colitis",
            "Ogilvie Syndrome", "Toxic Megacolon"
        ],
        'anorectal': [
            "Hemorrhoids (Internal)", "Hemorrhoids (External)",
            "Anal Fissure", "Perianal Abscess", "Anal Fistula",
            "Rectal Prolapse", "Anal Cancer"
        ]
    },
    
    'endocrinology_expanded': {
        'pituitary_disorders': [
            "Acromegaly", "Gigantism", "Prolactinoma",
            "Growth Hormone Deficiency", "Diabetes Insipidus (Central)",
            "Diabetes Insipidus (Nephrogenic)", "Hypopituitarism",
            "Pituitary Apoplexy", "Empty Sella Syndrome",
            "Sheehan's Syndrome"
        ],
        'parathyroid': [
            "Primary Hyperparathyroidism", "Secondary Hyperparathyroidism",
            "Tertiary Hyperparathyroidism", "Hypoparathyroidism",
            "Pseudohypoparathyroidism"
        ],
        'metabolic_bone': [
            "Osteoporosis (Postmenopausal)", "Osteoporosis (Senile)",
            "Osteoporosis (Secondary)", "Osteomalacia", "Rickets",
            "Paget's Disease of Bone", "Osteogenesis Imperfecta"
        ],
        'reproductive_endocrine': [
            "Polycystic Ovary Syndrome (PCOS)", "Hypogonadism (Primary)",
            "Hypogonadism (Secondary)", "Klinefelter Syndrome",
            "Turner Syndrome", "Androgen Insensitivity Syndrome"
        ]
    },
    
    'rheumatology_expanded': {
        'vasculitis': [
            "Giant Cell Arteritis", "Takayasu Arteritis",
            "Polyarteritis Nodosa", "Granulomatosis with Polyangiitis",
            "Microscopic Polyangiitis", "Eosinophilic Granulomatosis with Polyangiitis",
            "Henoch-Schönlein Purpura", "Behçet's Disease",
            "Kawasaki Disease", "Buerger's Disease"
        ],
        'crystal_arthropathy': [
            "Gout (Acute)", "Gout (Chronic Tophaceous)",
            "Pseudogout (CPPD)", "Calcium Pyrophosphate Deposition Disease"
        ],
        'soft_tissue_rheumatism': [
            "Fibromyalgia", "Polymyalgia Rheumatica",
            "Rotator Cuff Tendinitis", "Lateral Epicondylitis (Tennis Elbow)",
            "Medial Epicondylitis (Golfer's Elbow)", "De Quervain's Tenosynovitis",
            "Trigger Finger", "Plantar Fasciitis", "Achilles Tendinitis",
            "Bursitis (Olecranon)", "Bursitis (Prepatellar)", "Bursitis (Trochanteric)"
        ]
    },
    
    'hematology_expanded': {
        'myeloproliferative': [
            "Polycythemia Vera", "Essential Thrombocythemia",
            "Primary Myelofibrosis", "Chronic Eosinophilic Leukemia"
        ],
        'myelodysplastic': [
            "Myelodysplastic Syndrome (Low Risk)", "Myelodysplastic Syndrome (High Risk)",
            "Refractory Anemia", "Refractory Anemia with Ring Sideroblasts"
        ],
        'plasma_cell': [
            "Multiple Myeloma (Smoldering)", "Multiple Myeloma (Active)",
            "MGUS", "Waldenström Macroglobulinemia",
            "Amyloidosis (AL)", "Amyloidosis (AA)"
        ],
        'hemolytic_anemia': [
            "Hereditary Spherocytosis", "Hereditary Elliptocytosis",
            "G6PD Deficiency", "Pyruvate Kinase Deficiency",
            "Autoimmune Hemolytic Anemia (Warm)", "Autoimmune Hemolytic Anemia (Cold)",
            "Paroxysmal Nocturnal Hemoglobinuria", "Microangiopathic Hemolytic Anemia"
        ]
    },
    
    'nephrology_expanded': {
        'tubular_disorders': [
            "Acute Tubular Necrosis", "Acute Interstitial Nephritis",
            "Fanconi Syndrome", "Renal Tubular Acidosis (Type 1)",
            "Renal Tubular Acidosis (Type 2)", "Renal Tubular Acidosis (Type 4)",
            "Bartter Syndrome", "Gitelman Syndrome"
        ],
        'nephrotic_syndrome': [
            "Minimal Change Disease", "Focal Segmental Glomerulosclerosis",
            "Membranous Nephropathy", "Diabetic Nephropathy"
        ],
        'nephritic_syndrome': [
            "Post-Streptococcal Glomerulonephritis", "IgA Nephropathy",
            "Rapidly Progressive Glomerulonephritis", "Goodpasture Syndrome",
            "Alport Syndrome"
        ]
    },
    
    'infectious_diseases_expanded': {
        'bacterial_infections': [
            "Sepsis (Gram-positive)", "Sepsis (Gram-negative)",
            "Meningitis (Bacterial)", "Meningitis (Viral)", "Meningitis (Fungal)",
            "Endocarditis (Acute)", "Endocarditis (Subacute)",
            "Osteomyelitis (Acute)", "Osteomyelitis (Chronic)",
            "Cellulitis", "Erysipelas", "Necrotizing Fasciitis",
            "Lyme Disease (Early)", "Lyme Disease (Late)",
            "Syphilis (Primary)", "Syphilis (Secondary)", "Syphilis (Tertiary)",
            "Gonorrhea", "Chlamydia", "Mycoplasma Infection"
        ],
        'viral_infections': [
            "HIV (Acute)", "HIV (Chronic)", "AIDS",
            "Hepatitis A", "Hepatitis B (Acute)", "Hepatitis B (Chronic)",
            "Hepatitis C (Acute)", "Hepatitis C (Chronic)",
            "Hepatitis D", "Hepatitis E",
            "Epstein-Barr Virus (Mononucleosis)", "Cytomegalovirus",
            "Herpes Simplex Virus Type 1", "Herpes Simplex Virus Type 2",
            "Varicella-Zoster Virus", "Human Papillomavirus (HPV)",
            "Dengue Fever", "Zika Virus", "West Nile Virus",
            "Rabies", "Ebola Virus Disease"
        ],
        'parasitic_infections': [
            "Malaria (P. falciparum)", "Malaria (P. vivax)",
            "Toxoplasmosis", "Giardiasis", "Cryptosporidiosis",
            "Amebiasis", "Leishmaniasis (Cutaneous)", "Leishmaniasis (Visceral)",
            "Trypanosomiasis (African)", "Trypanosomiasis (American/Chagas)",
            "Schistosomiasis", "Filariasis", "Ascariasis",
            "Hookworm", "Pinworm", "Tapeworm"
        ],
        'fungal_infections': [
            "Candidiasis (Oral)", "Candidiasis (Esophageal)", "Candidiasis (Vulvovaginal)",
            "Aspergillosis (Invasive)", "Aspergillosis (Allergic)",
            "Cryptococcosis", "Histoplasmosis", "Coccidioidomycosis",
            "Blastomycosis", "Mucormycosis", "Pneumocystis Pneumonia"
        ]
    },
    
    'dermatology_expanded': {
        'inflammatory_skin': [
            "Psoriasis (Plaque)", "Psoriasis (Guttate)", "Psoriasis (Inverse)",
            "Psoriasis (Pustular)", "Psoriasis (Erythrodermic)",
            "Eczema (Atopic)", "Eczema (Contact)", "Eczema (Dyshidrotic)",
            "Eczema (Nummular)", "Eczema (Seborrheic)",
            "Rosacea (Erythematotelangiectatic)", "Rosacea (Papulopustular)",
            "Rosacea (Phymatous)", "Rosacea (Ocular)",
            "Lichen Planus", "Lichen Sclerosus", "Pityriasis Rosea",
            "Vitiligo", "Alopecia Areata", "Hidradenitis Suppurativa"
        ],
        'infections_skin': [
            "Impetigo", "Folliculitis", "Furuncle", "Carbuncle",
            "Cellulitis", "Erysipelas", "Abscess",
            "Tinea Corporis", "Tinea Cruris", "Tinea Pedis",
            "Tinea Capitis", "Tinea Versicolor",
            "Scabies", "Pediculosis (Lice)", "Molluscum Contagiosum",
            "Warts (Common)", "Warts (Plantar)", "Warts (Genital)"
        ],
        'autoimmune_skin': [
            "Pemphigus Vulgaris", "Bullous Pemphigoid",
            "Dermatitis Herpetiformis", "Linear IgA Disease"
        ]
    },
    
    'ophthalmology_expanded': {
        'corneal_disorders': [
            "Keratoconus", "Corneal Ulcer (Bacterial)", "Corneal Ulcer (Fungal)",
            "Corneal Abrasion", "Corneal Dystrophy (Fuchs')",
            "Corneal Dystrophy (Lattice)", "Keratitis (Bacterial)",
            "Keratitis (Viral)", "Keratitis (Fungal)"
        ],
        'uveal_disorders': [
            "Anterior Uveitis", "Intermediate Uveitis", "Posterior Uveitis",
            "Panuveitis", "Iritis", "Choroiditis"
        ],
        'retinal_vascular': [
            "Central Retinal Artery Occlusion", "Branch Retinal Artery Occlusion",
            "Central Retinal Vein Occlusion", "Branch Retinal Vein Occlusion",
            "Hypertensive Retinopathy", "Retinopathy of Prematurity"
        ],
        'optic_nerve': [
            "Optic Neuritis", "Papilledema", "Optic Atrophy",
            "Ischemic Optic Neuropathy (Arteritic)", "Ischemic Optic Neuropathy (Non-arteritic)"
        ]
    },
    
    'neurology_expanded': {
        'movement_disorders': [
            "Essential Tremor", "Dystonia (Focal)", "Dystonia (Generalized)",
            "Huntington's Disease", "Wilson's Disease",
            "Restless Legs Syndrome", "Periodic Limb Movement Disorder",
            "Tourette Syndrome", "Chorea", "Athetosis", "Myoclonus"
        ],
        'neuromuscular': [
            "Myasthenia Gravis", "Lambert-Eaton Myasthenic Syndrome",
            "Guillain-Barré Syndrome", "Chronic Inflammatory Demyelinating Polyneuropathy",
            "Charcot-Marie-Tooth Disease", "Muscular Dystrophy (Duchenne)",
            "Muscular Dystrophy (Becker)", "Muscular Dystrophy (Myotonic)",
            "Amyotrophic Lateral Sclerosis (ALS)", "Spinal Muscular Atrophy"
        ],
        'headache_disorders': [
            "Migraine without Aura", "Migraine with Aura",
            "Chronic Migraine", "Hemiplegic Migraine",
            "Tension-Type Headache (Episodic)", "Tension-Type Headache (Chronic)",
            "Cluster Headache", "Paroxysmal Hemicrania",
            "Trigeminal Neuralgia", "Occipital Neuralgia"
        ],
        'demyelinating': [
            "Multiple Sclerosis (Relapsing-Remitting)",
            "Multiple Sclerosis (Secondary Progressive)",
            "Multiple Sclerosis (Primary Progressive)",
            "Neuromyelitis Optica", "Acute Disseminated Encephalomyelitis",
            "Transverse Myelitis"
        ]
    },
    
    'cardiology_expanded': {
        'valvular_disease': [
            "Aortic Stenosis (Mild)", "Aortic Stenosis (Moderate)", "Aortic Stenosis (Severe)",
            "Aortic Regurgitation (Acute)", "Aortic Regurgitation (Chronic)",
            "Mitral Stenosis", "Mitral Regurgitation (Acute)", "Mitral Regurgitation (Chronic)",
            "Mitral Valve Prolapse", "Tricuspid Regurgitation",
            "Pulmonary Stenosis", "Endocarditis (Native Valve)", "Endocarditis (Prosthetic Valve)"
        ],
        'pericardial_disease': [
            "Acute Pericarditis", "Chronic Pericarditis",
            "Constrictive Pericarditis", "Pericardial Effusion",
            "Cardiac Tamponade", "Dressler Syndrome"
        ],
        'aortic_disease': [
            "Aortic Aneurysm (Thoracic)", "Aortic Aneurysm (Abdominal)",
            "Aortic Dissection (Type A)", "Aortic Dissection (Type B)",
            "Coarctation of Aorta", "Marfan Syndrome"
        ]
    },
    
    'oncology_expanded': {
        'head_neck_cancer': [
            "Oral Cancer (Tongue)", "Oral Cancer (Floor of Mouth)",
            "Oropharyngeal Cancer", "Nasopharyngeal Cancer",
            "Laryngeal Cancer (Glottic)", "Laryngeal Cancer (Supraglottic)",
            "Salivary Gland Cancer", "Thyroid Cancer (Papillary)",
            "Thyroid Cancer (Follicular)", "Thyroid Cancer (Medullary)",
            "Thyroid Cancer (Anaplastic)"
        ],
        'gi_cancer': [
            "Esophageal Cancer (Adenocarcinoma)", "Esophageal Cancer (Squamous)",
            "Gastric Cancer (Intestinal)", "Gastric Cancer (Diffuse)",
            "Small Bowel Cancer", "Colon Cancer (Right-sided)", "Colon Cancer (Left-sided)",
            "Rectal Cancer", "Anal Cancer",
            "Pancreatic Cancer (Ductal Adenocarcinoma)", "Pancreatic Neuroendocrine Tumor",
            "Hepatocellular Carcinoma", "Cholangiocarcinoma (Intrahepatic)",
            "Cholangiocarcinoma (Extrahepatic)", "Gallbladder Cancer"
        ],
        'urological_cancer': [
            "Bladder Cancer (Urothelial)", "Bladder Cancer (Squamous)",
            "Renal Cell Carcinoma (Clear Cell)", "Renal Cell Carcinoma (Papillary)",
            "Renal Cell Carcinoma (Chromophobe)", "Wilms Tumor",
            "Testicular Cancer (Seminoma)", "Testicular Cancer (Non-seminoma)",
            "Penile Cancer"
        ],
        'gynecologic_cancer': [
            "Cervical Cancer (Squamous)", "Cervical Cancer (Adenocarcinoma)",
            "Endometrial Cancer (Type I)", "Endometrial Cancer (Type II)",
            "Ovarian Cancer (Serous)", "Ovarian Cancer (Mucinous)",
            "Ovarian Cancer (Endometrioid)", "Ovarian Cancer (Clear Cell)",
            "Vulvar Cancer", "Vaginal Cancer",
            "Gestational Trophoblastic Disease"
        ],
        'sarcomas': [
            "Osteosarcoma", "Ewing Sarcoma", "Chondrosarcoma",
            "Liposarcoma", "Leiomyosarcoma", "Rhabdomyosarcoma",
            "Synovial Sarcoma", "Malignant Fibrous Histiocytoma",
            "Gastrointestinal Stromal Tumor (GIST)"
        ],
        'neuroendocrine': [
            "Carcinoid Tumor (Typical)", "Carcinoid Tumor (Atypical)",
            "Small Cell Carcinoma", "Large Cell Neuroendocrine Carcinoma",
            "Pheochromocytoma", "Paraganglioma"
        ]
    },
    
    'autoimmune_systemic': {
        'connective_tissue': [
            "Systemic Lupus Erythematosus", "Drug-Induced Lupus",
            "Systemic Sclerosis (Diffuse)", "Systemic Sclerosis (Limited/CREST)",
            "Mixed Connective Tissue Disease", "Undifferentiated Connective Tissue Disease",
            "Sjögren's Syndrome (Primary)", "Sjögren's Syndrome (Secondary)",
            "Polymyositis", "Dermatomyositis", "Inclusion Body Myositis",
            "Eosinophilic Fasciitis", "Relapsing Polychondritis"
        ],
        'organ_specific': [
            "Autoimmune Hepatitis", "Primary Biliary Cholangitis",
            "Primary Sclerosing Cholangitis", "Autoimmune Pancreatitis",
            "Celiac Disease", "Inflammatory Bowel Disease",
            "Autoimmune Thyroiditis", "Graves' Disease",
            "Type 1 Diabetes", "Addison's Disease",
            "Vitiligo", "Alopecia Areata", "Pemphigus Vulgaris"
        ]
    },
    
    'rare_diseases': {
        'genetic_disorders': [
            "Cystic Fibrosis", "Sickle Cell Disease", "Thalassemia",
            "Hemophilia A", "Hemophilia B", "Von Willebrand Disease",
            "Huntington's Disease", "Duchenne Muscular Dystrophy",
            "Marfan Syndrome", "Ehlers-Danlos Syndrome",
            "Osteogenesis Imperfecta", "Achondroplasia",
            "Neurofibromatosis Type 1", "Neurofibromatosis Type 2",
            "Tuberous Sclerosis", "Von Hippel-Lindau Disease"
        ],
        'metabolic_disorders': [
            "Phenylketonuria", "Galactosemia", "Maple Syrup Urine Disease",
            "Homocystinuria", "Gaucher Disease", "Fabry Disease",
            "Pompe Disease", "Tay-Sachs Disease", "Niemann-Pick Disease",
            "Mucopolysaccharidosis", "Glycogen Storage Disease"
        ],
        'orphan_diseases': [
            "Amyotrophic Lateral Sclerosis (ALS)", "Huntington's Disease",
            "Myasthenia Gravis", "Guillain-Barré Syndrome",
            "Sarcoidosis", "Pulmonary Arterial Hypertension",
            "Systemic Sclerosis", "Sjögren's Syndrome"
        ]
    },
    
    'toxicology': {
        'poisoning': [
            "Acetaminophen Overdose", "Salicylate Toxicity",
            "Opioid Overdose", "Benzodiazepine Overdose",
            "Tricyclic Antidepressant Overdose", "Beta-Blocker Overdose",
            "Calcium Channel Blocker Overdose", "Digoxin Toxicity",
            "Lithium Toxicity", "Theophylline Toxicity",
            "Carbon Monoxide Poisoning", "Cyanide Poisoning",
            "Organophosphate Poisoning", "Lead Poisoning",
            "Mercury Poisoning", "Arsenic Poisoning"
        ]
    },
    
    'nutritional_disorders': {
        'vitamin_deficiencies': [
            "Vitamin A Deficiency", "Vitamin B1 Deficiency (Beriberi)",
            "Vitamin B2 Deficiency", "Vitamin B3 Deficiency (Pellagra)",
            "Vitamin B6 Deficiency", "Vitamin B12 Deficiency",
            "Vitamin C Deficiency (Scurvy)", "Vitamin D Deficiency",
            "Vitamin E Deficiency", "Vitamin K Deficiency"
        ],
        'mineral_deficiencies': [
            "Iron Deficiency", "Calcium Deficiency",
            "Magnesium Deficiency", "Zinc Deficiency",
            "Iodine Deficiency", "Selenium Deficiency"
        ],
        'malnutrition': [
            "Protein-Energy Malnutrition (Marasmus)",
            "Protein-Energy Malnutrition (Kwashiorkor)",
            "Cachexia", "Failure to Thrive"
        ]
    }
}

added = 0
for category, subcategories in ultra_diseases.items():
    print(f"\nAdding {category}...")
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
                    disease_name.lower().replace('(', '').replace(')', '').replace('-', '_')
                ]
            }
            next_id += 1
            added += 1
    print(f"  Added {sum(len(d) for d in subcategories.values())} diseases")

# Save
with open(db_path, 'w') as f:
    json.dump(disease_db, f, indent=2)

print(f"\n{'='*80}")
print(f"ULTRA-WIDE EXPANSION COMPLETE!")
print(f"{'='*80}")
print(f"Added: {added} new diseases")
print(f"Total: {len(disease_db)} diseases")
print(f"{'='*80}")

# Show category breakdown
cats = {}
for d in disease_db.values():
    cat = d.get('category', 'unknown')
    cats[cat] = cats.get(cat, 0) + 1

print("\nTop 20 Categories by Disease Count:")
sorted_cats = sorted(cats.items(), key=lambda x: x[1], reverse=True)
for i, (cat, count) in enumerate(sorted_cats[:20], 1):
    print(f"  {i}. {cat}: {count} diseases")

print(f"\nTotal Categories: {len(cats)}")
