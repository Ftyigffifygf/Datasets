# Usage Guide

## Quick Start

### 1. Setup Infrastructure

```bash
# Clone repository
git clone <repo-url>
cd medical-vectordb

# Copy environment file
cp .env.example .env

# Start services
docker-compose up -d

# Install dependencies
pip install -r requirements.txt

# Setup database collections
python src/pipeline/orchestrator.py --setup-only
```

### 2. Ingest Sample Data

```bash
# Ingest small sample for testing
python scripts/ingest_sample.py
```

### 3. Start API Server

```bash
# Start FastAPI server
python src/api/query_api.py

# API will be available at http://localhost:8000
# Interactive docs at http://localhost:8000/docs
```

## Data Ingestion

### Full Pipeline

```bash
# Run complete ingestion pipeline
python src/pipeline/orchestrator.py \
  --data-dir ./data \
  --mimic-dir /path/to/mimic-iv
```

### Individual Sources

#### TCIA (Cancer Imaging)

```python
from src.ingest.tcia_ingester import TCIAIngester

ingester = TCIAIngester()

# List available collections
collections = ingester.get_collections()

# Ingest specific collection
stats = ingester.ingest_collection(
    collection="TCGA-BRCA",
    output_dir=Path("data/imaging"),
    max_patients=100
)
```

#### 1000 Genomes

```python
from src.ingest.genomics_ingester import GenomicsIngester

ingester = GenomicsIngester()

# Ingest from S3
stats = ingester.ingest_1000genomes(
    output_dir=Path("data/genomics"),
    max_files=1000
)
```

#### MIMIC-IV (EHR)

```python
from src.ingest.mimic_ingester import MIMICIngester
from src.embeddings.ehr_embedder import EHREmbedder
from src.storage.vector_db import MedicalVectorDB

# Initialize
mimic = MIMICIngester(Path("/path/to/mimic-iv"))
embedder = EHREmbedder()
vector_db = MedicalVectorDB()

# Ingest to vector DB
stats = mimic.ingest_to_vectordb(
    embedder=embedder,
    vector_db=vector_db,
    collection_name="ehr_clinical",
    max_patients=10000
)
```

## Querying the Database

### Using Python SDK

```python
from src.storage.vector_db import MedicalVectorDB
from src.embeddings.ehr_embedder import EHREmbedder

# Initialize
vector_db = MedicalVectorDB()
embedder = EHREmbedder()

# Search by text
query = "patient with diabetes and hypertension"
query_vector = embedder.embed_text(query)

results = vector_db.search(
    collection_name="ehr_clinical",
    query_vector=query_vector,
    top_k=10
)

# Process results
for hits in results:
    for hit in hits:
        print(f"Patient: {hit.entity.get('patient_id')}")
        print(f"Distance: {hit.distance}")
        print(f"Metadata: {hit.entity.get('metadata')}")
```

### Using REST API

#### Search by Text

```bash
curl -X POST "http://localhost:8000/search/text" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "patient with lung cancer",
    "collection": "ehr_clinical",
    "top_k": 5
  }'
```

#### Search by Image

```bash
curl -X POST "http://localhost:8000/search/image?top_k=5" \
  -F "file=@chest_xray.dcm"
```

#### Search by DNA Sequence

```bash
curl -X POST "http://localhost:8000/search/sequence" \
  -H "Content-Type: application/json" \
  -d '{
    "sequence": "ATCGATCGATCG",
    "collection": "genomics",
    "top_k": 10
  }'
```

### Using Python Requests

```python
import requests

# Text search
response = requests.post(
    "http://localhost:8000/search/text",
    json={
        "text": "breast cancer patient",
        "collection": "ehr_clinical",
        "top_k": 10
    }
)

results = response.json()
for result in results:
    print(f"Patient: {result['patient_id']}")
    print(f"Distance: {result['distance']}")
```

## Advanced Usage

### Custom Embedding Models

```python
from src.embeddings.imaging_embedder import MedicalImagingEmbedder

# Use custom model
embedder = MedicalImagingEmbedder(
    model_name="your-custom-model"
)

# Generate embeddings
embedding = embedder.embed("path/to/image.dcm")
```

### Batch Processing

```python
from pathlib import Path
from src.embeddings.imaging_embedder import MedicalImagingEmbedder

embedder = MedicalImagingEmbedder()

# Process directory of images
image_paths = list(Path("data/imaging").glob("**/*.dcm"))

# Batch embed
embeddings = embedder.embed_batch(image_paths[:100])
```

### Filtering Results

```python
# Search with metadata filters
results = vector_db.search(
    collection_name="medical_imaging",
    query_vector=query_vector,
    top_k=10,
    filters={
        "modality": "CT",
        "source": "TCIA"
    }
)
```

## Performance Tuning

### Indexing Parameters

Edit `config/vector_config.yaml`:

```yaml
collections:
  medical_imaging:
    dimension: 768
    index_type: "IVF_FLAT"  # or IVF_SQ8, HNSW
    metric_type: "L2"       # or IP, COSINE
    nlist: 16384            # number of clusters
```

### Batch Sizes

```python
# Adjust batch size based on GPU memory
embedder = MedicalImagingEmbedder()
embeddings = embedder.embed_batch(
    image_paths,
    batch_size=32  # Reduce if OOM
)
```

## Monitoring

### Check Collection Stats

```python
from pymilvus import Collection

collection = Collection("medical_imaging")
print(f"Entities: {collection.num_entities}")
print(f"Index: {collection.index().params}")
```

### API Health Check

```bash
curl http://localhost:8000/health
```

## Troubleshooting

### Out of Memory

- Reduce batch size
- Use smaller embedding models
- Enable disk-based indexing

### Slow Queries

- Increase `nprobe` parameter
- Add more query nodes
- Use faster index type (HNSW)

### Connection Issues

```bash
# Check services
docker-compose ps

# View logs
docker-compose logs milvus
```
