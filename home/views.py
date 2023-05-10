from django.shortcuts import render
from products.models import Product
import datetime
from datetime import date


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    categories = None
    today = datetime.date(2023, 12, 15)
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    # Add a dictionary mapping event dates to messages
    event_messages = {
        datetime.datetime(date.today().year, 12, 1).date(): "Happy Christmas dear {username} !!!",
        datetime.datetime(date.today().year, 1, 6).date(): "Welcome to alphaSchooler!",
        datetime.datetime(date.today().year, 2, 7).date(): "Happy Valentine`s day dear {username} !!!",
        datetime.datetime(date.today().year, 2, 15).date(): "Welcome to alphaSchooler!",
        datetime.datetime(date.today().year, 3, 10).date(): "Happy Patrick`s day dear {username} !!!",
        datetime.datetime(date.today().year, 3, 18).date(): "Welcome to alphaSchooler!",
        datetime.datetime(2023, 3, 18).date(): "Happy Mother`s day!",
        datetime.datetime(2023, 3, 20).date(): "Welcome to alphaSchooler!",
        datetime.datetime(2023, 4, 4).date(): "Happy Easter dear {username} !!!",
        datetime.datetime(2023, 4, 10).date(): "Welcome to alphaSchooler!",
        datetime.datetime(2024, 3, 8).date(): "Happy Mother`s day!",
        datetime.datetime(2024, 3, 11).date(): "Welcome to alphaSchooler!",
        datetime.datetime(2024, 3, 20).date(): "Happy Easter dear {username} !!!",
        datetime.datetime(2024, 4, 1).date(): "Welcome to alphaSchooler!",
        datetime.datetime(date.today().year, 8, 10).date(): "Welcome to alphaSchooler! Back to school!!!",
        datetime.datetime(date.today().year, 9, 15).date(): "Welcome to alphaSchooler!",
        datetime.datetime(date.today().year, 9, 22).date(): "Happy Heloween dear {username} !!!",
        datetime.datetime(date.today().year, 11, 1).date(): "Welcome to alphaSchooler!",
    }

    # Get the message for the current date, and substitute the username if user is authenticated
    message = event_messages.get(date.today(), "Welcome to alphaSchooler!")
    if request.user.is_authenticated:
        message = message.format(username=request.user.username.capitalize())
    print(today)  # Here we print the value of today using the print() function
    context = {
        'current_categories': categories,
        'products': products,
        'dated_message': message
    }

    return render(request, 'home/index.html', context)