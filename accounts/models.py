from django.db import models
from django.contrib.auth.models import User
from product.models import Product


class UserProfile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_active = models.BooleanField(default=True)
    gender = models.CharField(max_length=50, choices=GENDER, null=True, blank=True)
    wish_list = models.ManyToManyField(Product, blank=True, related_name='wish_list')

    def __str__(self):
        return str(self.user)
