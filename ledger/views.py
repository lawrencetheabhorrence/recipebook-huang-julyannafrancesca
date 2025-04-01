from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm, RecipeImageForm


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
def recipeingredient_add(request, recipe_id):
    if request.method == "POST":
        recipeingredient_form = RecipeIngredientForm(request.POST)
        if recipeingredient_form.is_valid():
            recipe = Recipe.objects.get(pk=recipe_id)
            recipeingredient = recipeingredient_form.save(commit=False)
            recipeingredient.recipe = recipe
            recipeingredient.save()
        return HttpResponseRedirect(reverse("recipe_detail", args=[recipe_id]))

    return render(
        request,
        "ledger/recipeingredient_add.html",
        {"recipeingredient_form": RecipeIngredientForm(), "recipe_id": recipe_id},
    )


@login_required
def recipeimage_add(request, recipe_id):
    if request.method == "POST":
        recipeimage = RecipeImage(recipe=Recipe.objects.get(pk=recipe_id))
        print(request.FILES)
        recipeimage_form = RecipeImageForm(
            request.POST, request.FILES, instance=recipeimage
        )
        if recipeimage_form.is_valid():
            recipeimage_form.save()

        return HttpResponseRedirect(reverse("recipe_detail", args=[recipe_id]))
    return render(
        request,
        "ledger/recipeimage_add.html",
        {"recipeimage_form": RecipeImageForm(), "recipe_id": recipe_id},
    )


@login_required
def ingredient_add(request):
    if request.method == "POST":
        ingredient_form = IngredientForm(request.POST)
        if ingredient_form.is_valid():
            ingredient_form.save()
        return HttpResponseRedirect(reverse("recipe_list"))

    return render(
        request,
        "ledger/ingredient_add.html",
        {"ingredient_form": IngredientForm()},
    )


@login_required
def recipe_add(request):
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save()
            if request.POST.get("add_ingredient"):
                return reverse(recipeingredient_add, recipe.id)
            return reverse(index)

    return render(request, "ledger/recipe_add.html", {"recipe_form": RecipeForm()})
