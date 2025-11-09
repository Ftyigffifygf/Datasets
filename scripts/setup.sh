#!/bin/bash

# Medical Vector DB Setup Script

echo "Setting up Medical Vector Database..."

# Create directories
mkdir -p data/{imaging,genomics,ehr}
mkdir -p logs
mkdir -p models

# Start infrastructure
echo "Starting Docker containers..."
docker-compose up -d

# Wait for services
echo "Waiting for services to be ready..."
sleep 30

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Setup collections
echo "Setting up vector database collections..."
python src/pipeline/orchestrator.py --setup-only

echo "Setup complete!"
echo ""
echo "Services running:"
echo "  - Milvus: localhost:19530"
echo "  - MinIO: localhost:9000"
echo "  - PostgreSQL: localhost:5432"
echo "  - Redis: localhost:6379"
echo ""
echo "Next steps:"
echo "  1. Run ingestion: python src/pipeline/orchestrator.py"
echo "  2. Start API: python src/api/query_api.py"
