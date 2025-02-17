from django.shortcuts import render

ctx = {
    "recipes": [
        {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"},
            ],
            "link": "/recipe/1",
        },
        {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "vinegar", "quantity": "1/2cup"},
                {"name": "water", "quanity": "1 cup"},
                {"name": "salt", "quantity": "1 tablespoon"},
                {"name": "whole black peppers", "quantity": "1 tablespoon"},
                {"name": "pork", "quantity": "1 kilo"},
            ],
            "link": "/recipe/2",
        },
    ]
}


# Create your views here.
def index(request):
    return render(request, "ledger/recipe_list.html", ctx)


def recipe_detail(request, recipe_id):
    recipe_ctx = ctx["recipes"][recipe_id - 1]
    return render(request, "ledger/recipe_detail.html", recipe_ctx)
