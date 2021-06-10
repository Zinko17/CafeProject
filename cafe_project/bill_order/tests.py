from django.test import TestCase
from django.urls import reverse
from content.models import Meal,Category


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



