# Individual Disease Search Guide

## Overview

We've created a comprehensive system where **every single disease** (607 individual diseases) can be searched and queried individually with complete details.

---

## 🎯 What's Available

### 607 Individual Diseases
Each disease has:
- ✅ Unique ID
- ✅ Full name
- ✅ Category classification
- ✅ Parent disease (if applicable)
- ✅ Clinical information (where available)
- ✅ Available datasets
- ✅ Sample counts
- ✅ Modalities
- ✅ Search terms

### Generated Files
- **JSON Database**: `data/disease_database.json` (607 diseases)
- **Markdown Files**: `docs/diseases/` (607 individual files)
- **Index**: `docs/diseases/INDEX.md`

---

## 🔍 How to Search Individual Diseases

### Method 1: Command Line Search
```bash
# Search for any disease by name
python scripts/search_individual_disease.py "nodular melanoma"
python scripts/search_individual_disease.py "triple negative"
python scripts/search_individual_disease.py "glioblastoma"
python scripts/search_individual_disease.py "atrial fibrillation"
python scripts/search_individual_disease.py "STEMI"
python scripts/search_individual_disease.py "pneumococcal"

# List all searchable diseases
python scripts/search_individual_disease.py --list-all
```

### Method 2: Browse Markdown Files
```bash
# View index of all diseases
cat docs/diseases/INDEX.md

# View specific disease
cat docs/diseases/disease_0001.md
cat docs/diseases/disease_0100.md
```

### Method 3: Query JSON Database
```python
import json

# Load database
with open('data/disease_database.json') as f:
    diseases = json.load(f)

# Search for specific disease
for disease_id, info in diseases.items():
    if 'melanoma' in info['name'].lower():
        print(f"{info['name']}: {info.get('clinical', {})}")
```

---

## 📋 Disease Categories

### 🫁 Respiratory Diseases (100+ individual diseases)
```
Pneumonia Types:
├─ Streptococcus pneumoniae (Pneumococcal)
├─ Staphylococcus aureus
├─ Haemophilus influenzae
├─ Mycoplasma pneumoniae (Atypical)
├─ Legionella pneumophila (Legionnaires')
├─ Klebsiella pneumoniae
├─ Pseudomonas aeruginosa
├─ COVID-19 (SARS-CoV-2)
├─ Influenza A/B
├─ RSV
└─ ... 90+ more

Tuberculosis Types:
├─ Primary TB
├─ Secondary TB (Reactivation)
├─ Miliary TB
├─ Cavitary TB
├─ Lymph Node TB
├─ Pleural TB
├─ MDR-TB
├─ XDR-TB
└─ ... more

Lung Cancer Types:
├─ Acinar Adenocarcinoma
├─ Papillary Adenocarcinoma
├─ Micropapillary Adenocarcinoma
├─ Solid Adenocarcinoma
├─ Lepidic Adenocarcinoma
├─ Keratinizing Squamous Cell
├─ Non-keratinizing Squamous Cell
├─ Basaloid Squamous Cell
└─ ... more
```

### 🧬 Cancer (200+ individual diseases)
```
Breast Cancer:
├─ Invasive Ductal Carcinoma (IDC)
├─ Invasive Lobular Carcinoma (ILC)
├─ Tubular Carcinoma
├─ Medullary Carcinoma
├─ Mucinous Carcinoma
├─ Papillary Carcinoma
├─ DCIS (Ductal Carcinoma In Situ)
├─ LCIS (Lobular Carcinoma In Situ)
├─ Luminal A
├─ Luminal B
├─ HER2-Enriched
├─ Triple Negative
├─ Inflammatory Breast Cancer
└─ Paget's Disease

Melanoma:
├─ Superficial Spreading Melanoma
├─ Nodular Melanoma
├─ Lentigo Maligna Melanoma
├─ Acral Lentiginous Melanoma
├─ Amelanotic Melanoma
└─ Desmoplastic Melanoma

Basal Cell Carcinoma:
├─ Nodular BCC
├─ Superficial BCC
├─ Morpheaform (Sclerosing) BCC
├─ Pigmented BCC
└─ Infiltrative BCC

Brain Tumors:
├─ Glioblastoma (Grade IV)
├─ Anaplastic Astrocytoma (Grade III)
├─ Diffuse Astrocytoma (Grade II)
├─ Pilocytic Astrocytoma (Grade I)
├─ Oligodendroglioma
├─ Ependymoma
├─ Meningioma Grade I
├─ Meningioma Grade II
├─ Meningioma Grade III
└─ ... more
```

