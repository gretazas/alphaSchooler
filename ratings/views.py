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
    print(Rating.rate_amount)
    # ratings = Rating.objects.all().filter(rate_id=product_id)
    # if ratings:
    #     print('ratings')
    #     # If rater does not exist yet:
    # else:
    #     print('not ratings')
            # Rating.rate_id = product_id
            # Rating.rate_amount = 0
            # Rating.rate_qnt = 0
            # print(Rating.rate_id)
        
        # if request.method == "POST":
        
        # 
        # # Get rate_amount and add prev saved amount
        # ratings.rate_amount = int(ratings.rate_amount) + int(product_rate)
        # ratings.rate_qnt = ratings.rate_qnt + 1
        # # Get average
        # avg_rating = ratings.rate_amount / ratings.rate_qnt
        # Product.objects.get(id=product_id)
        # product.rating = avg_rating
        # product.save()

        # print(ratings.rate_qnt)
        # print(ratings.rate_amount)
        # Rating.objects.create(rate_id=product_id, rate_qnt=ratings.rate_qnt, rate_amount=ratings.rate_amount, member=member, date=datetime.today())
        # messages.info(request, 'Rated successfully!')
    # if request.user in ratings.member:
    #     messages.error(request, 'You can\'t review product twice')
    #     return redirect(request, 'products/product_detail.html', {'product': product})
    return render(request, 'ratings/rate.html', {'product': product, 'on_ratings_page': True})
