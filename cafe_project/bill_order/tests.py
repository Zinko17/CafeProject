from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from content.models import Meal,Category
from .models import *


class TestOrder(TestCase):

    def setUp(self) -> None:
        self.url = reverse('order')


    def test_order_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)



class TestOrderPost(TestCase):

    def setUp(self) -> None:
        self.url = reverse('order')
        self.category = Category.objects.create(title='dfsfs')
        self.meal = Meal.objects.create(ingredients='f', title='fdf', price=200, gramms=200, category=self.category)

    def test_order_post(self):

        data = {
            'meal':self.meal,
            'quantity':1
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, 200)



class CloseCheckGetTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='fdsf',password='dfdsflskcms')
        self.order = Order.objects.create(user=self.user)
        self.url = reverse('close_check', args=(self.order.id,))

    def test_closecheck_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)


class CheckDetailTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='fdsf', password='dfdsflskcms')
        self.order = Order.objects.create(user=self.user)
        check = Bill.objects.create(order=self.order)
        Bill.objects.get(order__id=self.order.id)
        self.url = reverse('check_detail', args=(self.order.id,))

    def test_check_detail_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)



class MealDetailTest(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(title='dfsfs')
        self.meal = Meal.objects.create(ingredients='f', title='fdf', price=200, gramms=200, category=self.category)
        self.url = reverse('meal_detail', args=(self.meal.id,))

    def test_meal_detail_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)



class MealDetailTestPost(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(title='dfsfs')
        self.meal = Meal.objects.create(ingredients='f', title='fdf', price=200, gramms=200, category=self.category)
        self.url = reverse('meal_detail', args=(self.meal.id,))

    def test_meal_detail_post(self):
        data = {'text':'fdsfsdfsdg'}
        User.objects.create_user(username='safad',password='sfasfds')
        self.client.login(username='safad',password='sfasfds')
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code, 200)