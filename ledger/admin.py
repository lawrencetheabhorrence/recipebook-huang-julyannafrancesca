from django.contrib import admin

from .models import Ingredient, Recipe, RecipeIngredient


class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ["recipe", "ingredient", "quantity"]
    list_filter = ["recipe", "ingredient"]


# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
