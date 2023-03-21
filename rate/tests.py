from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from products.models import Product, Category
from .models import Rating


class GetRatingViewTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(category=self.category, name='Test Product')
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.rating = Rating.objects.create(user=self.user, product=self.product, value=3)

    def test_get_rating_view_with_valid_data(self):
        self.product = Product.objects.create(
            category=self.category,
            name='Test Product',
            price=10.00  # Replace 10.0 with the actual price value
        )

        self.client.force_login(self.user)
        response = self.client.get(reverse('get-rating', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)