from django.contrib.auth.hashers import make_password
from django.db import models


# Create your models here.
class Seller(models.Model):
    StallName = models.CharField(max_length=255)
    SellerName = models.CharField(max_length=255)
    ContactNo = models.IntegerField()
    Address = models.CharField(max_length=255)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=128) #increased length of password field to 128 for the hash value

    def save(self, *args, **kwargs):
        self.Password = make_password(self.Password)
        super(Seller, self).save(*args, **kwargs)
