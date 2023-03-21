from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings

from products.models import Product
from checkout.models import Order

import json

# Add a product to the bag
def test_add_to_bag(self):
    # Create a product
    product = Product.objects.create(name='Test Product', price=10.00)

    # Simulate a request to add the product to the bag
    response = self.client.post(reverse('add_to_bag', args=[product.id]), {
        'quantity': 2,
        'redirect_url': reverse('home')
    })

    # Check that the product was added to the bag
    self.assertEqual(response.status_code, 302)
    self.assertEqual(len(self.client.session['bag']), 1)
    self.assertEqual(self.client.session['bag'][str(product.id)], 2)


# Adjust the quantity of a product in the bag
def test_adjust_bag(self):
    # Create a product and add it to the bag
    product = Product.objects.create(name='Test Product', price=10.00)
    self.client.post(reverse('add_to_bag', args=[product.id]), {
        'quantity': 2,
        'redirect_url': reverse('home')
    })

    # Simulate a request to adjust the quantity of the product in the bag
    response = self.client.post(reverse('adjust_bag', args=[product.id]), {
        'quantity': 3,
    })

    # Check that the quantity was updated in the bag
    self.assertEqual(response.status_code, 302)
    self.assertEqual(len(self.client.session['bag']), 1)
    self.assertEqual(self.client.session['bag'][str(product.id)], 3)


# Remove a product from the bag
def test_remove_from_bag(self):
    # Create a product and add it to the bag
    product = Product.objects.create(name='Test Product', price=10.00)
    self.client.post(reverse('add_to_bag', args=[product.id]), {
        'quantity': 2,
        'redirect_url': reverse('home')
    })

    # Simulate a request to remove the product from the bag
    response = self.client.post(reverse('remove_from_bag', args=[product.id]))

    # Check that the product was removed from the bag
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(self.client.session['bag']), 0)
