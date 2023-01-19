from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ Add placeholders, remove auto-generated
        labels and set autofocus """
        super().__init__(*args, **kwargs)
        placeholders = {
            'saved_phone_number': 'Phone Number',
            'saved_postcode': 'Postal Code',
            'saved_town_or_city': 'Town or City',
            'saved_street_address1': 'Street Address 1',
            'saved_street_address2': 'Street Address 2',
            'saved_county': 'County, State or Locality',
        }

        self.fields['saved_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'saved_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black profile-form-input'
            self.fields[field].label = False
