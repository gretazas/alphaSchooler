from django.test import TestCase
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from bag.contexts import bag_contents
from products.models import Product, Category
from .models import Order

import json


class TestCheckoutViews(TestCase):

    def setUp(self):
        category = Category.objects.create(name='test category')
        self.product = Product.objects.create(name='test product', price=10, category=category)
        self.checkout_url = reverse('checkout')

    # def test_checkout_page_loads(self):
    #     response = self.client.get(self.checkout_url)
    #     self.assertEqual(response.status_code, 200)

    def test_checkout_post_saves_order(self):
        # Add product to bag
        STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
        STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
        bag = {'1': 1}
        self.client.post(reverse('add_to_bag', args=[self.product.id]), {'quantity': 1, 'redirect_url': '/'})
        response = self.client.post(self.checkout_url, {
            'full_name': 'Test User',
            'email': 'testuser@example.com',
            'phone_number': '0123456789',
            'country': 'Test Country',
            'postcode': 'AB1 2CD',
            'town_or_city': 'Test Town',
            'street_address1': 'Test Address 1',
            'street_address2': 'Test Address 2',
            'county': 'Test County',
            'client_secret': 'test_secret_123'
        })
        self.assertRedirects(response, reverse('checkout_success', args=['00000001']))
        order = Order.objects.get(order_number='00000001')
        self.assertEqual(order.full_name, 'Test User')
        self.assertEqual(order.email, 'testuser@example.com')
        self.assertEqual(order.phone_number, '0123456789')
        self.assertEqual(order.country, 'Test Country')
        self.assertEqual(order.postcode, 'AB1 2CD')
        self.assertEqual(order.town_or_city, 'Test Town')
        self.assertEqual(order.street_address1, 'Test Address 1')
        self.assertEqual(order.street_address2, 'Test Address 2')
        self.assertEqual(order.county, 'Test County')
        self.assertEqual(order.original_bag, json.dumps(bag))
        self.assertEqual(order.stripe_pid, 'test_secret_123')

    # def test_checkout_post_redirects_if_bag_empty(self):
    #     response = self.client.post(self.checkout, {
    #         'full_name': 'Test User',
    #         'email': 'testuser@example.com',
    #         'phone_number': '0123456789',
    #         'country': 'Test Country',
    #         'postcode': 'AB1 2CD',
    #         'town_or_city': 'Test Town',
    #         'street_address1': 'Test Address 1',
    #         'street_address2': 'Test Address 2',
    #         'county': 'Test County',
    #         'client_secret': 'test_secret_123'
    #     })
    #     self.assertRedirects(response, reverse('products'))

    def test_checkout_success_page_loads(self):
        order = Order.objects.create(
            full_name='Test User',
            email='testuser@example.com',
            phone_number='0123456789',
            country='ireland',
        )

