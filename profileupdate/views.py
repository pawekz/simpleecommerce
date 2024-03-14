from django.shortcuts import render, redirect
from .forms import CustomerUpdateForm, SellerUpdateForm
from sellerregistration.models import Customer, Seller


# Create your views here.
def update_profile(request):
    if request.user.is_authenticated:
        if isinstance(request.user, Customer):
            if request.method == 'POST':
                form = CustomerUpdateForm(request.POST, instance=request.user)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
            else:
                form = CustomerUpdateForm(instance=request.user)
        elif isinstance(request.user, Seller):
            if request.method == 'POST':
                form = SellerUpdateForm(request.POST, instance=request.user)
                if form.is_valid():
                    form.save()
                    return redirect('profile')
            else:
                form = SellerUpdateForm(instance=request.user)
        return render(request, 'profile_updates/update_profile.html', {'form': form})
    else:
        return redirect('login')
