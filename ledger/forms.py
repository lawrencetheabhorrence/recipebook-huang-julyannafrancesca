from django.forms import ModelForm
from .models import Recipe, RecipeIngredient, Ingredient


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "author"]


class RecipeIngredientForm(ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ["ingredient", "quantity"]


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]
