# 🆕 New Medical Specialties - Quick Reference Guide

## Overview
This guide provides quick access to the 15 new medical specialties added in the Super Expansion, bringing the total database to **1,865+ diseases** across **61+ specialties**.

---

## 1. 🩸 Hematology Expanded (46 diseases)

### Categories
- **Anemias** (13): Iron deficiency, B12 deficiency, Folate deficiency, Aplastic, Hemolytic, Sickle cell, Thalassemia variants
- **Bleeding Disorders** (8): Hemophilia A/B, Von Willebrand types, Factor V Leiden, DIC
- **Clotting Disorders** (7): DVT, PE, Antiphospholipid syndrome, Protein C/S deficiency
- **Blood Cancers** (14): Leukemias (ALL, AML, CLL, CML), Lymphomas, Multiple myeloma
- **Other** (4): Polycythemia vera, Essential thrombocythemia, Myelofibrosis

### Key Datasets
- TCGA-LAML (Acute Myeloid Leukemia)
- TARGET-ALL (Pediatric Leukemia)
- UK Biobank Hematology
- CPTAC-3 Blood Cancers

### Search Examples
```bash
python scripts/search_individual_disease.py "sickle cell anemia"
python scripts/search_individual_disease.py "hemophilia a"
python scripts/search_individual_disease.py "multiple myeloma"
```

---

## 2. 🫘 Nephrology Expanded (36 diseases)

### Categories
- **CKD Stages** (7): Stages 1-5, ESRD
- **Glomerular Diseases** (7): IgA nephropathy, Membranous, FSGS, Minimal change
- **Tubular Disorders** (8): ATN, Fanconi, RTA types, Bartter, Gitelman
- **Other Kidney Diseases** (14): PKD, Diabetic nephropathy, Lupus nephritis, Alport

### Key Datasets
- MIMIC-IV Nephrology
- UK Biobank Kidney Function
- USRDS (US Renal Data System)
- KDIGO Registry

### Search Examples
```bash
python scripts/search_individual_disease.py "chronic kidney disease stage 3"
python scripts/search_individual_disease.py "iga nephropathy"
python scripts/search_individual_disease.py "polycystic kidney disease"
```

---

## 3. 🫀 Hepatology Expanded (34 diseases)

### Categories
- **Viral Hepatitis** (7): Hepatitis A, B, C, D, E (acute/chronic)
- **Cirrhosis** (6): Alcoholic, Cryptogenic, Primary/Secondary biliary, Liver failure
- **Fatty Liver** (4): NAFLD, NASH, Alcoholic fatty liver
- **Autoimmune** (4): Autoimmune hepatitis, PBC, PSC
- **Metabolic** (7): Hemochromatosis, Wilson, Alpha-1 antitrypsin, Gilbert
- **Other** (6): Budd-Chiari, Portal hypertension, Hepatorenal syndrome

### Key Datasets
- MIMIC-IV Hepatology
- UK Biobank Liver Function
- TCGA-LIHC (Liver Cancer)
- NASH CRN

### Search Examples
```bash
python scripts/search_individual_disease.py "hepatitis c chronic"
python scripts/search_individual_disease.py "non alcoholic fatty liver"
python scripts/search_individual_disease.py "primary biliary cholangitis"
```

---

## 4. 🦴 Rheumatology Expanded (40 diseases)

### Categories
- **Inflammatory Arthritis** (10): RA variants, Psoriatic arthritis, Ankylosing spondylitis
- **Crystal Arthropathies** (5): Gout variants, Pseudogout, CPPD
- **Connective Tissue** (8): SLE variants, Scleroderma, MCTD, Sjögren's, Myositis
- **Vasculitis** (9): Giant cell arteritis, Takayasu, GPA, Kawasaki, Behçet
- **Other** (8): Polymyalgia rheumatica, Fibromyalgia, Osteoarthritis

### Key Datasets
- UK Biobank Rheumatology
- CORRONA Registry
- BRASS (Brigham RA Sequential Study)
- SLICC (Lupus Cohort)

