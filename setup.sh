#!/bin/bash

# Setup script for Mangosteen-documents project

set -e  # Exit on error

echo "Starting setup..."

# 1. Check and create documents folder structure
if [ ! -d "documents" ]; then
    echo "Creating documents folder structure..."
    mkdir -p documents/inputs
    mkdir -p documents/ppl
    mkdir -p documents/filtered_documents
    mkdir -p documents/extract_result
    echo "✓ Documents folder structure created"
else
    echo "✓ Documents folder already exists"
    # Ensure subdirectories exist
    mkdir -p documents/inputs
    mkdir -p documents/ppl
    mkdir -p documents/filtered_documents
    mkdir -p documents/extract_result
    echo "✓ Verified all subdirectories exist"
fi

# 2. Activate uv virtual environment
echo "Activating uv virtual environment..."
source .venv/bin/activate
echo "✓ Virtual environment activated"

# 3. Install dependencies
echo "Installing dependencies with uv..."
uv sync --group dev
echo "✓ Dependencies installed"

echo ""
echo "Setup complete! 🎉"

