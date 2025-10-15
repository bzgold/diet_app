# Deployment Guide

This guide explains how to deploy both the FastAPI backend and Next.js frontend to Vercel.

## Prerequisites

- [Vercel account](https://vercel.com)
- [Vercel CLI](https://vercel.com/cli) installed: `npm i -g vercel`
- OpenAI API key

## Project Structure

```
test-app3/
├── main.py              # FastAPI backend
├── api/
│   └── index.py        # Vercel serverless handler
├── vercel.json         # Backend deployment config
├── requirements.txt    # Python dependencies
├── .env                # Backend environment variables (local)
└── frontend/
    ├── app/            # Next.js app
    ├── components/     # React components
    ├── package.json    # Frontend dependencies
    ├── .env.local      # Frontend environment variables (local)
    └── vercel.json     # Frontend deployment config (auto-generated)
```

## Local Development

### Backend (FastAPI)

1. Navigate to the root directory
2. Activate your virtual environment
3. Create `.env` file with:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. Run the backend:
   ```bash
   uvicorn main:app --reload
   ```
   Backend will be available at `http://localhost:8000`

### Frontend (Next.js)

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create `.env.local` file with:
   ```
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```
4. Run the frontend:
   ```bash
   npm run dev
   ```
   Frontend will be available at `http://localhost:3000`

## Deploying to Vercel

### Option 1: Deploy via Vercel Dashboard (Recommended)

#### Deploy Backend

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "Add New" → "Project"
3. Import your repository
4. Configure:
   - **Framework Preset:** Other
   - **Root Directory:** `./` (root)
   - **Build Command:** Leave empty
   - **Output Directory:** Leave empty
5. Add Environment Variable:
   - Key: `OPENAI_API_KEY`
   - Value: Your OpenAI API key
6. Click "Deploy"
7. Note your backend URL (e.g., `https://your-backend.vercel.app`)

#### Deploy Frontend

1. In Vercel Dashboard, click "Add New" → "Project"
2. Import the same repository
3. Configure:
   - **Framework Preset:** Next.js
   - **Root Directory:** `./frontend`
   - **Build Command:** `npm run build`
   - **Output Directory:** `.next`
4. Add Environment Variable:
   - Key: `NEXT_PUBLIC_API_URL`
   - Value: Your backend URL from step 7 above
5. Click "Deploy"

### Option 2: Deploy via Vercel CLI

#### Deploy Backend

```bash
# From the root directory
vercel

# Follow the prompts:
# Set up and deploy? [Y/n] y
# Which scope? Select your account
# Link to existing project? [y/N] n
# What's your project's name? diet-app-backend
# In which directory is your code located? ./

# Add environment variable
vercel env add OPENAI_API_KEY
# Paste your OpenAI API key when prompted
# Select Production, Preview, Development

# Deploy to production
vercel --prod
```

Note the deployment URL for your backend.

#### Deploy Frontend

```bash
# Navigate to frontend directory
cd frontend

# Deploy
vercel

# Follow the prompts:
# Set up and deploy? [Y/n] y
# Which scope? Select your account
# Link to existing project? [y/N] n
# What's your project's name? diet-app-frontend
# In which directory is your code located? ./

# Add environment variable with your backend URL
vercel env add NEXT_PUBLIC_API_URL
# Enter your backend URL (from backend deployment)
# Select Production, Preview, Development

# Deploy to production
vercel --prod
```

## Environment Variables

### Backend (.env)
```
OPENAI_API_KEY=sk-...
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=https://your-backend.vercel.app
```

## Vercel Configuration Files

### Backend (vercel.json in root)
```json
{
  "version": 2,
  "builds": [
    {
      "src": "main.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "main.py"
    }
  ]
}
```

### Frontend
Next.js is auto-detected by Vercel, no configuration needed.

## Troubleshooting

### Backend Issues

1. **Import errors:** Make sure all dependencies in `requirements.txt` are compatible with Vercel's Python runtime
2. **CORS errors:** Backend is configured to accept requests from Vercel domains
3. **Environment variables:** Ensure `OPENAI_API_KEY` is set in Vercel dashboard

### Frontend Issues

1. **API connection:** Verify `NEXT_PUBLIC_API_URL` points to your deployed backend
2. **Build errors:** Check that React 18.3.1 and vaul 1.1.1 are properly installed
3. **Environment variables:** Ensure they're prefixed with `NEXT_PUBLIC_` for client-side access

## Post-Deployment

1. Test the frontend URL in your browser
2. Select a diet type and generate a recipe
3. Check Vercel deployment logs if issues occur
4. Monitor API usage in OpenAI dashboard

## Updating Deployments

### Backend
```bash
# Make changes to main.py or requirements.txt
git push  # If connected to GitHub
# or
vercel --prod  # Direct deployment
```

### Frontend
```bash
cd frontend
# Make changes
git push  # If connected to GitHub
# or
vercel --prod  # Direct deployment
```

## Custom Domains

You can add custom domains in the Vercel dashboard:
1. Go to your project settings
2. Navigate to "Domains"
3. Add your custom domain
4. Update DNS records as instructed
5. Update `NEXT_PUBLIC_API_URL` if backend domain changed

## Cost Considerations

- Vercel: Free tier includes hobby projects
- OpenAI API: Pay per token usage
- Monitor usage to avoid unexpected costs

## Support

- [Vercel Documentation](https://vercel.com/docs)
- [Next.js Documentation](https://nextjs.org/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com)