### Search Examples
```bash
python scripts/search_individual_disease.py "rheumatoid arthritis severe"
python scripts/search_individual_disease.py "systemic lupus erythematosus"
python scripts/search_individual_disease.py "giant cell arteritis"
```

---

## 5. 🧬 Endocrinology Expanded (38 diseases)

### Categories
- **Diabetes** (8): Type 1/2 variants, Gestational, MODY, Neonatal
- **Thyroid** (10): Hypo/hyperthyroidism, Graves, Hashimoto, Thyroid nodules
- **Adrenal** (7): Addison, Cushing variants, Aldosteronism, Pheochromocytoma
- **Pituitary** (9): Acromegaly, Prolactinoma, GH deficiency, Diabetes insipidus
- **Parathyroid** (4): Hyperparathyroidism, Hypoparathyroidism, Osteoporosis

### Key Datasets
- UK Biobank Endocrine
- DCCT/EDIC (Diabetes)
- ACCORD, UKPDS
- NHANES

### Search Examples
```bash
python scripts/search_individual_disease.py "diabetes type 2 advanced"
python scripts/search_individual_disease.py "graves disease"
python scripts/search_individual_disease.py "cushing syndrome"
```

---

## 6. 🦠 Infectious Diseases Expanded (47 diseases)

### Categories
- **Bacterial** (16): TB variants, Lyme disease, Syphilis, STIs
- **Viral** (16): HIV/AIDS, Hepatitis, Herpes viruses, Measles, Dengue, Zika
- **Fungal** (9): Candidiasis, Aspergillosis, Cryptococcosis, PCP
- **Parasitic** (6): Malaria, Toxoplasmosis, Giardiasis

### Key Datasets
- MIMIC-IV Infectious Disease
- WHO TB Database
- HIV-CAUSAL Collaboration
- GISAID (Viral sequences)

### Search Examples
```bash
python scripts/search_individual_disease.py "tuberculosis pulmonary"
python scripts/search_individual_disease.py "hiv chronic"
python scripts/search_individual_disease.py "malaria falciparum"
```

---

## 7. 🫃 Gastroenterology Expanded (42 diseases)

### Categories
- **Esophageal** (8): GERD, Barrett's, Eosinophilic esophagitis, Achalasia
- **Stomach** (7): Gastritis, Peptic ulcer, H. pylori, Gastroparesis
- **IBD** (7): Crohn's variants, Ulcerative colitis variants
- **Functional** (4): IBS variants, Functional dyspepsia
- **Small Intestine** (6): Celiac, SIBO, Lactose intolerance
- **Colon** (7): Diverticulitis, Polyps, Ischemic colitis
- **Pancreas** (3): Pancreatitis acute/chronic, Pancreatic insufficiency

### Key Datasets
- MIMIC-IV Gastroenterology
- UK Biobank GI
- SPARC IBD
- NIDDK IBD Genetics

### Search Examples
```bash
python scripts/search_individual_disease.py "crohn disease ileal"
python scripts/search_individual_disease.py "ulcerative colitis pancolitis"
python scripts/search_individual_disease.py "celiac disease"
```

---

## 8. 👶 Pediatrics Expanded (39 diseases)

### Categories
- **Congenital** (7): Down, Turner, Klinefelter, Fragile X, Prader-Willi
- **Developmental** (7): Autism, ADHD, Cerebral palsy, Intellectual disability
- **Metabolic** (8): PKU, MSUD, Galactosemia, Gaucher, Tay-Sachs
- **Respiratory** (6): Bronchiolitis, Croup, RSV, CF
- **Infectious** (5): Kawasaki, Scarlet fever, Fifth disease
- **Other** (6): Failure to thrive, Pyloric stenosis, Intussusception

### Key Datasets
- PEDSnet
- MIMIC-IV Pediatrics
- UK Biobank Birth Cohort
- SPARK (Autism)

### Search Examples
```bash
python scripts/search_individual_disease.py "autism spectrum disorder"
python scripts/search_individual_disease.py "cerebral palsy spastic"
python scripts/search_individual_disease.py "phenylketonuria"
```

---

## 9. 👴 Geriatrics (29 diseases)

