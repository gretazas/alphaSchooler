from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """ Handle webhook events """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
