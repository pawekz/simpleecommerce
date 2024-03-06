from django import forms
from django.core.exceptions import ValidationError

from .models import Seller


class SellerForm(forms.ModelForm):
    StallName = forms.CharField(label='Stall Name', max_length=255)
    SellerName = forms.CharField(label='Seller Name', max_length=255)
    ContactNo = forms.IntegerField(label='Contact Number')
    Address = forms.CharField(label='Address', max_length=255)
    Username = forms.CharField(label='Username', max_length=20)
    Password = forms.CharField(label='Password', max_length=128, widget=forms.PasswordInput)
    ConfirmPassword = forms.CharField(label='Confirm Password', max_length=128, widget=forms.PasswordInput)

    class Meta:
        model = Seller
        fields = ['StallName', 'SellerName', 'ContactNo', 'Address', 'Username', 'Password', 'ConfirmPassword']
        widgets = {
            'Password': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('Password')
        confirm_password = cleaned_data.get('ConfirmPassword')

        if password and confirm_password:
            if password != confirm_password:
                raise ValidationError("Password and Confirm Password fields do not match.")
