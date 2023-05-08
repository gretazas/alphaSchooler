from django.db import models
from rate.models import Rating


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    presentable_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_presentable_name(self):
        return self.presentable_name


class Product(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    sku = models.CharField(max_length=254, null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.CharField(max_length=254, null=True, blank=True, default=0.0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    pencil_softness = models.BooleanField(default=False, null=True, blank=True)
    folder_sizes = models.BooleanField(default=False, null=True, blank=True)
    lunch_box = models.BooleanField(default=False, null=True, blank=True)
    pencil_case = models.BooleanField(default=False, null=True, blank=True)
    copies = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
