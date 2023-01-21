from . import views
from django.urls import path


urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
]
