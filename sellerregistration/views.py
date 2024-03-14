from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import SellerForm, CustomerForm


# Create your views here.

def sellerreg(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Seller account has been created! You are now able to log in')
            return redirect('sellerreg')
    else:
        form = SellerForm()
    return render(request, 'sellerregistration/sellerreg.html', {'form': form})


def terms_and_conditions(request):
    return render(request, 'sellerregistration/terms_and_conditions.html')


def customer_registration(request):
    return render(request, 'customerregistration/customerreg.html')


def customerreg(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Customer account has been created! You are now able to log in')
            return redirect('customerreg')
    else:
        form = CustomerForm()
    return render(request, 'customerregistration/customerreg.html', {'form': form})


def customer_terms_and_conditions(request):
    return render(request, 'customerregistration/terms_and_conditions.html')


def seller_registration(request):
    return render(request, 'sellerregistration/sellerreg.html')
