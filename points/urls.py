from django.urls import path
from . import views


urlpatterns = [
    path('points/', views.points, name='points'),
]