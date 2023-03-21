from django.test import TestCase, Client
from django.urls import reverse
from products.models import Category, Product
import datetime


class TestIndexView(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')
        self.product1 = Product.objects.create(name='Product 1', price=10, category=self.category1)
        self.product2 = Product.objects.create(name='Product 2', price=20, category=self.category2)

    def test_index_view_without_filter(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertQuerysetEqual(response.context['products'], [repr(self.product1), repr(self.product2)])
        self.assertIsNone(response.context['current_categories'])
        self.assertIsInstance(response.context['dated_message'], str)

    def test_index_view_with_category_filter(self):
        url = f'{self.url}?category={self.category1.id}'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertQuerysetEqual(response.context['products'], [repr(self.product1)])
        self.assertQuerysetEqual(response.context['current_categories'], [repr(self.category1)])
        self.assertIsInstance(response.context['dated_message'], str)

    def test_index_view_with_invalid_category_filter(self):
        url = f'{self.url}?category=invalid'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertQuerysetEqual(response.context['products'], [repr(self.product1), repr(self.product2)])
        self.assertIsNone(response.context['current_categories'])
        self.assertIsInstance(response.context['dated_message'], str)

    def test_index_view_with_dated_message(self):
        year = datetime.datetime.now().year
        xmas = datetime.datetime(year, 12, 1).date()
        self.assertEqual(xmas < datetime.date.today(), True)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertIsInstance(response.context['dated_message'], str)