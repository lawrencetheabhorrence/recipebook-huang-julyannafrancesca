from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm


# Create your views here.
@login_required
def index(request):
    recipes = Recipe.objects.all()
    return render(request, "ledger/recipe_list.html", {"recipes": recipes})


@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(
        request,
        "ledger/recipe_detail.html",
        {"recipe": recipe},
    )


@login_required
def recipe_add(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe_form.save()

    return render(request, "ledger/recipe_add.html", {"recipe_form": RecipeForm()})
