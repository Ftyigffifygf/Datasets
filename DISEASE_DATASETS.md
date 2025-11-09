# Disease-Specific Datasets Reference

Complete reference of all disease-specific datasets integrated into the vector database.

## 🫁 Respiratory Diseases

### NIH Chest X-ray14
- **Size**: 45 GB
- **Samples**: 112,120 images
- **Conditions**: 14 thoracic diseases
  - Atelectasis, Cardiomegaly, Effusion, Infiltration, Mass, Nodule, Pneumonia, Pneumothorax, Consolidation, Edema, Emphysema, Fibrosis, Pleural Thickening, Hernia
- **URL**: https://nihcc.app.box.com/v/ChestXray-NIHCC

### CheXpert
- **Size**: 439 GB
- **Samples**: 224,316 images
- **Conditions**: 5 conditions with uncertainty labels
  - Atelectasis, Cardiomegaly, Consolidation, Edema, Pleural Effusion
- **URL**: https://stanfordmlgroup.github.io/competitions/chexpert/

### COVIDx
- **Size**: 5 GB
- **Samples**: 30,000 images
- **Conditions**: COVID-19, Pneumonia, Normal
- **Modalities**: X-ray, CT
- **URL**: https://github.com/lindawangg/COVID-Net

### RSNA Pneumonia Detection
- **Size**: 10 GB
- **Samples**: 30,000 images
- **Conditions**: Pneumonia
- **URL**: https://www.kaggle.com/c/rsna-pneumonia-detection-challenge

## 🧠 Neurological Disorders

### BraTS (Brain Tumor Segmentation)
- **Size**: 100 GB
- **Samples**: 2,000 cases
- **Conditions**: Glioblastoma, Lower Grade Glioma
- **Sequences**: T1, T1ce, T2, FLAIR
- **URL**: https://www.med.upenn.edu/cbica/brats2023/

### OASIS (Alzheimer's)
- **Size**: 50 GB
- **Samples**: 1,000+ subjects
- **Conditions**: Alzheimer's Disease, Dementia
- **Type**: Longitudinal MRI
- **URL**: https://www.oasis-brains.org

### ADNI (Alzheimer's Disease Neuroimaging Initiative)
- **Size**: 200 GB
- **Samples**: 2,000+ subjects
- **Modalities**: MRI, PET, Clinical
- **Access**: Credentialed
- **URL**: https://adni.loni.usc.edu

## 🫀 Cardiovascular Diseases

### MIT-BIH Arrhythmia Database
- **Size**: 100 MB
- **Samples**: 48 recordings (48 hours)
- **Conditions**: Arrhythmia, Atrial Fibrillation, Ventricular Tachycardia
- **URL**: https://physionet.org/content/mitdb/

### MIMIC-III Waveform Database
- **Size**: 4 TB
- **Samples**: 67,000 recordings
- **Modalities**: ECG, ABP, PPG
- **Access**: Credentialed
- **URL**: https://physionet.org/content/mimic3wdb/

### PTB-XL
- **Size**: 500 MB
- **Samples**: 21,837 recordings
- **Conditions**: Myocardial Infarction, Bundle Branch Block, Arrhythmia
- **URL**: https://physionet.org/content/ptb-xl/

## 🧬 Cancer

### TCGA (The Cancer Genome Atlas)
- **Size**: 2.5 TB
- **Samples**: 11,000+ cases
- **Cancer Types**: 33 types including:
  - BRCA (Breast), LUAD (Lung Adenocarcinoma), LUSC (Lung Squamous), COAD (Colon), GBM (Glioblastoma), OV (Ovarian), KIRC (Kidney), HNSC (Head & Neck), and 25 more
- **Data Types**: WGS, WES, RNA-Seq, miRNA-Seq, Methylation
- **URL**: https://portal.gdc.cancer.gov

### TCIA (The Cancer Imaging Archive)
- **Size**: 100+ TB
- **Collections**: 30+ cancer types
- **Modalities**: CT, MRI, PET
- **URL**: https://www.cancerimagingarchive.net

