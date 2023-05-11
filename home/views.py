from django.shortcuts import render
from products.models import Product
import datetime
from datetime import date


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    categories = None
    username = request.user
    dated_message = ''
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    current_date = date.today()

    if request.user.is_authenticated:
        username = request.user.username.capitalize()
    else:
        username = 'Guest'

    if current_date.month == 12 and current_date.day >= 1 or current_date.month == 1 and current_date.day <= 6:
        message = f"Happy Christmas dear {username} !!!"
    elif current_date.month == 2 and current_date.day >= 7 and current_date.day <= 15:
        message = f"Happy Valentine's day dear {username} !!!"
    elif current_date.month == 3 and current_date.day >= 10 and current_date.day <= 18:
        message = f"Happy Patrick's day dear {username} !!!"
    elif current_date.month == 3 and current_date.day >= 18 and current_date.day <= 20:
        message = f"Happy Mother's day!"
    elif current_date.month == 4 and current_date.day >= 4 and current_date.day <= 10:
        message = f"Happy Easter dear {username} !!!"
    elif current_date.month == 8 and current_date.day >= 10 or current_date.month == 9 and current_date.day <= 15:
        message = f"Welcome to alphaSchooler! Back to school!!!"
    elif current_date.month == 9 and current_date.day >= 22 or current_date.month == 11 and current_date.day <= 1:
        message = f"Happy Heloween dear {username} !!!"
    else:
        message = f"Welcome to alphaSchooler dear {username} !"

    context = {
        'current_categories': categories,
        'products': products,
        'dated_message': message
    }

    return render(request, 'home/index.html', context)