from . import views
from django.urls import path

urlpatterns = [
    path('<int:product_id>/', views.get_rating, name='rate'),
]