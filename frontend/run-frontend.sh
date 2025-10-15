#!/bin/bash

# Script to run the Next.js frontend

echo "🚀 Starting Next.js frontend..."
echo "📍 Frontend will be available at http://localhost:3000"
echo ""

# Check if .env.local exists
if [ ! -f .env.local ]; then
    echo "⚠️  Warning: .env.local file not found!"
    echo "Creating .env.local with default settings..."
    echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
    echo "✅ Created .env.local"
    echo ""
fi

# Check if node_modules exists
if [ ! -d node_modules ]; then
    echo "📦 Installing dependencies..."
    npm install
    echo ""
fi

# Run Next.js dev server
npm run dev

