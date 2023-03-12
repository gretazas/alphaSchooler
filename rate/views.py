from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from profiles.models import UserProfile
from rate.models import Rating
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
    member = request.user
    product_id = request.POST.get('product_id')
    try:
        product_rate = int(request.POST.get(['rate'][0]))

        if product_rate > 0:
            # ratings = Rating.objects.all().filter(rate_id=product_id)
            # print('ratings:', ratings, '/')
            # rating_total = 0
            # if ratings:
            # # Get this rate_amount sum and add saved this product product_rate:
            ratings = Rating.objects.all().filter(rate_id=product_id)
            print('ratings:', ratings, '/')
            #     for rating in ratings:
            #         rating_total += rating
            # else:
            rating_total = 0
            rate_qnt = 0
            print('First rate', rating_total)
            print('Total rating:', rating_total)
            # rating_total += product_rate
    except:
        pass
    

            # ratings.rate_qnt += 1
    # product.save()
    # Get average:
    # avg_rating = round(rating_total / ratings.rate_qnt)
    # product.rating = avg_rating
  
    # if request.method == "POST":
    # ratings.rate_amount = int(ratings.rate_amount) + int(product_rate)
    # Product.objects.get(id=product_id)
    # Rating.objects.create(rate_id=product_id, rate_qnt=ratings.rate_qnt, rate_amount=ratings.rate_amount, member=member, date=datetime.today())
    # messages.info(request, 'Rated successfully!')
    # if request.user in ratings.member:
    #     messages.error(request, 'You can\'t review product twice')
    #     return redirect(request, 'products/product_detail.html', {'product': product})
    return render(request, 'rate/rate.html', {'product': product, 'on_ratings_page': True})

