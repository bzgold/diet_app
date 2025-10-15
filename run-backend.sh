#!/bin/bash

# Script to run the FastAPI backend

echo "🚀 Starting FastAPI backend..."
echo "📍 API will be available at http://localhost:8000"
echo "📚 API docs will be available at http://localhost:8000/docs"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "Please create a .env file with your OPENAI_API_KEY"
    echo "Example: OPENAI_API_KEY=sk-..."
    echo ""
    exit 1
fi

# Run uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000

