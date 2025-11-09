"""Generate embeddings for medical imaging data"""
import torch
from transformers import AutoModel, AutoProcessor
import pydicom
import nibabel as nib
import numpy as np
from typing import Union
from pathlib import Path


class MedicalImagingEmbedder:
    def __init__(self, model_name: str = "microsoft/BiomedCLIP-PubMedBERT_256-vit_base_patch16_224"):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModel.from_pretrained(model_name).to(self.device)
        self.processor = AutoProcessor.from_pretrained(model_name)
        self.model.eval()
        
    def load_dicom(self, path: str) -> np.ndarray:
        """Load DICOM image"""
        ds = pydicom.dcmread(path)
        return ds.pixel_array
    
    def load_nifti(self, path: str) -> np.ndarray:
        """Load NIfTI image"""
        img = nib.load(path)
        return img.get_fdata()
    
    def preprocess_image(self, image: np.ndarray) -> np.ndarray:
        """Normalize and prepare image"""
        # Normalize to 0-255
        image = ((image - image.min()) / (image.max() - image.min()) * 255).astype(np.uint8)
        
        # Convert to RGB if grayscale
        if len(image.shape) == 2:
            image = np.stack([image] * 3, axis=-1)
        
        return image
    
    @torch.no_grad()
    def embed(self, image_path: Union[str, Path]) -> np.ndarray:
        """Generate embedding for medical image"""
        path = Path(image_path)
        
        # Load based on format
        if path.suffix.lower() == '.dcm':
            image = self.load_dicom(str(path))
        elif path.suffix.lower() in ['.nii', '.nii.gz']:
            image = self.load_nifti(str(path))
            # Take middle slice for 3D volumes
            if len(image.shape) == 3:
                image = image[:, :, image.shape[2] // 2]
        else:
            raise ValueError(f"Unsupported format: {path.suffix}")
        
        # Preprocess
        image = self.preprocess_image(image)
        
        # Generate embedding
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)
        outputs = self.model.get_image_features(**inputs)
        
        return outputs.cpu().numpy().flatten()
    
    def embed_batch(self, image_paths: list) -> np.ndarray:
        """Generate embeddings for batch of images"""
        embeddings = []
        for path in image_paths:
            try:
                emb = self.embed(path)
                embeddings.append(emb)
            except Exception as e:
                print(f"Error processing {path}: {e}")
                embeddings.append(np.zeros(768))  # Placeholder
        
        return np.array(embeddings)