### Categories
- **Cognitive** (9): Alzheimer's variants, Vascular dementia, Lewy body, Delirium
- **Mobility** (6): Sarcopenia, Frailty, Falls, Gait disorders
- **Sensory** (4): Presbycusis, Presbyopia, AMD
- **Urinary** (4): Incontinence variants, BPH
- **Other** (6): Pressure ulcers, Polypharmacy, Malnutrition

### Key Datasets
- UK Biobank Aging
- ADNI (Alzheimer's)
- NACC (Alzheimer's Centers)
- Health ABC Study

### Search Examples
```bash
python scripts/search_individual_disease.py "alzheimer disease moderate"
python scripts/search_individual_disease.py "frailty syndrome"
python scripts/search_individual_disease.py "age related macular degeneration"
```

---

## 10. 🚑 Emergency Medicine (34 diseases)

### Categories
- **Trauma** (12): TBI, Spinal cord injury, Pneumothorax, Organ injuries
- **Shock** (5): Hypovolemic, Cardiogenic, Septic, Anaphylactic, Neurogenic
- **Acute Events** (6): ACS, Stroke, PE, Aortic dissection
- **Toxicology** (7): Overdoses (acetaminophen, opioid, etc.), Poisoning
- **Environmental** (4): Hypothermia, Heat stroke, Frostbite

### Key Datasets
- MIMIC-IV Emergency Department
- NEMSIS (EMS)
- NTDB (Trauma)
- Toxicology Data Network

### Search Examples
```bash
python scripts/search_individual_disease.py "traumatic brain injury severe"
python scripts/search_individual_disease.py "septic shock"
python scripts/search_individual_disease.py "opioid overdose"
```

---

## 11. 😴 Sleep Medicine (25 diseases)

### Categories
- **Sleep Apnea** (5): OSA variants, Central, Complex
- **Insomnia** (2): Acute, Chronic
- **Hypersomnias** (3): Narcolepsy, Idiopathic hypersomnia
- **Movement** (2): RLS, PLMD
- **Circadian** (5): Delayed/Advanced phase, Shift work, Jet lag
- **Parasomnias** (5): Sleepwalking, Sleep terrors, REM behavior disorder
- **Other** (3): Sleep-related hypoventilation, Bruxism

### Key Datasets
- Sleep Heart Health Study
- SHHS (Sleep Health Study)
- Wisconsin Sleep Cohort
- NSRR (National Sleep Research Resource)

### Search Examples
```bash
python scripts/search_individual_disease.py "obstructive sleep apnea severe"
python scripts/search_individual_disease.py "narcolepsy type 1"
python scripts/search_individual_disease.py "restless legs syndrome"
```

---

## 12. 🤧 Allergy & Immunology (29 diseases)

### Categories
- **Allergic** (8): Rhinitis, Conjunctivitis, Atopic dermatitis, Contact dermatitis
- **Food Allergies** (8): Peanut, Tree nut, Milk, Egg, Wheat, Soy, Fish, Shellfish
- **Drug Allergies** (3): Penicillin, Sulfa, NSAID
- **Immunodeficiencies** (7): CVID, IgA deficiency, SCID, CGD, Wiskott-Aldrich
- **Other** (3): Mastocytosis, Hereditary angioedema, EoE

### Key Datasets
- UK Biobank Allergy
- CAMP Study (Asthma)
- CoFAR (Food Allergy)
- USIDNET (Immunodeficiency)

### Search Examples
```bash
python scripts/search_individual_disease.py "peanut allergy"
python scripts/search_individual_disease.py "common variable immunodeficiency"
python scripts/search_individual_disease.py "hereditary angioedema"
```

---

## 13. 😣 Pain Medicine (27 diseases)

### Categories
- **Neuropathic** (7): Diabetic neuropathy, PHN, Trigeminal neuralgia, CRPS
- **Musculoskeletal** (5): Chronic back/neck pain, Myofascial pain, TMJ
- **Headache** (5): Chronic migraine, Tension headache, Cluster headache
- **Visceral** (4): Chronic abdominal/pelvic pain, Interstitial cystitis
- **Other** (6): Fibromyalgia, Central sensitization, Cancer pain

### Key Datasets
- UK Biobank Pain
- OPPERA (Orofacial Pain)
- MAPP Network (Pelvic Pain)
- PainOmics

### Search Examples
```bash
python scripts/search_individual_disease.py "complex regional pain syndrome"
python scripts/search_individual_disease.py "chronic migraine"
python scripts/search_individual_disease.py "fibromyalgia syndrome"
```

---

## 14. ⚽ Sports Medicine (24 diseases)

### Categories
- **Overuse** (9): Tendinopathies (rotator cuff, tennis elbow, Achilles, etc.)
- **Acute Injuries** (12): Ligament tears (ACL, PCL, MCL), Meniscus tears, Ankle sprains
- **Concussions** (3): Grades 1, 2, 3

### Key Datasets
- NCAA Injury Surveillance
- NFL Concussion Database
- MOON Cohort (Knee injuries)
- MARS Cohort (Shoulder)

### Search Examples
```bash
python scripts/search_individual_disease.py "anterior cruciate ligament tear"
python scripts/search_individual_disease.py "concussion grade 2"
python scripts/search_individual_disease.py "achilles tendinopathy"
```

---

## 15. 👷 Occupational Medicine (22 diseases)

### Categories
- **Respiratory** (7): Asbestosis, Silicosis, Coal worker's pneumoconiosis, Occupational asthma
- **Musculoskeletal** (4): Carpal tunnel, RSI, Vibration injury, Low back pain
- **Dermatologic** (2): Contact dermatitis, Urticaria
- **Toxic** (5): Lead, Mercury, Arsenic, Pesticide poisoning
- **Other** (4): Hearing loss, Radiation exposure, Heat stress, Shift work disorder

### Key Datasets
- NIOSH Surveillance
- SENSOR (Occupational Disease)
- OSHA Injury Database
- WorkSafeBC

### Search Examples
```bash
python scripts/search_individual_disease.py "carpal tunnel syndrome occupational"
python scripts/search_individual_disease.py "silicosis"
python scripts/search_individual_disease.py "noise induced hearing loss"
```

---

## 🔍 Quick Search Commands

### By Specialty
```bash
# List all diseases in a specialty
python scripts/list_datasets_by_condition.py "hematology"
python scripts/list_datasets_by_condition.py "nephrology"
python scripts/list_datasets_by_condition.py "sleep_medicine"
```

### By Disease Name
```bash
# Search for specific disease
python scripts/search_individual_disease.py "disease_name"
```

### Advanced Search
```bash
# Search with filters
python scripts/advanced_disease_search.py --category "specialty" --severity "level"
```

---

## 📊 Statistics Summary

| Specialty | Diseases | Key Focus |
|-----------|----------|-----------|
| Hematology | 46 | Blood disorders, cancers |
| Nephrology | 36 | Kidney diseases |
| Hepatology | 34 | Liver diseases |
| Rheumatology | 40 | Arthritis, autoimmune |
| Endocrinology | 38 | Hormonal disorders |
| Infectious Diseases | 47 | Infections |
| Gastroenterology | 42 | GI disorders |
| Pediatrics | 39 | Childhood diseases |
| Geriatrics | 29 | Age-related diseases |
| Emergency Medicine | 34 | Trauma, acute events |
| Sleep Medicine | 25 | Sleep disorders |
| Allergy & Immunology | 29 | Allergies, immunodeficiency |
| Pain Medicine | 27 | Chronic pain |
| Sports Medicine | 24 | Sports injuries |
| Occupational Medicine | 22 | Work-related diseases |
| **TOTAL** | **512** | **15 specialties** |

---

## 🎯 Common Use Cases

### Clinical Research
- Disease cohort identification
- Comparative effectiveness studies
- Biomarker discovery
- Clinical trial recruitment

### AI/ML Development
- Disease prediction models
- Diagnostic assistance
- Treatment recommendations
- Prognosis prediction

### Healthcare Analytics
- Population health management
- Disease surveillance
- Quality metrics
- Cost analysis

### Medical Education
- Case-based learning
- Differential diagnosis
- Clinical decision support

---

*Last Updated: November 9, 2025*
*Version: 4.0 (Super Expansion)*
