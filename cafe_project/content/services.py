from .models import *


def category_link(category,meal):
    for c in category:
        meal = c.meal_set.all()
