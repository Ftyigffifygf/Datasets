"""Enhanced API with disease-specific endpoints"""
from fastapi import FastAPI, HTTPException, UploadFile, File, Query
from pydantic import BaseModel
from typing import List, Dict, Optional
import numpy as np
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from storage.disease_vector_db import DiseaseVectorDB
from embeddings.imaging_embedder import MedicalImagingEmbedder
from embeddings.ehr_embedder import EHREmbedder
from ingest.disease_specific_ingester import DiseaseSpecificIngester


app = FastAPI(title="Medical Disease Vector DB API", version="2.0.0")

# Initialize components
vector_db = DiseaseVectorDB()
imaging_embedder = MedicalImagingEmbedder()
ehr_embedder = EHREmbedder()
disease_ingester = DiseaseSpecificIngester()


class DiseaseQuery(BaseModel):
    text: str
    disease_category: Optional[str] = None
    condition: Optional[str] = None
    modality: Optional[str] = None
    top_k: int = 10


class DiseaseSearchResult(BaseModel):
    id: int
    distance: float
    disease_category: str
    condition: str
    dataset_source: str
    patient_id: str
    modality: str
    severity: str


@app.get("/")
def root():
    return {
        "service": "Medical Disease Vector Database API",
        "version": "2.0.0",
        "disease_categories": [
            "respiratory", "neurological", "cardiovascular",
            "cancer", "dermatology", "infectious", "diabetes", "general"
        ],
        "endpoints": {
            "search_by_disease": "/search/disease",
            "search_by_condition": "/search/condition",
            "list_datasets": "/datasets",
            "list_conditions": "/conditions",
            "disease_stats": "/stats/{category}"
        }
    }


@app.get("/datasets")
def list_datasets(category: Optional[str] = None):
    """List available disease datasets"""
    datasets = disease_ingester.list_datasets_by_category(category)
    return datasets


@app.get("/datasets/condition/{condition}")
def find_datasets_by_condition(condition: str):
    """Find datasets containing specific condition"""
    datasets = disease_ingester.list_datasets_by_condition(condition)
    return {
        "condition": condition,
        "matching_datasets": datasets,
        "count": len(datasets)
    }


@app.get("/conditions")
def list_all_conditions():
    """List all available conditions across datasets"""
    conditions = set()
    datasets = disease_ingester.list_datasets_by_category()
    
    for category, dataset_list in datasets.items():
        for dataset_name, info in dataset_list.items():
            if 'conditions' in info and isinstance(info['conditions'], list):
                conditions.update(info['conditions'])
    
    return {
        "total_conditions": len(conditions),
        "conditions": sorted(list(conditions))
    }


@app.post("/search/disease")
def search_by_disease(query: DiseaseQuery):
    """Search within specific disease category"""
    try:
        # Generate embedding
        query_vector = ehr_embedder.embed_text(query.text)
        
        # Determine collection
        if query.disease_category:
            collection_name = f"disease_{query.disease_category}"
        else:
            collection_name = "disease_general"
        
        # Search
        results = vector_db.search_by_disease(
            collection_name,
            query_vector,
            condition=query.condition,
            modality=query.modality,
            top_k=query.top_k
        )
        
        # Format results
        formatted_results = []
        for hits in results:
            for hit in hits:
                formatted_results.append({
                    "id": hit.id,
                    "distance": float(hit.distance),
                    "disease_category": hit.entity.get('disease_category'),
                    "condition": hit.entity.get('condition'),
                    "dataset_source": hit.entity.get('dataset_source'),
                    "patient_id": hit.entity.get('patient_id'),
                    "modality": hit.entity.get('modality'),
                    "severity": hit.entity.get('severity')
                })
        
        return {
            "query": query.text,
            "results": formatted_results,
            "count": len(formatted_results)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search/condition/{condition}")
def search_by_condition(condition: str, 
                       text: str,
                       top_k: int = 10):
    """Search for similar cases of specific condition"""
    try:
        query_vector = ehr_embedder.embed_text(text)
        
        # Search across all disease categories
        results = vector_db.search_across_diseases(
            query_vector,
            top_k=top_k
        )
        
        # Filter by condition
        filtered_results = {}
        for category, category_results in results.items():
            matching = []
            for hits in category_results:
                for hit in hits:
                    if condition.lower() in hit.entity.get('condition', '').lower():
                        matching.append({
                            "id": hit.id,
                            "distance": float(hit.distance),
                            "condition": hit.entity.get('condition'),
                            "patient_id": hit.entity.get('patient_id')
                        })
            
            if matching:
                filtered_results[category] = matching
        
        return {
            "condition": condition,
            "results_by_category": filtered_results
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/stats/{category}")
def get_disease_stats(category: str):
    """Get statistics for disease category"""
    try:
        collection_name = f"disease_{category}"
        stats = vector_db.get_disease_statistics(collection_name)
        return stats
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Category not found: {category}")


@app.post("/search/similar-cases")
async def search_similar_cases(
    file: UploadFile = File(...),
    disease_category: str = Query(...),
    top_k: int = 10
):
    """Find similar medical cases by uploading an image"""
    try:
        # Save uploaded file
        temp_path = Path(f"/tmp/{file.filename}")
        with open(temp_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Generate embedding
        query_vector = imaging_embedder.embed(temp_path)
        
        # Search
        collection_name = f"disease_{disease_category}"
        results = vector_db.search_by_disease(
            collection_name,
            query_vector,
            top_k=top_k
        )
        
        # Clean up
        temp_path.unlink()
        
        # Format results
        formatted_results = []
        for hits in results:
            for hit in hits:
                formatted_results.append({
                    "id": hit.id,
                    "distance": float(hit.distance),
                    "condition": hit.entity.get('condition'),
                    "dataset_source": hit.entity.get('dataset_source')
                })
        
        return {
            "disease_category": disease_category,
            "similar_cases": formatted_results
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "2.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
