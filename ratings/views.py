from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from ratings.models import Rating
from products.models import Product
from django.db.models import Avg
from .forms import RatingForm
from django.contrib import messages
from datetime import datetime


def get_rating(request, product_id):
    model = Rating
    template_name = "rate.html"
    product = get_object_or_404(Product, pk=product_id)
    member = request.user
    date = datetime.today()
    product_id = request.POST.get('product_id')
    product_rate = request.POST.get('rate')
    member = request.user
    if request.method == "POST":
        ratings = Rating.objects.all()
        # If rater does not exist yet:
        if Rating(rate_id=None):
            ratings.rate_id = product_id
            ratings.rate_amount = 0
            ratings.rate_qnt = 0
        ratings = Rating.objects.all().filter(rate_id=product_id).first()
        # Get rate_amount and add prev saved amount
        ratings.rate_amount = int(ratings.rate_amount) + int(product_rate)
        ratings.rate_qnt = ratings.rate_qnt + 1
        # Get average
        avg_rating = ratings.rate_amount / ratings.rate_qnt
        Product.objects.get(id=product_id)
        product.rating = avg_rating
        product.save()

        print(ratings.rate_qnt)
        print(ratings.rate_amount)
        Rating(rate_id=product_id, rate_qnt=ratings.rate_qnt, rate_amount=ratings.rate_amount, member=member, date=datetime.today()).objects.create()
        messages.info(request, 'Rated successfully!')
    # if request.user in ratings.member:
    #     messages.error(request, 'You can\'t review product twice')
    #     return redirect(request, 'products/product_detail.html', {'product': product})
    return render(request, 'ratings/rate.html', {'product': product})
