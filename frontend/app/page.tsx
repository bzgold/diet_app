import { RecipeGenerator } from "@/components/recipe-generator"

export default function Home() {
  return (
    <main className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-12">
        <div className="mx-auto max-w-4xl">
          <div className="mb-12 text-center">
            <h1 className="mb-4 text-5xl font-bold tracking-tight text-foreground">AI Recipe Generator</h1>
            <p className="text-lg text-muted-foreground">
              Get personalized dinner recipes based on your dietary preferences
            </p>
          </div>

          <RecipeGenerator />
        </div>
      </div>
    </main>
  )
}
