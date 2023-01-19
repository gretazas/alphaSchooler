from django import forms
from products.models import Product
from ratings.models import Rating


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = '__all__'
