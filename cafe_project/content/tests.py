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


class RegisterTest(TestCase):

    def setUp(self) -> None:
        self.url = reverse('register')


    def test_register_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code,200)




class LoginTest(TestCase):

    def setUp(self) -> None:
        self.url = reverse('login')


    def test_login_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)


class RegisterTestPost(TestCase):

    def setUp(self) -> None:
        self.url = reverse('register')
        data = {'name':'name',
                'age':10,
                'email':'vvv@gmail.com',
                'username':'zzz',
                'password1':'123456',
                'password2':'123456',
        }


    def test_register_post(self):
        data = {'name': 'name',
                'age': 10,
                'email': 'vvv@gmail.com',
                'username': 'zzz',
                'password1': '123456',
                'password2': '123456',
                }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code, 200)