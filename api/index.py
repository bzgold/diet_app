from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Literal
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

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

# Helper function to get OpenAI response
def get_response(prompt: str):
    """Get response from OpenAI API"""
    if not openai.api_key:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY not configured. Please set it in environment variables."
        )
    return openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
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
        # Create prompt
        prompt = f"""You are a helpful chef assistant specializing in simple, healthy recipes.

Generate a simple {request.diet_type} dinner recipe. 
Include:
- Recipe name
- Cooking time
- Ingredients list
- Step-by-step instructions

Keep it simple and easy to follow. Make it delicious and healthy."""
        
        # Call OpenAI API
        response = get_response(prompt)
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


# Vercel serverless function handler
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)