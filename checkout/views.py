from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem

from products.models import Product
from bag.contexts import bag_contents
import stripe
import json


def checkout(request):
    ''' Render checkout page '''

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})

    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = OrderForm()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MOKnEGn2B9VBfJ8LBqpyeJl7RaHR45CoYUpc9Iyv5gwQ2YxGoHoh9DZuTjfVjuXl1Uqkv06DeNgRzkgDbuBS3XD00WHNOWlIC',
        'client_secret': intent.client_secret,
        }

    return render(request, template, context)
