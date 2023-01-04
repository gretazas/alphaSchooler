from decimal import Decimal
from django.conf import settings


def bag_contents(request):
    """ View that renders bag contents """

    bag_items = []
    total = 0
    product_count = 0
    collected_points = 0

# Delivery
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimil(settings.STANDART_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD * total
    else:
        dekivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

# Points
    if use_points:
        collected_money = collected_points_total * settings.ONE_PERCENT
        total = total - collected_money

        # For unused points
        if total < 0:
            collected_points_total = total * 2
        else:
            collected_points_total = collected_points_total - total
    else:
        collected_points_total = collected_points_total + total


    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'collected_points': collected_points,
        'collected_points_total': settings.COLLECTED_POINTS,

    }
    return context