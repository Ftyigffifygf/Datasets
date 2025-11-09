"""FastAPI query interface for medical vector database"""
from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List, Dict, Optional
import numpy as np
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from storage.vector_db import MedicalVectorDB
from embeddings.imaging_embedder import MedicalImagingEmbedder
from embeddings.ehr_embedder import EHREmbedder
from embeddings.genomics_embedder import GenomicsEmbedder


app = FastAPI(title="Medical Vector DB API", version="1.0.0")

# Initialize components
vector_db = MedicalVectorDB()
imaging_embedder = MedicalImagingEmbedder()
ehr_embedder = EHREmbedder()
genomics_embedder = GenomicsEmbedder()


class TextQuery(BaseModel):
    text: str
    collection: str = "ehr_clinical"
    top_k: int = 10


class SequenceQuery(BaseModel):
    sequence: str
    collection: str = "genomics"
    top_k: int = 10


class SearchResult(BaseModel):
    id: int
    distance: float
    source: str
    patient_id: str
    modality: str
    metadata: Dict


@app.get("/")
def root():
    return {
        "service": "Medical Vector Database API",
        "version": "1.0.0",
        "endpoints": {
            "search_text": "/search/text",
            "search_image": "/search/image",
            "search_sequence": "/search/sequence",
            "collections": "/collections"
        }
    }


@app.get("/collections")
def list_collections():
    """List available collections"""
    return {
        "collections": [
            "medical_imaging",
            "genomics",
            "ehr_clinical"
        ]
    }


@app.post("/search/text", response_model=List[SearchResult])
def search_text(query: TextQuery):
    """Search using clinical text query"""
    try:
        # Generate embedding
        query_vector = ehr_embedder.embed_text(query.text)
        
        # Search
        results = vector_db.search(
            query.collection,
            query_vector,
            top_k=query.top_k
        )
        
        # Format results
        formatted_results = []
        for hits in results:
            for hit in hits:
                formatted_results.append(SearchResult(
                    id=hit.id,
                    distance=hit.distance,
                    source=hit.entity.get('source'),
                    patient_id=hit.entity.get('patient_id'),
                    modality=hit.entity.get('modality'),
                    metadata=hit.entity.get('metadata')
                ))
        
        return formatted_results
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search/image")
async def search_image(file: UploadFile = File(...), top_k: int = 10):
    """Search using medical image"""
    try:
        # Save uploaded file temporarily
        temp_path = Path(f"/tmp/{file.filename}")
        with open(temp_path, "wb") as f:
            content = await file.read()
            f.write(content)
        
        # Generate embedding
        query_vector = imaging_embedder.embed(temp_path)
        
        # Search
        results = vector_db.search(
            "medical_imaging",
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
                    "source": hit.entity.get('source'),
                    "patient_id": hit.entity.get('patient_id'),
                    "modality": hit.entity.get('modality')
                })
        
        return formatted_results
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/search/sequence", response_model=List[SearchResult])
def search_sequence(query: SequenceQuery):
    """Search using DNA/RNA sequence"""
    try:
        # Generate embedding
        query_vector = genomics_embedder.embed_sequence(query.sequence)
        
        # Search
        results = vector_db.search(
            query.collection,
            query_vector,
            top_k=query.top_k
        )
        
        # Format results
        formatted_results = []
        for hits in results:
            for hit in hits:
                formatted_results.append(SearchResult(
                    id=hit.id,
                    distance=hit.distance,
                    source=hit.entity.get('source'),
                    patient_id=hit.entity.get('patient_id'),
                    modality=hit.entity.get('modality'),
                    metadata=hit.entity.get('metadata')
                ))
        
        return formatted_results
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
