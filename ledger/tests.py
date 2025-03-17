from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, RecipeIngredient
from user.models import Profile

# Create your tests here.


class AuthorizedViewsTestCase(TestCase):
    def setUp(self):
        testUser = User.objects.create_user(
            username="fakename", email="fakename@email.com", password="pass"
        )
        testProfile = Profile(user=testUser, name="Fake Name", bio="Not a real profile")

        testProfile.save()

        ingredient1 = Ingredient.objects.create(name="egg")
        ingredient2 = Ingredient.objects.create(name="tomato")
        recipe = Recipe.objects.create(name="test recipe", author=testProfile)
        recipe_ingredient1 = RecipeIngredient.objects.create(
            quantity="1 pc", ingredient=ingredient1, recipe=recipe
        )
        recipe_ingredient2 = RecipeIngredient.objects.create(
            quantity="5 pcs", ingredient=ingredient2, recipe=recipe
        )

    def test_recipe_list_unauthorized(self):
        c = Client()
        response = c.get("/recipes/list", follow=True)
        self.assertIn("registration/login.html", response.template_name)

    def test_recipe_detail_unauthorized(self):
        c = Client()
        id = Recipe.objects.get(name="test recipe").pk
        response = c.get("/recipe/" + str(id), follow=True)
        self.assertIn("registration/login.html", response.template_name)

    def test_recipe_list_authorized(self):
        c = Client()
        login_res = c.post(
            "/accounts/login/",
            {"username": "fakename", "password": "pass"},
        )
        self.assertEqual(login_res.url, "/recipes/list")

    def test_recipe_detail_authorized(self):
        c = Client()
        login_res = c.post(
            "/accounts/login/",
            {"username": "fakename", "password": "pass"},
            follow=True,
        )

        id = Recipe.objects.get(name="test recipe").pk
        response = c.get("/recipe/" + str(id), follow=True)
        self.assertEqual(response.status_code, 200)
