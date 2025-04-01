from django.urls import path

from ledger import views

urlpatterns = [
    path("recipes/list", views.index),
    path("recipe/<int:recipe_id>", views.recipe_detail, name="detail"),
    path("recipe/add", views.recipe_add, name="recipe_add"),
]
