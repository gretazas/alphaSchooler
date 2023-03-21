from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm


def test_all_products_view_returns_products_on_get_request_without_filters(client):
    response = client.get(reverse('products'))
    assert response.status_code == 200
    assert len(response.context['products']) == Product.objects.all().count()

# Check if all_products view returns products filtered by category on GET request:

def test_all_products_view_returns_products_filtered_by_category_on_get_request(client):
    category = Category.objects.first()
    product = Product.objects.filter(category=category).first()
    response = client.get(reverse('products'), {'category': category.name})
    assert response.status_code == 200
    assert len(response.context['products']) == Product.objects.filter(category=category).count()
    assert product in response.context['products']

# Check if all_products view returns products sorted by name on GET request:

def test_all_products_view_returns_products_sorted_by_name_on_get_request(client):
    response = client.get(reverse('products'), {'sort': 'name'})
    assert response.status_code == 200
    products = Product.objects.order_by('name')
    assert list(response.context['products']) == list(products)

# Check if all_products view returns products sorted by category on GET request:

def test_all_products_view_returns_products_sorted_by_category_on_get_request(client):
    response = client.get(reverse('products'), {'sort': 'category'})
    assert response.status_code == 200
    products = Product.objects.order_by('category__name', 'name')
    assert list(response.context['products']) == list(products)

# Check if all_products view returns products filtered by search term on GET request:

def test_all_products_view_returns_products_filtered_by_search_term_on_get_request(client):
    product = Product.objects.first()
    response = client.get(reverse('products'), {'q': product.name})
    assert response.status_code == 200
    assert len(response.context['products']) == Product.objects.filter(name__icontains=product.name).count()
    assert product in response.context['products']

# Check if product_detail view returns product on GET request:

def test_product_detail_view_returns_product_on_get_request(client):
    product = Product.objects.first()
    response = client.get(reverse('product_detail', args=[product.id]))
    assert response.status_code == 200
    assert response.context['product'] == product

# Check if add_product view adds product to database on POST request:

def test_add_product_view_adds_product_to_database_on_post_request(client, admin_user):
    client.force_login(admin_user)
    form_data = {
        'name': 'Test Product',
        'description': 'Test description',
        'category': Category.objects.first().id,
        'price': 9.99,
        'image': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
    }
    response = client.post(reverse('add_product'), form_data, follow=True)
    assert response.status_code == 200
    assert Product.objects.filter(name=form_data['name']).exists()

# Check if edit_product view updates product in database on POST request:

def test_edit_product_view_updates_product_in_database_on_post_request(client, admin_user):
    client.force_login(admin_user)
    product = Product.objects.first()
    form_data = {
        'name': 'Updated Product Name',
        'description': product.description,
    }

