from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm


class ProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            full_name='Test User',
            address='Test Address',
            phone_number='1234567890'
        )

    def test_profile_view_GET(self):
        """
        Test that the profile view renders the correct template with the correct context
        when accessed with GET request
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, 'Test User')
        self.assertContains(response, 'Test Address')
        self.assertContains(response, '1234567890')

    def test_profile_view_POST(self):
        """
        Test that the profile view updates the user profile when accessed with POST request
        """
        self.client.login(username='testuser', password='testpassword')
        form_data = {
            'full_name': 'New Test User',
            'address': 'New Test Address',
            'phone_number': '0987654321'
        }
        response = self.client.post(reverse('profile'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        updated_user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_user_profile.full_name, 'New Test User')
        self.assertEqual(updated_user_profile.address, 'New Test Address')
        self.assertEqual(updated_user_profile.phone_number, '0987654321')
        self.assertContains(response, 'Your profile updated successfully')

class OrderHistoryViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.order = Order.objects.create(
            user=self.user,
            order_number='123456',
            total=10.0
        )

    def test_order_history_view(self):
        """
        Test that the order history view renders the correct template with the correct context
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('order_history', args=[self.order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')
        self.assertContains(response, f'This is a past confirmation for order number {self.order.order_number}')
        self.assertContains(response, 'Order Total: $10.00')