from django.urls import path

from ledger import views

urlpatterns = [
    path("recipes/list", views.index),
    path("recipe/<int:recipe_id>", views.recipe_detail, name="detail"),
    path(
        "recipe/<int:recipe_id>/ingredient/add",
        views.recipeingredient_add,
        name="recipeingredient_add",
    ),
    path("ingredient/add", views.ingredient_add, name="ingredient_add"),
    path("recipe/add", views.recipe_add, name="recipe_add"),
]
