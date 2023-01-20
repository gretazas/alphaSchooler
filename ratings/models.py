from django.db import models
from profiles.models import UserProfile
import products.models
from django.utils import timezone
from django.contrib.auth.models import User


class Rating(models.Model):

    def __str__(self):
        return str(self.id)

    rate_amount = models.IntegerField(null=True, blank=True)
    rate_qnt = models.PositiveSmallIntegerField(null=True, blank=True)
    rate_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    member = models.OneToOneField(User, on_delete=models.CASCADE)
