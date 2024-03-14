# profile_updates/forms.py

from django import forms
from sellerregistration.models import Customer, Seller


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['CustomerName', 'ContactNo', 'Address', 'Username', 'Password']


class SellerUpdateForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['StallName', 'SellerName', 'ContactNo', 'Address', 'Username', 'Password']
