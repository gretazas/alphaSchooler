from django.shortcuts import render
from products.models import Product
import datetime
from datetime import date


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
    user = request.user
    year = date.today().year
    today = datetime.date.today()
    dated_message = '/'

    xmas = datetime.datetime(year, 12, 1)
    no_event = datetime.datetime(year, 1, 6)
    valentines = datetime.datetime(year, 2, 7)
    no_event1 = datetime.datetime(year, 2, 15)
    Patricks = datetime.datetime(year, 3, 10)
    no_event2 = datetime.datetime(year, 3, 18)
    if year == 2023:
        Mothers = datetime.datetime(2023, 3, 18)
        no_event3 = datetime.datetime(2023, 3, 20)
        Easter = datetime.datetime(2023, 4, 4)
        no_event4 = datetime.datetime(2023, 4, 10)
    if year == 2024:
        Mothers = datetime.datetime(2024, 3, 8)
        no_event3 = datetime.datetime(2024, 3, 11)
        Easter = datetime.datetime(2024, 3, 20)
        no_event4 = datetime.datetime(2024, 4, 1)

    back_to_school = datetime.datetime(year, 8, 10)
    no_event5 = datetime.datetime(year, 9, 15)
    heloween = datetime.datetime(year, 9, 22)
    no_event6 = datetime.datetime(year, 11, 1)

    if xmas.date() < today:
        if request.user.is_authenticated:
            dated_message = f'Happy Christmas dear {user.username.capitalize()} !!!'
        else:
            dated_message = f'Happy Christmas dear cotumer!!! '
    if no_event.date() < today:
        dated_message = f'Welcome to alphaSchooler! '
    if valentines.date() < today:
        if request.user.is_authenticated:
            dated_message = f'Happy Valentine`s day dear {user.username.capitalize()} !!!'
        else:
            dated_message = f'Happy Valentine`s day dear cotumer!!! '
    if no_event1.date() < today:
        dated_message = f'Welcome to alphaSchooler! '
    if Patricks.date() < today:
        if request.user.is_authenticated:
            dated_message = f'Happy Patrick`s day dear {user.username.capitalize()} !!!'
        else:
            dated_message = f'Happy Patrick`s day dear cotumer!!! '
    if no_event2.date() < today:
        dated_message = f'Welcome to alphaSchooler! '
    if Mothers.date() < today:
        dated_message = f'Happy Mother`s day! '
    if no_event3.date() < today:
        dated_message = f'Welcome to alphaSchooler! '
    if Easter.date() < today:
        if request.user.is_authenticated:
            dated_message = f'Happy Easter dear {user.username.capitalize()} !!!'
        else:
            dated_message = f'Happy Easter dear cotumer!!! '
    if no_event4.date() < today:
        dated_message = f'Welcome to alphaSchooler! '
    if back_to_school.date() < today:
        dated_message = f'Welcome to alphaSchooler! Back to school!!! '
    if no_event5.date() < today:
        dated_message = f'Welcome to alphaSchooler! '
    if heloween.date() < today:
        if request.user.is_authenticated:
            dated_message = f'Happy Heloween dear {user.username.capitalize()} !!!'
        else:
            dated_message = f'Happy heloween dear cotumer!!! '
    if no_event6.date() < today:
        dated_message = f'Welcome to alphaSchooler! '

    context = {
        'current_categories': categories,
        'products': products,
        'dated_message': dated_message
    }

    return render(request, 'home/index.html', context)
