# Quick Reference Guide

## 🚀 Getting Started in 5 Minutes

```bash
# 1. Start services
docker-compose up -d

# 2. Install dependencies
pip install -r requirements.txt

# 3. View all available datasets
python scripts/show_dataset_stats.py

# 4. Search for specific condition
python scripts/list_datasets_by_condition.py "breast cancer"

# 5. Setup collections
python scripts/setup_disease_collections.py

# 6. Start API
python src/api/disease_query_api.py
```

## 📊 Dataset Quick Stats

| Category | Datasets | Size | Top Dataset |
|----------|----------|------|-------------|
| Respiratory | 11 | 6+ TB | MIMIC-CXR (4.7TB) |
| Neurological | 10 | 5.8+ TB | HCP (5TB) |
| Cardiovascular | 9 | 4.6+ TB | MIMIC Waveform (4TB) |
| Cancer | 11 | 4+ TB | TCGA (2.5TB) |
| Orthopedic | 4 | 5+ TB | OAI (5TB) |
| Pathology | 4 | 2.7+ TB | TCGA-BRCA Slides (2TB) |
| Ophthalmology | 5 | 100+ GB | EyePACS (88GB) |
| Kidney/Liver | 5 | 470+ GB | TCGA-KIRC (200GB) |
| Mental Health | 3 | 180+ GB | BSNIP (100GB) |
| Dermatology | 3 | 115+ GB | ISIC (100GB) |
| General | 2 | 10+ TB | MIMIC-IV (10TB) |
| **TOTAL** | **75+** | **450+ TB** | - |

## 🔍 Search by Condition

### Cancer
```bash
python scripts/list_datasets_by_condition.py "breast cancer"
python scripts/list_datasets_by_condition.py "lung cancer"
python scripts/list_datasets_by_condition.py "melanoma"
```

### Neurological
```bash
python scripts/list_datasets_by_condition.py "alzheimer"
python scripts/list_datasets_by_condition.py "parkinson"
python scripts/list_datasets_by_condition.py "stroke"
```

### Respiratory
```bash
python scripts/list_datasets_by_condition.py "pneumonia"
python scripts/list_datasets_by_condition.py "covid"
python scripts/list_datasets_by_condition.py "tuberculosis"
```

### Cardiovascular
```bash
python scripts/list_datasets_by_condition.py "arrhythmia"
python scripts/list_datasets_by_condition.py "heart failure"
python scripts/list_datasets_by_condition.py "infarction"
```

## 🎯 Top 10 Largest Datasets

1. **MIMIC-IV** (10 TB) - ICU data, all conditions
2. **OAI** (5 TB) - Osteoarthritis
3. **HCP** (5 TB) - Brain connectivity
4. **MIMIC-CXR** (4.7 TB) - Chest X-rays + reports
5. **MIMIC Waveform** (4 TB) - ECG/ABP/PPG
6. **TCGA** (2.5 TB) - 33 cancer types
7. **TCGA-BRCA Slides** (2 TB) - Histopathology
8. **PadChest** (1 TB) - 160K chest X-rays
9. **Camelyon17** (1 TB) - Breast metastases
10. **Camelyon16** (700 GB) - Lymph node metastases

## 🏥 By Medical Specialty

### Radiology
- Chest: MIMIC-CXR, PadChest, CheXpert, NIH X-ray14
- Neuro: HCP, BraTS, OASIS, ADNI
- Cardiac: Cardiac Atlas, ACDC, MESA
- Oncology: TCIA collections, NSCLC-Radiomics

### Pathology
- Camelyon16/17 (breast metastases)
- TCGA whole-slide images
- PanNuke (nuclei segmentation)
- Lizard (colon cancer)

### Cardiology
- MIMIC Waveform (ICU)
- PTB-XL (ECG)
- CINC Challenge (27 abnormalities)
- Cardiac Atlas (MRI)

### Oncology
- TCGA (genomics)
- TCIA (imaging)
- Camelyon (histopathology)
- METABRIC (breast cancer)

