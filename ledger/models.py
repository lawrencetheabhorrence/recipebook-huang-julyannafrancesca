from django.db import models
from django.urls import reverse

from user.models import Profile


class Ingredient(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=250, unique=True)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    createdon = models.DateField(auto_now_add=True)
    updatedon = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=250)
    ingredient = models.ForeignKey(
        Ingredient,
        null=True,
        on_delete=models.SET_NULL,
        related_name="ingredient",
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe")

    def __str__(self):
        return f"{self.recipe}: {self.ingredient}, {self.quantity}"


class RecipeImage(models.Model):
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/")
    description = models.CharField(max_length=255)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe_image"
    )
