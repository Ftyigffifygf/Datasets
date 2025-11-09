"""Generate embeddings for genomics data"""
import torch
from transformers import AutoTokenizer, AutoModel
import numpy as np
from Bio import SeqIO
from typing import List


class GenomicsEmbedder:
    def __init__(self, model_name: str = "zhihan1996/DNABERT-2-117M"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModel.from_pretrained(model_name, trust_remote_code=True).to(self.device)
        self.model.eval()
        
    def chunk_sequence(self, sequence: str, chunk_size: int = 512, overlap: int = 50) -> List[str]:
        """Split long sequences into overlapping chunks"""
        chunks = []
        for i in range(0, len(sequence), chunk_size - overlap):
            chunk = sequence[i:i + chunk_size]
            if len(chunk) >= 100:  # Minimum chunk size
                chunks.append(chunk)
        return chunks
    
    @torch.no_grad()
    def embed_sequence(self, sequence: str) -> np.ndarray:
        """Generate embedding for DNA/RNA sequence"""
        # Tokenize
        inputs = self.tokenizer(sequence, return_tensors="pt", 
                               truncation=True, max_length=512).to(self.device)
        
        # Generate embedding
        outputs = self.model(**inputs)
        
        # Use mean pooling
        embedding = outputs.last_hidden_state.mean(dim=1)
        
        return embedding.cpu().numpy().flatten()
    
    def embed_long_sequence(self, sequence: str) -> np.ndarray:
        """Embed long sequence by chunking and averaging"""
        chunks = self.chunk_sequence(sequence)
        
        if not chunks:
            return np.zeros(512)
        
        embeddings = []
        for chunk in chunks:
            emb = self.embed_sequence(chunk)
            embeddings.append(emb)
        
        # Average chunk embeddings
        return np.mean(embeddings, axis=0)
    
    def embed_fasta(self, fasta_path: str) -> dict:
        """Generate embeddings for sequences in FASTA file"""
        embeddings = {}
        
        for record in SeqIO.parse(fasta_path, "fasta"):
            seq_id = record.id
            sequence = str(record.seq)
            
            embedding = self.embed_long_sequence(sequence)
            embeddings[seq_id] = embedding
        
        return embeddings
    
    def embed_vcf_variants(self, vcf_path: str, reference_genome: dict) -> dict:
        """Generate embeddings for genetic variants"""
        # Simplified - in production, use proper VCF parsing
        embeddings = {}
        
        with open(vcf_path) as f:
            for line in f:
                if line.startswith('#'):
                    continue
                
                parts = line.strip().split('\t')
                chrom, pos, var_id, ref, alt = parts[:5]
                
                # Get context sequence around variant
                context_size = 100
                pos = int(pos)
                
                if chrom in reference_genome:
                    context = reference_genome[chrom][pos-context_size:pos+context_size]
                    embedding = self.embed_sequence(context)
                    embeddings[var_id] = embedding
        
        return embeddings
