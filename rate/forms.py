from django import forms
from products.models import Product
from rate.models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = '__all__'
