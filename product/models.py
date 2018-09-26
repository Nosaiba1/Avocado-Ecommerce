# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import MaxLengthValidator, MaxValueValidator, MinValueValidator
from djoser.views import User
from django.contrib.auth import get_user_model


class Product(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to='media_cdn/protected_media/products/', default='media_cdn/protected_media'
                                                                                     '/products/no-ig.jpg')
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField(validators=[MaxLengthValidator(600)], blank=True)
    has_offer_value = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def price_with_promo(self, promo_code):
        if self.has_offer_value:
            return self.unit_price * promo_code.code_percentage/100
        else:
            return self.unit_price


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Offer(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    offer_percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True,
                                           blank=True)
    offer_details = models.TextField(validators=[MaxLengthValidator(600)], null=True, blank=True)

    def __str__(self):
        return str(self.product)


class PromoCode(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    code = models.CharField(max_length=100, unique=False)
    usage_limit = models.IntegerField(default=1)
    expiring_date = models.DateTimeField()
    code_percentage = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.code
