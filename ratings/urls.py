from . import views
from django.urls import path

urlpatterns = [
    path('rating/<int:product_id>/', views.get_rating, name='ratings'),
]