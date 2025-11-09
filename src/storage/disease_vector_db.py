"""Enhanced vector database with disease-specific collections and metadata"""
from pymilvus import connections, Collection, CollectionSchema, FieldSchema, DataType, utility
import yaml
from typing import List, Dict, Any
import numpy as np
from pathlib import Path


class DiseaseVectorDB:
    def __init__(self, config_path: str = "config/vector_config.yaml"):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
        
        connections.connect(
            host=self.config['milvus']['host'],
            port=self.config['milvus']['port']
        )
        
        # Load disease categories
        disease_config_path = Path("config/disease_datasets.yaml")
        if disease_config_path.exists():
            with open(disease_config_path) as f:
                self.disease_datasets = yaml.safe_load(f)
    
    def create_disease_collection(self, disease_category: str, dimension: int = 768):
        """Create collection for specific disease category"""
        collection_name = f"disease_{disease_category}"
        
        if utility.has_collection(collection_name):
            print(f"Collection {collection_name} already exists")
            return Collection(collection_name)
        
        fields = [
            FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
            FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=dimension),
            FieldSchema(name="disease_category", dtype=DataType.VARCHAR, max_length=64),
            FieldSchema(name="condition", dtype=DataType.VARCHAR, max_length=128),
            FieldSchema(name="dataset_source", dtype=DataType.VARCHAR, max_length=128),
            FieldSchema(name="patient_id", dtype=DataType.VARCHAR, max_length=128),
            FieldSchema(name="modality", dtype=DataType.VARCHAR, max_length=64),
            FieldSchema(name="severity", dtype=DataType.VARCHAR, max_length=32),
            FieldSchema(name="metadata", dtype=DataType.JSON)
        ]
        
        schema = CollectionSchema(fields=fields, 
                                 description=f"{disease_category} disease data")
        collection = Collection(name=collection_name, schema=schema)
        
        # Create index
        index_params = {
            "metric_type": "L2",
            "index_type": "IVF_FLAT",
            "params": {"nlist": 2048}
        }
        collection.create_index(field_name="embedding", index_params=index_params)
        
        return collection
    
    def insert_disease_vectors(self, collection_name: str, 
                              embeddings: np.ndarray,
                              disease_metadata: List[Dict[str, Any]]):
        """Insert vectors with disease-specific metadata"""
        collection = Collection(collection_name)
        
        data = [
            embeddings.tolist(),
            [m['disease_category'] for m in disease_metadata],
            [m['condition'] for m in disease_metadata],
            [m['dataset_source'] for m in disease_metadata],
            [m['patient_id'] for m in disease_metadata],
            [m['modality'] for m in disease_metadata],
            [m.get('severity', 'unknown') for m in disease_metadata],
            disease_metadata
        ]
        
        collection.insert(data)
        collection.flush()
    
    def search_by_disease(self, collection_name: str, 
                         query_vector: np.ndarray,
                         condition: str = None,
                         modality: str = None,
                         top_k: int = 10) -> List[Dict]:
        """Search with disease-specific filters"""
        collection = Collection(collection_name)
        collection.load()
        
        # Build filter expression
        filters = []
        if condition:
            filters.append(f'condition == "{condition}"')
        if modality:
            filters.append(f'modality == "{modality}"')
        
        expr = " && ".join(filters) if filters else None
        
        search_params = {"metric_type": "L2", "params": {"nprobe": 10}}
        
        results = collection.search(
            data=[query_vector.tolist()],
            anns_field="embedding",
            param=search_params,
            limit=top_k,
            expr=expr,
            output_fields=["disease_category", "condition", "dataset_source", 
                          "patient_id", "modality", "severity", "metadata"]
        )
        
        return results
    
    def get_disease_statistics(self, collection_name: str) -> Dict:
        """Get statistics for disease collection"""
        collection = Collection(collection_name)
        collection.load()
        
        stats = {
            'total_records': collection.num_entities,
            'collection_name': collection_name
        }
        
        return stats
    
    def create_all_disease_collections(self):
        """Create collections for all disease categories"""
        categories = [
            'respiratory',
            'neurological', 
            'cardiovascular',
            'cancer',
            'dermatology',
            'infectious',
            'diabetes',
            'general'
        ]
        
        created = []
        for category in categories:
            collection = self.create_disease_collection(category)
            created.append(collection.name)
            print(f"Created collection: {collection.name}")
        
        return created
    
    def search_across_diseases(self, query_vector: np.ndarray,
                              categories: List[str] = None,
                              top_k: int = 10) -> Dict[str, List]:
        """Search across multiple disease categories"""
        if not categories:
            categories = ['respiratory', 'neurological', 'cardiovascular', 
                         'cancer', 'dermatology', 'infectious']
        
        results = {}
        
        for category in categories:
            collection_name = f"disease_{category}"
            
            if utility.has_collection(collection_name):
                try:
                    category_results = self.search_by_disease(
                        collection_name, query_vector, top_k=top_k
                    )
                    results[category] = category_results
                except Exception as e:
                    print(f"Error searching {category}: {e}")
        
        return results
