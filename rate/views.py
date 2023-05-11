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
    form = RatingForm()
    member = request.user
    product = get_object_or_404(Product, pk=product_id)
    product_id = request.POST.get('product_id')
    ratings = Rating.objects.all().filter(rate_id=product_id)
    same_member = Rating.objects.all().filter(rate_id=product_id, member=member)

    if same_member:
        messages.info(request, 'You have already rated this product.')
    else:
        # Get to the point where i get a rate as a number, not NoneType
        try:
            product_rate = int(request.POST.get(['rate'][0]))
            if product_rate > 0:
                # Get info from database
                if ratings:
                    # Get rate_amount sum and add product_rate:
                    rate_amount_list = []
                    for rate, x in enumerate(ratings):
                        rating = ratings[rate].rate_amount
                        rate_amount_list.append(rating)
                        rating_total = sum(rate_amount_list)
                    ratings_qnt_list = []
                    # Get quantity of all rates:
                    for qnt, y in enumerate(ratings):
                        raters = ratings[qnt].rate_qnt
                        ratings_qnt_list.append(raters)
                        raters_total = sum(ratings_qnt_list) 
                # If not in database = first rate:
                else:
                    rating_total = 0
                    raters_total = 0
                rating_total += product_rate
                raters_total += 1
                if request.method == 'POST':
                    data = {
                            'rate_id': product_id,
                            'rate_qnt': raters_total,
                            'rate_amount': int(request.POST['rate'][0]),
                            'member': request.user.id,
                        }
                    form = RatingForm(data)
                    if form.is_valid():
                        form.save()
                        # Get average and save:
                        avg_rating = round(rating_total / raters_total)
                        products = Product.objects.all().filter(id=product_id)
                        messages.info(request, 'Rated successfully!')
                        for product in products:
                            product.rating = avg_rating
                            product.save()
                            # Serialize updated products and save to file
                            serialized_products = serializers.serialize('json', products)
                            with open('products/fixtures/products.json', 'w') as f:
                                f.write(serialized_products)
                        
                        return render(request, 'rate/rate.html', {'product': product, 'on_ratings_page': True, 'form': form})
                    else:
                        messages.info(request, 'Sorry, something went wrong.')
                        
        except:
            pass
    return render(request, 'rate/rate.html', {'product': product, 'on_ratings_page': True, 'form':form})
