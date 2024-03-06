from django.urls import path
from . import views

urlpatterns = [
    path('', views.sellerreg, name='sellerreg'),
    path('terms_and_conditions/', views.terms_and_conditions, name='terms_and_conditions'),
    path('customer_registration/', views.customer_registration, name='customer_registration'),
]