### Neurology
- HCP (connectivity)
- ADNI (Alzheimer's)
- PPMI (Parkinson's)
- ABIDE (Autism)

## 🔑 Access Requirements

### Public (No Registration)
- NIH Chest X-ray14
- COVIDx
- HAM10000
- ISIC Archive
- MURA
- PatchCamelyon
- Most Kaggle datasets

### Registration Required
- CheXpert (Stanford)
- BraTS (CBICA)
- TCIA collections
- OAI
- MESA
- HCP

### Credentialed Access (PhysioNet)
- MIMIC-IV
- MIMIC-CXR
- MIMIC Waveform
- ADNI
- PPMI
- UK Biobank

## 📡 API Endpoints

```bash
# List all datasets
curl http://localhost:8000/datasets

# Find datasets by condition
curl http://localhost:8000/datasets/condition/melanoma

# List all conditions
curl http://localhost:8000/conditions

# Search by disease category
curl -X POST http://localhost:8000/search/disease \
  -H "Content-Type: application/json" \
  -d '{"text": "patient with pneumonia", "disease_category": "respiratory"}'

# Search by condition
curl -X POST http://localhost:8000/search/condition/cancer \
  -H "Content-Type: application/json" \
  -d '{"text": "tumor in lung", "top_k": 10}'

# Upload image for similar cases
curl -X POST "http://localhost:8000/search/similar-cases?disease_category=respiratory" \
  -F "file=@chest_xray.dcm"

# Get category statistics
curl http://localhost:8000/stats/respiratory
```

## 💻 Python SDK Examples

### Search by Text
```python
from src.storage.disease_vector_db import DiseaseVectorDB
from src.embeddings.ehr_embedder import EHREmbedder

db = DiseaseVectorDB()
embedder = EHREmbedder()

query = "patient with diabetes and hypertension"
query_vector = embedder.embed_text(query)

results = db.search_by_disease(
    "disease_general",
    query_vector,
    top_k=10
)
```

### Search by Image
```python
from src.embeddings.imaging_embedder import MedicalImagingEmbedder

embedder = MedicalImagingEmbedder()
query_vector = embedder.embed("chest_xray.dcm")

results = db.search_by_disease(
    "disease_respiratory",
    query_vector,
    modality="X-ray",
    top_k=10
)
```

### Search by Condition
```python
results = db.search_by_disease(
    "disease_cancer",
    query_vector,
    condition="Breast Cancer",
    top_k=10
)
```

### Cross-Category Search
```python
results = db.search_across_diseases(
    query_vector,
    categories=['respiratory', 'cardiovascular', 'infectious'],
    top_k=10
)
```

## 🎓 Use Case Examples

### Clinical Decision Support
```python
# Find similar ICU cases
from src.ingest.mimic_ingester import MIMICIngester

mimic = MIMICIngester("/path/to/mimic-iv")
records = mimic.create_patient_records([patient_id])

embedding = ehr_embedder.embed_structured_ehr(records[0])
similar_cases = db.search_by_disease("disease_general", embedding)
```

### Radiology AI
```python
# Find similar chest X-rays
embedding = imaging_embedder.embed("new_chest_xray.dcm")
similar_images = db.search_by_disease(
    "disease_respiratory",
    embedding,
    modality="X-ray"
)
```

### Cancer Diagnosis
```python
# Find similar histopathology slides
embedding = imaging_embedder.embed("tissue_slide.jpg")
similar_cases = db.search_by_disease(
    "disease_cancer",
    embedding,
    condition="Breast Cancer",
    modality="Histopathology"
)
```

### Drug Discovery
```python
# Search genomics data
from src.embeddings.genomics_embedder import GenomicsEmbedder

genomics_embedder = GenomicsEmbedder()
sequence_embedding = genomics_embedder.embed_sequence("ATCGATCG...")

similar_sequences = db.search_by_disease(
    "disease_cancer",
    sequence_embedding
)
```

## 📚 Documentation Links

- [EXPANDED_DATASETS.md](EXPANDED_DATASETS.md) - Complete 75+ dataset catalog
- [DISEASE_DATASETS.md](DISEASE_DATASETS.md) - Disease-specific reference
- [USAGE.md](USAGE.md) - Detailed usage guide
- [DEPLOYMENT.md](DEPLOYMENT.md) - Production deployment

## 🆘 Troubleshooting

### Out of Memory
```bash
# Reduce batch size
python scripts/ingest_disease_data.py --max-samples 100
```

### Slow Queries
```yaml
# Edit config/vector_config.yaml
collections:
  medical_imaging:
    index_type: "HNSW"  # Faster than IVF_FLAT
    M: 16
    efConstruction: 200
```

### Connection Issues
```bash
# Check services
docker-compose ps

# View logs
docker-compose logs milvus
docker-compose logs minio
```

## 🎯 Next Steps

1. **Explore datasets**: `python scripts/show_dataset_stats.py`
2. **Search conditions**: `python scripts/list_datasets_by_condition.py <condition>`
3. **Setup collections**: `python scripts/setup_disease_collections.py`
4. **Ingest data**: `python scripts/ingest_disease_data.py --category <category>`
5. **Start API**: `python src/api/disease_query_api.py`
6. **Query data**: Use API endpoints or Python SDK

---

**Need help?** Check the documentation or open an issue on GitHub.
