from django.shortcuts import render

from .models import Recipe, RecipeIngredient


# Create your views here.
def index(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    return render(
        request,
        "ledger/recipe_detail.html",
        {"name": recipe.name, "ingredients": ingredients},
    )
