# Quick Start Guide 🚀

Get your Diet Recipe App up and running in minutes!

## Prerequisites

Make sure you have:
- ✅ Python 3.13+ installed
- ✅ Node.js 18+ installed
- ✅ OpenAI API key ready

## Step 1: Backend Setup (5 minutes)

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create .env file:**
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```
   
   Replace `your_api_key_here` with your actual OpenAI API key.

4. **Start the backend:**
   ```bash
   uvicorn main:app --reload
   ```
   
   Or use the script:
   ```bash
   chmod +x run-backend.sh
   ./run-backend.sh
   ```

   ✅ Backend running at http://localhost:8000

## Step 2: Frontend Setup (3 minutes)

1. **Open a new terminal** and navigate to frontend:
   ```bash
   cd frontend
   ```

2. **Install Node dependencies:**
   ```bash
   npm install
   ```

3. **Create .env.local file:**
   ```bash
   echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
   ```

4. **Start the frontend:**
   ```bash
   npm run dev
   ```
   
   Or use the script:
   ```bash
   chmod +x run-frontend.sh
   ./run-frontend.sh
   ```

   ✅ Frontend running at http://localhost:3000

## Step 3: Test the App! 🎉

1. Open your browser and go to **http://localhost:3000**
2. Select your dietary preference (vegetarian or vegan)
3. Click "Generate Recipe"
4. Watch as GPT-4 creates a delicious recipe for you!

## Troubleshooting

### Backend Issues

**Error: "OPENAI_API_KEY not found"**
- Make sure your `.env` file exists in the root directory
- Check that it contains: `OPENAI_API_KEY=sk-...`

**Port 8000 already in use:**
```bash
# Find and kill the process
lsof -ti:8000 | xargs kill -9

# Or use a different port
uvicorn main:app --reload --port 8001
```

### Frontend Issues

**Error: "Cannot connect to API"**
- Make sure the backend is running at http://localhost:8000
- Check your `.env.local` file has the correct API URL

**Port 3000 already in use:**
```bash
# Next.js will automatically suggest port 3001
# Or manually specify:
npm run dev -- -p 3001
```

**Dependencies not installing:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

## What's Next?

- 📚 Read [README.md](README.md) for full documentation
- 🚀 Check [DEPLOYMENT.md](DEPLOYMENT.md) to deploy to Vercel
- 🔧 Explore the code and customize your app!

## Quick Commands Reference

**Backend:**
```bash
# Start backend
uvicorn main:app --reload

# Test backend directly
curl -X POST http://localhost:8000/recipe \
  -H "Content-Type: application/json" \
  -d '{"diet_type": "vegan"}'

# View API docs
open http://localhost:8000/docs
```

**Frontend:**
```bash
# Start frontend
cd frontend && npm run dev

# Build for production
npm run build

# Start production server
npm start
```

## Need Help?

- Check the API documentation: http://localhost:8000/docs
- Review the logs in your terminal
- Verify your OpenAI API key is valid
- Ensure both backend and frontend are running

Happy cooking! 👨‍🍳👩‍🍳

