from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Literal
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Diet Recipe App",
    description="Get simple dinner recipes based on your dietary preferences",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://*.vercel.app",
        "*"  # Allow all origins for development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client lazily
def get_openai_client():
    """Get OpenAI client, initializing it lazily"""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY not configured. Please set it in environment variables."
        )
    # Explicitly initialize without custom http client to avoid proxy issues on Vercel
    return OpenAI(
        api_key=api_key,
        max_retries=2,
        timeout=30.0
    )


# Request model
class RecipeRequest(BaseModel):
    diet_type: Literal["vegetarian", "vegan"]


# Response model
class RecipeResponse(BaseModel):
    diet_type: str
    recipe: str


@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to the Diet Recipe App!",
        "endpoints": {
            "/recipe": "POST - Get a dinner recipe based on your diet",
            "/docs": "GET - Interactive API documentation"
        }
    }


@app.post("/recipe", response_model=RecipeResponse)
async def get_recipe(request: RecipeRequest):
    """
    Get a simple dinner recipe based on dietary preference
    
    - **diet_type**: Either 'vegetarian' or 'vegan'
    """
    try:
        # Get OpenAI client
        client = get_openai_client()
        
        # Create prompt for GPT-4
        prompt = f"""Generate a simple {request.diet_type} dinner recipe. 
        Include:
        - Recipe name
        - Cooking time
        - Ingredients list
        - Step-by-step instructions
        
        Keep it simple and easy to follow. Make it delicious and healthy."""
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful chef assistant specializing in simple, healthy recipes."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        recipe_text = response.choices[0].message.content
        
        return RecipeResponse(
            diet_type=request.diet_type,
            recipe=recipe_text
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating recipe: {str(e)}"
        )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

