from ledger import views
from django.urls import path

urlpatterns = [
    path("recipes/list", views.index),
    path("recipe/<int:recipe_id>", views.recipe_detail, name="detail"),
]
