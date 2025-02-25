from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    quantity = models.PositiveIntegerField()
    ingredient = models.ForeignKey(Ingredient, on_delete=models.SET_NULL)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
