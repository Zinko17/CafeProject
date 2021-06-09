from django.test import TestCase
from django.urls import reverse


class TestOrder(TestCase):

    def setUp(self) -> None:
        self.url = reverse('order')


    def test_order_get(self):
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)
