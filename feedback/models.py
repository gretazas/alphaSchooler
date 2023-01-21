from django.db import models


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    details = models.TextField()
    happy = models.BooleanField(null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
