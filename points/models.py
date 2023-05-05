from django.db import models
from django.contrib.auth.models import User


class Points(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    points = models.FloatField(default=0.00)
    date = models.DateField(auto_now_add=True)

