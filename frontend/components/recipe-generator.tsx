"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Loader2, ChefHat, Leaf, Sprout } from "lucide-react"

type DietType = "vegetarian" | "vegan" | "none"

interface Recipe {
  diet_type: string
  recipe: string
}

export function RecipeGenerator() {
  const [dietType, setDietType] = useState<DietType>("none")
  const [recipe, setRecipe] = useState<Recipe | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleGenerateRecipe = async () => {
    setLoading(true)
    setError(null)
    setRecipe(null)

    try {
      const apiUrl = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

      // For "none" diet type, we'll send "vegetarian" to the backend
      // since the backend only accepts vegetarian or vegan
      const requestDietType = dietType === "none" ? "vegetarian" : dietType

      const response = await fetch(`${apiUrl}/recipe`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          diet_type: requestDietType,
        }),
      })

      if (!response.ok) {
        throw new Error("Failed to generate recipe")
      }

      const data: Recipe = await response.json()
      setRecipe(data)
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred")
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="space-y-6">
      <Card className="border-border bg-card">
        <CardHeader>
          <CardTitle className="text-card-foreground">Select Your Dietary Preference</CardTitle>
          <CardDescription className="text-muted-foreground">
            Choose your dietary restrictions to get a personalized recipe
          </CardDescription>
        </CardHeader>
        <CardContent>
          <RadioGroup value={dietType} onValueChange={(value) => setDietType(value as DietType)} className="space-y-4">
            <div className="flex items-center space-x-3 rounded-lg border border-border bg-secondary/50 p-4 transition-colors hover:bg-secondary">
              <RadioGroupItem value="none" id="none" />
              <Label htmlFor="none" className="flex flex-1 cursor-pointer items-center gap-3 text-secondary-foreground">
                <ChefHat className="h-5 w-5" />
                <div>
                  <div className="font-medium">No Restrictions</div>
                  <div className="text-sm text-muted-foreground">All ingredients welcome</div>
                </div>
              </Label>
            </div>

            <div className="flex items-center space-x-3 rounded-lg border border-border bg-secondary/50 p-4 transition-colors hover:bg-secondary">
              <RadioGroupItem value="vegetarian" id="vegetarian" />
              <Label
                htmlFor="vegetarian"
                className="flex flex-1 cursor-pointer items-center gap-3 text-secondary-foreground"
              >
                <Leaf className="h-5 w-5" />
                <div>
                  <div className="font-medium">Vegetarian</div>
                  <div className="text-sm text-muted-foreground">No meat, but includes dairy and eggs</div>
                </div>
              </Label>
            </div>

            <div className="flex items-center space-x-3 rounded-lg border border-border bg-secondary/50 p-4 transition-colors hover:bg-secondary">
              <RadioGroupItem value="vegan" id="vegan" />
              <Label
                htmlFor="vegan"
                className="flex flex-1 cursor-pointer items-center gap-3 text-secondary-foreground"
              >
                <Sprout className="h-5 w-5" />
                <div>
                  <div className="font-medium">Vegan</div>
                  <div className="text-sm text-muted-foreground">Plant-based only, no animal products</div>
                </div>
              </Label>
            </div>
          </RadioGroup>

          <Button
            onClick={handleGenerateRecipe}
            disabled={loading}
            className="mt-6 w-full bg-accent text-accent-foreground hover:bg-accent/90"
            size="lg"
          >
            {loading ? (
              <>
                <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                Generating Recipe...
              </>
            ) : (
              "Generate Recipe"
            )}
          </Button>
        </CardContent>
      </Card>

      {error && (
        <Card className="border-destructive bg-destructive/10">
          <CardContent className="pt-6">
            <p className="text-destructive-foreground">Error: {error}</p>
          </CardContent>
        </Card>
      )}

      {recipe && (
        <Card className="border-border bg-card">
          <CardHeader>
            <CardTitle className="text-card-foreground">
              Your {recipe.diet_type.charAt(0).toUpperCase() + recipe.diet_type.slice(1)} Recipe
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="prose prose-invert max-w-none whitespace-pre-wrap text-card-foreground">
              {recipe.recipe}
            </div>
          </CardContent>
        </Card>
      )}
    </div>
  )
}
