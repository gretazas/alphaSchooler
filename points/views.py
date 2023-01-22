from django.shortcuts import render, redirect
from .forms import PointsForm
from django.contrib import messages
from points.models import Points
from datetime import datetime
from django.contrib.auth.models import User
from bag.contexts import bag_contents
from checkout.forms import OrderForm
from profiles.models import UserProfile
from checkout.models import Order, OrderLineItem


def points(request):
    ''' View that renders poits.html '''
    user = request.user
    date = datetime.today()
    userpoints = Points.objects.all()
    form = PointsForm()
    if Points(points=None):
        userpoints.points = 0
    current_bag = bag_contents(request)
    total = current_bag['grand_total']

    userpoints.points = total # Delete after test

    if userpoints.points < total:
        redirect_url = request.POST.get('redirect_url')
        messages.error(request, f'Sorry, no efficient points for this transaction.')
        return redirect(redirect_url)

    if request.method == 'POST':
        bag = request.session.get('bag', {})
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'country': request.POST['country'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.original_bag = json.dumps(bag)
            order.save()
            for item_id, item_data in bag.items():
                try:
                    product = Product.objects.get(id=item_id)   
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )
                    order_line_item.save()

                except Product.DoesNotExist:
                    messages.error(request, (
                        "Some products in your bag wasn't found in our system."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            request.session['save_info'] = 'save_info' in request.POST
            form = PointsForm()
            current_bag = bag_contents(request)
            total = current_bag['grand_total']
            userpoints.points = userpoints.points - total
            if form.is_valid():
                form.save()
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            print(order_form.cleaned_data)
            print(order_form.errors)
            messages.error(request, 'Something went wrong with your form.\
                Please double check your information.')
            redirect_url = request.POST.get('redirect_url')
            return redirect(redirect_url)
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "Your bag is empty")
            return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    total = round(total * 100)

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order_form = OrderForm(initial={
                'full_name': profile.user.get_full_name(),
                'email': profile.user.email,
                'phone_number': profile.saved_phone_number,
                'country': profile.saved_country,
                'postcode': profile.saved_postcode,
                'town_or_city': profile.saved_town_or_city,
                'street_address1': profile.saved_street_address1,
                'street_address2': profile.saved_street_address2,
                'county': profile.saved_county,
            })
        except UserProfile.DoesNotExist:
            order_form = OrderForm()
    else:
        order_form = OrderForm()

    current_bag = bag_contents(request)
    total = current_bag['grand_total']

    template = 'points/points_checkout.html'
    context = {
        'order_form': order_form,
        'on_points_page': True
        }
    return render(request, template, context)
