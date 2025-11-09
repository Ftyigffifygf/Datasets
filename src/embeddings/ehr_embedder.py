"""Generate embeddings for EHR and clinical text"""
import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np
from typing import List, Dict


class EHREmbedder:
    def __init__(self, model_name: str = "emilyalsentzer/Bio_ClinicalBERT"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.model.eval()
        
    @torch.no_grad()
    def embed_text(self, text: str) -> np.ndarray:
        """Generate embedding for clinical text"""
        inputs = self.tokenizer(text, return_tensors="pt", 
                               truncation=True, max_length=512, 
                               padding=True).to(self.device)
        
        outputs = self.model(**inputs)
        
        # Use CLS token embedding
        embedding = outputs.last_hidden_state[:, 0, :]
        
        return embedding.cpu().numpy().flatten()
    
    def embed_clinical_note(self, note: str) -> np.ndarray:
        """Embed clinical note with section handling"""
        # Split into sections if too long
        max_length = 512
        tokens = self.tokenizer.tokenize(note)
        
        if len(tokens) <= max_length:
            return self.embed_text(note)
        
        # Chunk and average
        chunks = []
        for i in range(0, len(tokens), max_length - 50):
            chunk = self.tokenizer.convert_tokens_to_string(tokens[i:i+max_length])
            chunks.append(chunk)
        
        embeddings = [self.embed_text(chunk) for chunk in chunks]
        return np.mean(embeddings, axis=0)
    
    def embed_structured_ehr(self, ehr_record: Dict) -> np.ndarray:
        """Embed structured EHR data"""
        # Convert structured data to text representation
        text_parts = []
        
        if 'diagnosis' in ehr_record:
            text_parts.append(f"Diagnosis: {ehr_record['diagnosis']}")
        
        if 'medications' in ehr_record:
            meds = ', '.join(ehr_record['medications'])
            text_parts.append(f"Medications: {meds}")
        
        if 'vitals' in ehr_record:
            vitals = ', '.join([f"{k}: {v}" for k, v in ehr_record['vitals'].items()])
            text_parts.append(f"Vitals: {vitals}")
        
        if 'labs' in ehr_record:
            labs = ', '.join([f"{k}: {v}" for k, v in ehr_record['labs'].items()])
            text_parts.append(f"Labs: {labs}")
        
        combined_text = '. '.join(text_parts)
        return self.embed_text(combined_text)
    
    def embed_batch(self, texts: List[str]) -> np.ndarray:
        """Generate embeddings for batch of texts"""
        embeddings = []
        
        for text in texts:
            emb = self.embed_text(text)
            embeddings.append(emb)
        
        return np.array(embeddings)