### METABRIC (Breast Cancer)
- **Size**: 5 GB
- **Samples**: 2,509 cases
- **Data Types**: Gene Expression, CNV, Clinical
- **URL**: https://www.cbioportal.org/study/summary?id=brca_metabric

## 🩺 Dermatology

### HAM10000
- **Size**: 10 GB
- **Samples**: 10,015 images
- **Conditions**: 7 types
  - Melanoma, Melanocytic Nevus, Basal Cell Carcinoma, Actinic Keratosis, Benign Keratosis, Dermatofibroma, Vascular Lesion
- **URL**: https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/DBW86T

### ISIC Archive
- **Size**: 100 GB
- **Samples**: 50,000+ images
- **Conditions**: Melanoma, Nevus, Seborrheic Keratosis
- **URL**: https://www.isic-archive.com

### Fitzpatrick17k
- **Size**: 5 GB
- **Samples**: 16,577 images
- **Skin Types**: All Fitzpatrick types (I-VI)
- **URL**: https://github.com/mattgroh/fitzpatrick17k

## 🦠 Infectious Diseases

### COVIDx
- **Size**: 5 GB
- **Samples**: 30,000 images
- **Conditions**: COVID-19
- **Modalities**: X-ray, CT
- **URL**: https://github.com/lindawangg/COVID-Net

### Tuberculosis Chest X-ray
- **Size**: 2 GB
- **Samples**: 4,200 images
- **Conditions**: Tuberculosis
- **URL**: https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset

### Malaria Cell Images
- **Size**: 1 GB
- **Samples**: 27,558 images
- **Modality**: Microscopy
- **URL**: https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria

## 🩸 Diabetes

### Diabetic Retinopathy Detection
- **Size**: 88 GB
- **Samples**: 88,702 images
- **Modality**: Fundus Photography
- **Severity Levels**: 5 (0-4)
- **URL**: https://www.kaggle.com/c/diabetic-retinopathy-detection

### Pima Indians Diabetes
- **Size**: 1 MB
- **Samples**: 768 cases
- **Type**: Clinical data
- **URL**: https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

## 🏥 General & Multi-Disease

### MIMIC-IV
- **Size**: 10 TB
- **Samples**: 73,000+ ICU stays
- **Data Types**: Vitals, Labs, Medications, Notes, Diagnoses
- **Access**: Credentialed
- **URL**: https://physionet.org/content/mimiciv/

### Disease-Symptom Mapping (GTS.ai)
- **Size**: 50 MB
- **Conditions**: 400+ diseases
- **Type**: Structured symptoms and treatments
- **URL**: https://gts.ai/datasets

## Usage Examples

### Search by Disease Category
```python
from src.storage.disease_vector_db import DiseaseVectorDB

db = DiseaseVectorDB()

# Search respiratory diseases
results = db.search_by_disease(
    "disease_respiratory",
    query_vector,
    condition="Pneumonia"
)
```

### Find Datasets for Specific Condition
```python
from src.ingest.disease_specific_ingester import DiseaseSpecificIngester

ingester = DiseaseSpecificIngester()

# Find all datasets with melanoma
datasets = ingester.list_datasets_by_condition("melanoma")
```

### API Query
```bash
# Search for similar pneumonia cases
curl -X POST "http://localhost:8000/search/condition/Pneumonia" \
  -H "Content-Type: application/json" \
  -d '{"text": "patient with fever and cough", "top_k": 10}'
```

## Dataset Access Requirements

### Public Access (No Registration)
- NIH Chest X-ray14
- COVIDx
- MIT-BIH Arrhythmia
- HAM10000
- ISIC Archive
- Tuberculosis Dataset
- Malaria Dataset

### Registration Required
- CheXpert (Stanford)
- BraTS (CBICA)
- TCIA (Cancer Imaging Archive)

### Credentialed Access
- MIMIC-IV (PhysioNet)
- MIMIC Waveform
- UK Biobank
- ADNI
- All of Us

## Total Dataset Coverage

- **Categories**: 8 major disease categories
- **Datasets**: 25+ individual datasets
- **Conditions**: 400+ specific conditions
- **Total Size**: 400+ TB
- **Samples**: Millions of medical records and images
