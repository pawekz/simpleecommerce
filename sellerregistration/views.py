from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import SellerForm


# Create your views here.

def sellerreg(request):
    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            return redirect('sellerreg')
    else:
        form = SellerForm()
    return render(request, 'sellerregistration/sellerreg.html', {'form': form})


def terms_and_conditions(request):
    return render(request, 'sellerregistration/terms_and_conditions.html')


def customer_registration(request):
    return render(request, 'sellerregistration/customer_registration.html')
