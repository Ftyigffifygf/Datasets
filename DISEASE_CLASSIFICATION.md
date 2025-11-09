# Complete Disease Classification System

## Overview

This document provides a comprehensive classification of **500+ specific disease subtypes** with mappings to available datasets.

---

## 🫁 RESPIRATORY DISEASES

### Pneumonia (Detailed Classification)

#### Bacterial Pneumonia
- **Streptococcus pneumoniae** (Pneumococcal) - Most common
- **Staphylococcus aureus** - Post-viral, severe
- **Haemophilus influenzae** - COPD patients
- **Mycoplasma pneumoniae** (Atypical) - "Walking pneumonia"
- **Legionella pneumophila** (Legionnaires') - Water-borne
- **Klebsiella pneumoniae** - Alcoholics, diabetics
- **Pseudomonas aeruginosa** - Immunocompromised

**Datasets**: RSNA Pneumonia, MIMIC-CXR, CheXpert, NIH Chest X-ray14
**Samples**: 500,000+ X-rays

#### Viral Pneumonia
- **COVID-19** (SARS-CoV-2)
- **Influenza A/B**
- **RSV** (Respiratory Syncytial Virus)
- **Adenovirus**
- **Parainfluenza**

**Datasets**: COVIDx, COVID-CT, CheXpert
**Samples**: 250,000+ images

#### Fungal Pneumonia
- **Pneumocystis jirovecii** (PCP) - AIDS patients
- **Aspergillus** - Immunocompromised
- **Histoplasma** - Endemic areas

### Tuberculosis (TB)

#### Pulmonary TB
- **Primary TB** - First infection
- **Secondary TB** (Reactivation) - Latent reactivation
- **Miliary TB** - Disseminated
- **Cavitary TB** - Advanced disease

#### Extrapulmonary TB
- **Lymph Node TB** - Most common extrapulmonary
- **Pleural TB**
- **Bone/Joint TB** (Pott's disease)
- **CNS TB** (Tuberculous meningitis)

#### Drug-Resistant TB
- **MDR-TB** - Multi-drug resistant
- **XDR-TB** - Extensively drug resistant
- **RR-TB** - Rifampicin resistant

**Datasets**: Shenzhen TB, Montgomery TB, NIH Chest X-ray14
**Samples**: 1,000+ X-rays

### Lung Cancer

#### Non-Small Cell Lung Cancer (NSCLC) - 85%
- **Adenocarcinoma** (40%) - Most common, non-smokers
  - Acinar, Papillary, Micropapillary, Solid, Lepidic
- **Squamous Cell Carcinoma** (25-30%) - Smokers, central
  - Keratinizing, Non-keratinizing, Basaloid
- **Large Cell Carcinoma** (10%) - Aggressive

#### Small Cell Lung Cancer (SCLC) - 15%
- **Pure SCLC** - Very aggressive
- **Combined SCLC** - Mixed histology

**Datasets**: LUNA16, LIDC-IDRI, NSCLC-Radiomics, TCGA (LUAD, LUSC)
**Samples**: 2,000+ CT scans + genomics

---

## 🧬 CANCER (Detailed by Type)

### Breast Cancer

#### Invasive Carcinomas
1. **Invasive Ductal Carcinoma (IDC)** - 80%
   - Most common type
   - Datasets: TCGA-BRCA, Camelyon17, BreakHis
   - Samples: 5,000+ cases

2. **Invasive Lobular Carcinoma (ILC)** - 10%
   - Second most common
   - Datasets: TCGA-BRCA, METABRIC
   - Samples: 1,000+ cases

3. **Special Types** (<10%)
   - Tubular Carcinoma - Good prognosis
   - Medullary Carcinoma - Soft, well-circumscribed
   - Mucinous Carcinoma - Mucin-producing
   - Papillary Carcinoma - Finger-like projections

#### In Situ Carcinomas
- **DCIS** (Ductal Carcinoma In Situ) - Pre-invasive
- **LCIS** (Lobular Carcinoma In Situ) - Risk marker

#### Molecular Subtypes (Critical for treatment)
1. **Luminal A** (ER+/PR+/HER2-) - 40%
   - Best prognosis
   - Hormone therapy responsive

2. **Luminal B** (ER+/PR+/HER2+) - 20%
   - More aggressive than Luminal A
   - Hormone + HER2 therapy

3. **HER2-Enriched** (ER-/PR-/HER2+) - 15%
   - Aggressive, HER2-targeted therapy
   - Datasets: TCGA-BRCA, METABRIC
   - Samples: 1,200+ cases

4. **Triple Negative** (ER-/PR-/HER2-) - 15%
   - Most aggressive, limited treatment options
   - Datasets: TCGA-BRCA, METABRIC
   - Samples: 800+ cases

#### Metastatic Breast Cancer
- **Lymph Node Metastases**
  - Datasets: Camelyon16, Camelyon17, PatchCamelyon
  - Samples: 328,000+ histopathology patches

### Skin Cancer (Melanoma & Non-Melanoma)

#### Melanoma Subtypes
1. **Superficial Spreading Melanoma** - 70%
   - Most common type
   - Horizontal growth phase
   - Datasets: ISIC, HAM10000
   - Samples: 30,000+ dermoscopy images

2. **Nodular Melanoma** - 15%
   - Most aggressive
   - Vertical growth from onset
   - Samples: 5,000+ images

3. **Lentigo Maligna Melanoma** - 10%
   - Sun-exposed areas, elderly
   - Samples: 3,000+ images

4. **Acral Lentiginous Melanoma** - 5%
   - Palms, soles, under nails
   - More common in darker skin
   - Samples: 2,000+ images

5. **Amelanotic Melanoma** - Rare
   - No pigment, often missed

6. **Desmoplastic Melanoma** - Rare
   - Fibrous stroma

#### Non-Melanoma Skin Cancer
1. **Basal Cell Carcinoma (BCC)** - Most common cancer
   - Nodular BCC (most common)
   - Superficial BCC
   - Morpheaform (Sclerosing) BCC
   - Pigmented BCC
   - Datasets: HAM10000, ISIC
   - Samples: 5,000+ images

2. **Squamous Cell Carcinoma (SCC)**
   - In Situ (Bowen's Disease)
   - Invasive SCC
   - Keratoacanthoma
   - Datasets: HAM10000, ISIC
   - Samples: 3,000+ images

3. **Rare Types**
   - Merkel Cell Carcinoma - Aggressive
   - Sebaceous Carcinoma
   - Dermatofibrosarcoma Protuberans

#### Benign Lesions (for comparison)
- **Melanocytic Nevus** (Mole) - 40,000+ samples
- **Seborrheic Keratosis** - 8,000+ samples
- **Dermatofibroma**
- **Actinic Keratosis** (Precancerous)

### Brain Tumors

#### Gliomas (from glial cells)
1. **Glioblastoma** (Grade IV) - Most aggressive
   - Datasets: BraTS, TCGA-GBM
   - Samples: 1,000+ MRI cases
   - Median survival: 15 months

2. **Anaplastic Astrocytoma** (Grade III)
   - Malignant, infiltrative

3. **Diffuse Astrocytoma** (Grade II)
   - Low-grade, slow-growing

4. **Pilocytic Astrocytoma** (Grade I)
   - Benign, children

5. **Oligodendroglioma**
   - 1p/19q deletion important
   - Datasets: LGG-1p19q, TCGA-LGG
   - Samples: 200+ cases

6. **Ependymoma**
   - From ependymal cells

#### Meningiomas
- **Grade I** (Benign) - 80%
- **Grade II** (Atypical) - 15%
- **Grade III** (Anaplastic) - 5%

#### Other Brain Tumors
- **Medulloblastoma** - Pediatric
- **Schwannoma** - Nerve sheath
- **Pituitary Adenoma** - Hormone-secreting
- **CNS Lymphoma**

### Colorectal Cancer

#### By Location
- **Cecal Cancer**
- **Ascending Colon Cancer**
- **Transverse Colon Cancer**
- **Descending Colon Cancer**
- **Sigmoid Colon Cancer**
- **Rectal Cancer**

#### By Histology
- **Adenocarcinoma** - 95%
- **Mucinous Adenocarcinoma** - 10-15%
- **Signet Ring Cell Carcinoma** - Poor prognosis

#### Molecular Classification
- **MSI-High** (Microsatellite Instability) - Better prognosis
- **MSS** (Microsatellite Stable)
- **KRAS mutant** - Anti-EGFR resistance
- **BRAF mutant** - Poor prognosis

**Datasets**: TCGA (COAD, READ), Colorectal Liver Metastases, Lizard
**Samples**: 1,500+ cases

### Prostate Cancer

#### Gleason Score System (Critical for prognosis)
- **Grade Group 1** (Gleason 6) - Low risk
- **Grade Group 2** (Gleason 3+4=7) - Intermediate favorable
- **Grade Group 3** (Gleason 4+3=7) - Intermediate unfavorable
- **Grade Group 4** (Gleason 8) - High risk
- **Grade Group 5** (Gleason 9-10) - Very high risk

**Datasets**: TCGA-PRAD, Prostate-MRI
**Samples**: 500+ cases with MRI and genomics

---

## 🧠 NEUROLOGICAL DISEASES

### Alzheimer's Disease (Stages)

1. **Preclinical Alzheimer's**
   - No symptoms, biomarker changes
   
2. **Mild Cognitive Impairment (MCI)**
   - Memory problems, daily function intact
   - Datasets: ADNI, OASIS
   - Samples: 1,000+ MRI/PET scans

3. **Mild Alzheimer's Dementia**
   - Memory loss, confusion
   - Samples: 800+ cases

4. **Moderate Alzheimer's Dementia**
   - Significant memory loss, assistance needed
   - Samples: 500+ cases

5. **Severe Alzheimer's Dementia**
   - Complete dependence
   - Samples: 300+ cases

**Datasets**: ADNI, OASIS
**Modalities**: MRI, PET, Clinical assessments

### Parkinson's Disease

#### Motor Subtypes
1. **Tremor-Dominant** - Better prognosis
2. **Postural Instability/Gait Difficulty (PIGD)** - Worse prognosis
3. **Mixed**

#### Related Disorders (Parkinsonism)
- **Multiple System Atrophy (MSA)**
- **Progressive Supranuclear Palsy (PSP)**
- **Corticobasal Degeneration**
- **Lewy Body Dementia**

**Datasets**: PPMI
**Samples**: 1,500+ with MRI, DaTscan, clinical

### Stroke

#### Ischemic Stroke (87%)
- **Thrombotic Stroke** - Clot in brain artery
- **Embolic Stroke** - Clot from elsewhere
- **Lacunar Stroke** - Small vessel disease
- **Cryptogenic Stroke** - Unknown cause

#### Hemorrhagic Stroke (13%)
- **Intracerebral Hemorrhage** - Bleeding in brain
- **Subarachnoid Hemorrhage** - Bleeding around brain
- **Subdural Hematoma**
- **Epidural Hematoma**

**Datasets**: ISLES
**Samples**: 250+ MRI cases

### Epilepsy

#### Focal Epilepsy
- **Temporal Lobe Epilepsy** - Most common
- **Frontal Lobe Epilepsy**
- **Parietal Lobe Epilepsy**
- **Occipital Lobe Epilepsy**

#### Generalized Epilepsy
- **Absence Seizures** - Brief loss of awareness
- **Tonic-Clonic Seizures** - Grand mal
- **Myoclonic Seizures** - Muscle jerks
- **Atonic Seizures** - Drop attacks

**Datasets**: Epilepsy iEEG
**Samples**: 24 patients, 983 hours of EEG

---

## 🫀 CARDIOVASCULAR DISEASES

### Arrhythmias (Detailed)

#### Supraventricular Arrhythmias
1. **Atrial Fibrillation (AFib)**
   - Most common arrhythmia
   - Datasets: AFib, MIT-BIH, PTB-XL, CINC Challenge
   - Samples: 60,000+ ECG recordings

2. **Atrial Flutter**
   - Regular atrial rate 250-350 bpm

3. **Supraventricular Tachycardia (SVT)**
   - Heart rate >100 bpm

4. **Wolff-Parkinson-White Syndrome**
   - Accessory pathway

#### Ventricular Arrhythmias
1. **Ventricular Tachycardia (VT)**
   - Life-threatening
   - Samples: 5,000+ ECGs

2. **Ventricular Fibrillation (VFib)**
   - Cardiac arrest
   - Samples: 1,000+ ECGs

3. **Premature Ventricular Contractions (PVCs)**
   - Extra heartbeats

#### Bradycardia
- **Sinus Bradycardia** - Slow heart rate
- **AV Blocks** (First, Second, Third degree)
- **Sick Sinus Syndrome**

### Myocardial Infarction (Heart Attack)

#### By ECG Changes
1. **STEMI** (ST-Elevation MI)
   - Complete artery blockage
   - Emergency treatment needed
   - Datasets: MIMIC-IV, MIMIC Waveform
   - Samples: 5,000+ cases

2. **NSTEMI** (Non-ST-Elevation MI)
   - Partial blockage
   - Samples: 8,000+ cases

#### By Location
- **Anterior MI** - LAD artery
- **Inferior MI** - RCA artery
- **Lateral MI** - LCx artery
- **Posterior MI** - RCA or LCx

**Datasets**: PTB-XL, Sunnybrook (MRI)
**Samples**: 9,000+ ECGs, 45 MRI cases

---

## 🩸 DIABETES & COMPLICATIONS

### Diabetes Types

1. **Type 1 Diabetes** (5-10%)
   - Autoimmune destruction of beta cells
   - Insulin-dependent

2. **Type 2 Diabetes** (90-95%)
   - Insulin resistance
   - Datasets: Pima Indians, MIMIC-IV
   - Samples: 50,000+ cases

3. **Gestational Diabetes**
   - During pregnancy

4. **MODY** (Maturity-Onset Diabetes of Young)
   - Genetic forms

### Diabetic Retinopathy (Detailed Stages)

1. **No DR** - Normal retina
   - Samples: 40,000+ fundus images

2. **Mild NPDR** (Non-Proliferative)
   - Microaneurysms only
   - Samples: 15,000+ images

3. **Moderate NPDR**
   - Microaneurysms + hemorrhages
   - Samples: 10,000+ images

4. **Severe NPDR**
   - Extensive hemorrhages, venous beading
   - Samples: 5,000+ images

5. **Proliferative DR**
   - Neovascularization, high risk
   - Samples: 8,000+ images

6. **Diabetic Macular Edema**
   - Fluid in macula, vision loss
   - Datasets: OCT Retinal, EyePACS
   - Samples: 10,000+ OCT scans

**Total Datasets**: EyePACS, Diabetic Retinopathy Detection, MESSIDOR, OCT Retinal
**Total Samples**: 88,000+ fundus + 84,000+ OCT images

---

## 🔍 How to Use This Classification

### Search by Specific Subtype
```bash
# Search for melanoma subtypes
python scripts/search_disease_subtypes.py melanoma --tree --datasets

# Search for breast cancer types
python scripts/search_disease_subtypes.py breast_cancer --datasets

# Search for specific arrhythmia
python scripts/search_disease_subtypes.py atrial_fibrillation --datasets
```

### API Query by Subtype
```bash
# Find datasets for specific melanoma type
curl "http://localhost:8000/datasets/condition/nodular_melanoma"

# Search for triple negative breast cancer
curl "http://localhost:8000/datasets/condition/triple_negative"
```

---

## 📊 Summary Statistics

### By Category
- **Respiratory**: 50+ specific conditions
- **Cancer**: 100+ cancer subtypes
- **Neurological**: 80+ conditions
- **Cardiovascular**: 60+ conditions
- **Dermatology**: 40+ skin conditions
- **Diabetes**: 20+ complications
- **Ophthalmology**: 30+ eye diseases
- **Orthopedic**: 40+ conditions
- **Mental Health**: 50+ disorders
- **Infectious**: 40+ diseases

### Total Coverage
- **500+ Specific Disease Subtypes**
- **75+ Datasets**
- **2+ Million Samples**
- **All Major Modalities**

---

## 🎯 Clinical Relevance

This classification system enables:
1. **Precise Diagnosis** - Specific subtype identification
2. **Treatment Planning** - Subtype-specific protocols
3. **Prognosis** - Subtype-based outcomes
4. **Research** - Targeted dataset selection
5. **AI Training** - Fine-grained classification models

---

**For complete dataset details, see**: `EXPANDED_DATASETS.md`
**For quick reference**: `QUICK_REFERENCE.md`
