from django.test import TestCase
from django.urls import reverse
from .models import *

class MealTest(TestCase):

    def setUp(self) -> None:
        self.url = reverse('meals')
        self.category = Category.objects.create(title='fsdfdsf')
        Meal.objects.create(title='sfaff',price=100,gramms=100,ingredients='fafdfs',category=self.category)


    def test_meal_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)



class CategoryTest(TestCase):

    def setUp(self) -> None:
        self.url = reverse('home')
        Category.objects.create(title='dfsdfsf')


    def test_category_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)