### 🧠 Neurological (150+ individual diseases)
```
Alzheimer's Stages:
├─ Preclinical Alzheimer's
├─ Mild Cognitive Impairment (MCI)
├─ Mild Alzheimer's Dementia
├─ Moderate Alzheimer's Dementia
└─ Severe Alzheimer's Dementia

Parkinson's Types:
├─ Tremor-dominant
├─ Postural Instability/Gait Difficulty (PIGD)
├─ Mixed
├─ Multiple System Atrophy (MSA)
├─ Progressive Supranuclear Palsy (PSP)
├─ Corticobasal Degeneration
└─ Lewy Body Dementia

Stroke Types:
├─ Thrombotic Stroke
├─ Embolic Stroke
├─ Lacunar Stroke
├─ Cryptogenic Stroke
├─ Intracerebral Hemorrhage
├─ Subarachnoid Hemorrhage
├─ Subdural Hematoma
└─ Epidural Hematoma

Epilepsy Types:
├─ Temporal Lobe Epilepsy
├─ Frontal Lobe Epilepsy
├─ Parietal Lobe Epilepsy
├─ Occipital Lobe Epilepsy
├─ Absence Seizures
├─ Tonic-Clonic Seizures
├─ Myoclonic Seizures
├─ Atonic Seizures
└─ ... more
```

### 🫀 Cardiovascular (100+ individual diseases)
```
Arrhythmias:
├─ Atrial Fibrillation (AFib)
├─ Atrial Flutter
├─ Supraventricular Tachycardia (SVT)
├─ Wolff-Parkinson-White Syndrome
├─ AV Nodal Reentrant Tachycardia
├─ Ventricular Tachycardia (VT)
├─ Ventricular Fibrillation (VFib)
├─ Premature Ventricular Contractions (PVCs)
├─ Long QT Syndrome
├─ Brugada Syndrome
├─ Sinus Bradycardia
├─ First-degree AV Block
├─ Second-degree AV Block (Mobitz I)
├─ Second-degree AV Block (Mobitz II)
├─ Third-degree AV Block
└─ Sick Sinus Syndrome

Myocardial Infarction:
├─ STEMI (ST-Elevation MI)
├─ NSTEMI (Non-ST-Elevation MI)
├─ Anterior MI
├─ Inferior MI
├─ Lateral MI
└─ Posterior MI

Heart Failure:
├─ HFrEF (Reduced EF <40%)
├─ HFmrEF (Mid-range EF 40-49%)
├─ HFpEF (Preserved EF ≥50%)
├─ Left-sided Heart Failure
├─ Right-sided Heart Failure
└─ Biventricular Failure
```

---

## 💡 Example Searches

### Example 1: Search for Nodular Melanoma
```bash
$ python scripts/search_individual_disease.py "nodular melanoma"

================================================================================
DISEASE: NODULAR MELANOMA
================================================================================

📋 BASIC INFORMATION
   Name: Nodular Melanoma
   Category: cancer
   Parent: skin_cancer
   Type: subtype

📝 CLINICAL NOTES
   • Second most common melanoma (15%)
   • Most aggressive melanoma type
   • Vertical growth from onset
   • Rapid progression, poor prognosis if not caught early

💾 AVAILABLE DATASETS
   Datasets: ISIC Archive, HAM10000
   Samples: 5,000+ dermoscopy images
   Modalities: Dermoscopy
```

### Example 2: Search for Triple Negative Breast Cancer
```bash
$ python scripts/search_individual_disease.py "triple negative"

================================================================================
DISEASE: TRIPLE NEGATIVE
================================================================================

📋 BASIC INFORMATION
   Name: Triple Negative
   Category: breast_cancer
   Type: molecular_subtype

📝 CLINICAL NOTES
   • ER-, PR-, HER2- breast cancer (15%)
   • Most aggressive breast cancer subtype
   • Limited targeted therapy options
   • Higher recurrence rate
   • More common in younger women and BRCA1 carriers

💾 AVAILABLE DATASETS
   Datasets: TCGA-BRCA, METABRIC
   Samples: 800+ cases
   Modalities: Genomics, Histopathology
```

### Example 3: Search for Glioblastoma
```bash
$ python scripts/search_individual_disease.py "glioblastoma"

================================================================================
DISEASE: GLIOBLASTOMA
================================================================================

📋 BASIC INFORMATION
   Name: Glioblastoma (Grade IV)
   Category: brain_tumors
   Type: glioma

📝 CLINICAL NOTES
   • Most aggressive brain tumor (Grade IV)
   • Median survival: 15 months
   • Highly infiltrative, difficult to remove completely
   • Standard treatment: Surgery + radiation + chemotherapy

💾 AVAILABLE DATASETS
   Datasets: BraTS, TCGA-GBM
   Samples: 1,000+ MRI cases
   Modalities: MRI (T1, T1ce, T2, FLAIR), Genomics
```

