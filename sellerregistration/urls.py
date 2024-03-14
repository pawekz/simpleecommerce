from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.sellerreg, name='sellerreg'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('customer_registration/', views.customer_registration, name='customer_registration'),
    path('customerreg/', views.customerreg, name='customerreg'),
    path('customer_terms_and_conditions/', views.customer_terms_and_conditions, name='customer_terms_and_conditions'),

    #path('profile_updates/', include('profile_updates.urls')),
]