# Diet Recipe App 🥗

A full-stack application with FastAPI backend and Next.js frontend that uses GPT-4 to generate vegetarian and vegan dinner recipes based on your dietary preferences.

## Features

- 🌱 Support for vegetarian and vegan diets
- 🤖 Powered by OpenAI's GPT-4
- 📝 Simple, easy-to-follow recipes
- 🚀 Fast and lightweight FastAPI backend
- ⚛️ Modern Next.js frontend with React 18.3.1
- 🎨 Beautiful UI with Tailwind CSS and shadcn/ui
- 📚 Interactive API documentation with Swagger UI
- ☁️ Easy deployment to Vercel

## Requirements

- Python 3.13+
- Node.js 18+
- OpenAI API key

## Installation

### Backend Setup

1. Clone the repository or navigate to the project directory

2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```bash
touch .env
```

5. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your_actual_api_key_here
```

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env.local` file:
```bash
touch .env.local
```

4. Add the backend API URL:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Usage

### Running the Backend

From the root directory:

```bash
# Using Python directly
python main.py

# Or using uvicorn
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Running the Frontend

From the frontend directory:

```bash
cd frontend
npm run dev
```

The frontend will be available at `http://localhost:3000`

### Full Stack Development

Open two terminal windows:

**Terminal 1 (Backend):**
```bash
uvicorn main:app --reload
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

Then visit `http://localhost:3000` in your browser!

### API Endpoints

#### GET `/`
Root endpoint with API information

#### POST `/recipe`
Get a dinner recipe based on dietary preference

**Request Body:**
```json
{
  "diet_type": "vegetarian"  // or "vegan"
}
```

**Response:**
```json
{
  "diet_type": "vegetarian",
  "recipe": "Recipe name\n\nCooking time: ...\n\nIngredients:\n..."
}
```

#### GET `/health`
Health check endpoint

### Using the API

#### Using cURL:
```bash
curl -X POST "http://localhost:8000/recipe" \
  -H "Content-Type: application/json" \
  -d '{"diet_type": "vegetarian"}'
```

#### Using Python requests:
```python
import requests

response = requests.post(
    "http://localhost:8000/recipe",
    json={"diet_type": "vegan"}
)
print(response.json())
```

#### Using the Interactive Docs:
Visit `http://localhost:8000/docs` in your browser for an interactive Swagger UI where you can test the API directly.

## Project Structure

```
test-app3/
├── main.py              # FastAPI application
├── api/
│   └── index.py        # Vercel serverless handler
├── requirements.txt     # Python dependencies
├── vercel.json         # Backend Vercel config
├── .env                # Backend environment variables (create this)
├── .vercelignore       # Files to ignore in backend deployment
├── README.md           # This file
├── DEPLOYMENT.md       # Deployment guide
├── LICENSE            # License file
└── frontend/
    ├── app/            # Next.js app directory
    ├── components/     # React components
    ├── lib/           # Utilities
    ├── public/        # Static assets
    ├── package.json   # Frontend dependencies
    ├── .env.local     # Frontend environment variables (create this)
    └── .env.example   # Example frontend environment file
```

## Configuration

### Backend Environment Variables (.env)

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Frontend Environment Variables (.env.local)

- `NEXT_PUBLIC_API_URL`: Backend API URL (default: http://localhost:8000)

## Deployment to Vercel

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

### Quick Deploy

**Backend:**
```bash
vercel
```

**Frontend:**
```bash
cd frontend
vercel
```

Make sure to set environment variables in Vercel dashboard:
- Backend: `OPENAI_API_KEY`
- Frontend: `NEXT_PUBLIC_API_URL`

## License

See LICENSE file for details.

## Technology Stack

### Backend
- FastAPI (Python 3.13+)
- OpenAI GPT-4 API
- Uvicorn server
- python-dotenv

### Frontend
- Next.js 15
- React 18.3.1
- TypeScript
- Tailwind CSS
- shadcn/ui components
- vaul 1.1.1

## Notes

- The app uses GPT-4 model by default. Make sure your OpenAI account has access to GPT-4.
- Each recipe generation will consume OpenAI API credits.
- All libraries are compatible with Python 3.13.
- React version 18.3.1 ensures compatibility with all dependencies.
- Frontend uses modern Next.js App Router.

