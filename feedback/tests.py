from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.test import TestCase, Client
from .forms import FeedbackForm


class FeedbackFormTestCase(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.url = '/feedback/'

#     def test_valid_submission(self):
#         # Arrange
#         data = {
#             'name': 'John Doe',
#             'email': 'johndoe@example.com',
#             'message': 'This is a test feedback message',
#         }
#         form = FeedbackForm(data)
#         # Act
#         response = self.client.post(self.url, data)
#         # Assert
#         self.assertRedirects(response, 'feedback/')
#         self.assertTrue(form.is_valid())

# # Test an invalid submission of the feedback form

#     def test_invalid_submission(self):
#         # Arrange
#         data = {
#             'name': '',
#             'email': 'johndoe@example.com',
#             'message': '',
#         }
#         form = FeedbackForm(data)
#         # Act
#         response = self.client.post(self.url, data)
#         # Assert
#         self.assertEqual(response.status_code, 200)
#         self.assertFalse(form.is_valid())

# # Test GET request to the feedback page

#     def test_get_feedback_page(self):
#         # Act
#         response = self.client.get(self.url)
#         # Assert
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'feedback/feedback.html')

# Test GET request to the contact page

    # def test_get_contact_page(self):
    #     # Act
    #     response = self.client.get(self.url)
    #     # Assert
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'feedback/contact.html')
