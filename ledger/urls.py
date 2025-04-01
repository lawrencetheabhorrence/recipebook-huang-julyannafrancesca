from django.urls import path

from ledger import views

urlpatterns = [
    path("recipes/list", views.index, name="recipe_list"),
    path("recipe/<int:recipe_id>", views.recipe_detail, name="recipe_detail"),
    path(
        "recipe/<int:recipe_id>/add_ingredient",
        views.recipeingredient_add,
        name="recipeingredient_add",
    ),
    path(
        "recipe/<int:recipe_id>/add_image",
        views.recipeimage_add,
        name="recipeimage_add",
    ),
    path("add_ingredient", views.ingredient_add, name="ingredient_add"),
    path("recipe/add", views.recipe_add, name="recipe_add"),
]
