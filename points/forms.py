from django import forms
from .models import Points
from checkout.models import Order


class PointsForm(forms.ModelForm):
    class Meta:
        model = Points
        exclude = []
