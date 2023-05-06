from django.db import models

from django.db import models
from profiles.models import UserProfile
import products.models
from django.utils import timezone
from django.contrib.auth.models import User


class Rating(models.Model):
    rate_amount = models.IntegerField(null=True, blank=True, default=0)
    rate_qnt = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    rate_id = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    member = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


