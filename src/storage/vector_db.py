"""Vector database operations using Milvus"""
from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType, utility
import yaml
from typing import List, Dict, Any
import numpy as np


class MedicalVectorDB:
    def __init__(self, config_path: str = "config/vector_config.yaml"):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
        
        connections.connect(
            host=self.config['milvus']['host'],
            port=self.config['milvus']['port']
        )
        
    def create_collection(self, collection_name: str, modality: str):
        """Create a collection for a specific medical data modality"""
        if utility.has_collection(collection_name):
            print(f"Collection {collection_name} already exists")
            return Collection(collection_name)
        
        config = self.config['collections'][modality]
        
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=config['dimension']),
            FieldSchema(name="source", dtype=DataType.VARCHAR, max_length=256),
            FieldSchema(name="patient_id", dtype=DataType.VARCHAR, max_length=128),
            FieldSchema(name="modality", dtype=DataType.VARCHAR, max_length=64),
            FieldSchema(name="metadata", dtype=DataType.JSON)
        ]
        
        schema = CollectionSchema(fields=fields, description=f"{modality} medical data")
        collection = Collection(name=collection_name, schema=schema)
        
        # Create index
        index_params = {
            "metric_type": config['metric_type'],
            "index_type": config['index_type'],
            "params": {"nlist": config.get('nlist', 1024)}
        }
        collection.create_index(field_name="embedding", index_params=index_params)
        
        return collection
    
    def insert_vectors(self, collection_name: str, embeddings: np.ndarray, 
                      metadata: List[Dict[str, Any]]):
        """Insert vectors with metadata"""
        collection = Collection(collection_name)
        
        data = [
            embeddings.tolist(),
            [m['source'] for m in metadata],
            [m['patient_id'] for m in metadata],
            [m['modality'] for m in metadata],
            metadata
        ]
        
        collection.insert(data)
        collection.flush()
        
    def search(self, collection_name: str, query_vector: np.ndarray, 
               top_k: int = 10, filters: Dict = None):
        """Search for similar vectors"""
        collection = Collection(collection_name)
        collection.load()
        
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        
        results = collection.search(
            data=[query_vector.tolist()],
            anns_field="embedding",
            param=search_params,
            limit=top_k,
            output_fields=["source", "patient_id", "modality", "metadata"]
        )
        
        return results
