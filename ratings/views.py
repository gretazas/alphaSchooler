from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from ratings.models import Rating
from products.models import Product
from django.db.models import Avg
from django.views import generic
from .forms import RatingForm
from django.contrib import messages


def get_rating(request, product_id):
    model = Rating
    template_name = "rate.html"
    product = get_object_or_404(Product, pk=product_id)
    
    # rate = request.POST.get('rate')
    # member = request.user
    # print(rate)
    # rate = Product.rating

    if request.method == "POST":
        print(request)
        product_id = request.POST.get('product_id')
        print(product_id)
        
        # user = request.user
        
        # rate = Product.rating
        # messages.info(request, 'Rated successfully!')
        # Rating(user=user, product=product, rate=rate).save()
    rate = request.GET.get('rate')
    print(rate)
    return render(request, 'ratings/rate.html', {'product': product, 'rate': rate})
