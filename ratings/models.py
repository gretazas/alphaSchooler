from django.db import models
from profiles.models import UserProfile
import products.models
from django.utils import timezone


class Rating(models.Model):

    def __str__(self):
        return str(self.id)

    rate_id = models.CharField(max_length=10, null=True, blank=True)
    member = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='member')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='product', default=False)
    date = models.DateTimeField(default=timezone.now)
    rate = models.PositiveSmallIntegerField(null=True, blank=True)

    def ratings(self):
        return Product.objects.filter(pk=product_id).aggregate(Avg("rating__rate"))