---

## 📊 Statistics

### Total Coverage
- **607 Individual Diseases** cataloged
- **15 Major Categories**
- **100+ Respiratory diseases**
- **200+ Cancer subtypes**
- **150+ Neurological diseases**
- **100+ Cardiovascular diseases**
- **50+ Other diseases**

### Files Generated
- **1 JSON Database**: Complete searchable database
- **607 Markdown Files**: One per disease
- **1 Index File**: Master index of all diseases

---

## 🎯 Use Cases

### 1. Medical Research
```bash
# Find all datasets for specific melanoma type
python scripts/search_individual_disease.py "superficial spreading melanoma"

# Compare different breast cancer subtypes
python scripts/search_individual_disease.py "luminal a"
python scripts/search_individual_disease.py "luminal b"
python scripts/search_individual_disease.py "her2 enriched"
```

### 2. AI Model Training
```bash
# Find training data for specific arrhythmia
python scripts/search_individual_disease.py "ventricular tachycardia"

# Get datasets for specific pneumonia type
python scripts/search_individual_disease.py "pneumococcal"
```

### 3. Clinical Decision Support
```bash
# Look up specific stroke type
python scripts/search_individual_disease.py "lacunar stroke"

# Find information on specific heart failure type
python scripts/search_individual_disease.py "hfref"
```

### 4. Medical Education
```bash
# Study specific disease variants
python scripts/search_individual_disease.py "lentigo maligna melanoma"
python scripts/search_individual_disease.py "acral lentiginous melanoma"
```

---

## 🔧 API Integration

### REST API Endpoints
```bash
# Search by individual disease
curl "http://localhost:8000/disease/nodular_melanoma"

# Get disease details
curl "http://localhost:8000/disease/triple_negative/details"

# Find similar diseases
curl "http://localhost:8000/disease/glioblastoma/similar"

# Get datasets for disease
curl "http://localhost:8000/disease/atrial_fibrillation/datasets"
```

---

## 📚 Documentation Structure

```
medical-vectordb/
├── data/
│   └── disease_database.json          # Complete JSON database (607 diseases)
├── docs/
│   └── diseases/
│       ├── INDEX.md                   # Master index
│       ├── disease_0001.md            # Streptococcus pneumoniae
│       ├── disease_0002.md            # Staphylococcus aureus
│       ├── ...
│       └── disease_0607.md            # Last disease
├── scripts/
│   ├── search_individual_disease.py   # Search tool
│   └── generate_disease_database.py   # Database generator
└── config/
    ├── disease_taxonomy.yaml          # Disease hierarchy
    └── disease_to_dataset_mapping.yaml # Disease → Dataset mapping
```

---

## 🚀 Quick Start

```bash
# 1. Generate disease database (already done)
python scripts/generate_disease_database.py

# 2. Search for any disease
python scripts/search_individual_disease.py "your disease name"

# 3. List all diseases
python scripts/search_individual_disease.py --list-all

# 4. Browse markdown files
ls docs/diseases/
cat docs/diseases/INDEX.md

# 5. Query JSON database
python -c "import json; print(json.load(open('data/disease_database.json'))['disease_0001'])"
```

---

## 💡 Advanced Features

### Fuzzy Search
The system supports fuzzy matching:
```bash
# These all work:
python scripts/search_individual_disease.py "melanoma"
python scripts/search_individual_disease.py "nodular"
python scripts/search_individual_disease.py "nodular melanoma"
```

### Multiple Matches
If multiple diseases match, you'll see a list:
```bash
$ python scripts/search_individual_disease.py "melanoma"

Multiple matches found:
1. Superficial Spreading Melanoma
2. Nodular Melanoma
3. Lentigo Maligna Melanoma
4. Acral Lentiginous Melanoma
5. Amelanotic Melanoma
6. Desmoplastic Melanoma

Please be more specific.
```

### Category Filtering
```bash
# Filter by category
python scripts/search_individual_disease.py "melanoma" --category cancer
```

---

## 🎓 Summary

We've created a **complete individual disease search system** with:

✅ **607 Individual Diseases** - Every disease searchable
✅ **JSON Database** - Programmatic access
✅ **607 Markdown Files** - Human-readable documentation
✅ **Search Tool** - Command-line interface
✅ **Clinical Information** - Where available
✅ **Dataset Mapping** - Direct links to data
✅ **Fuzzy Matching** - Flexible search
✅ **Category Organization** - Hierarchical structure

**Every disease is now individually searchable and documented! 🎯**

---

For more information, see:
- `DISEASE_CLASSIFICATION.md` - Complete disease taxonomy
- `FINAL_SUMMARY.md` - System overview
- `docs/diseases/INDEX.md` - Disease index
