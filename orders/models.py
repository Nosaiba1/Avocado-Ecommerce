from django.db import models
from product.models import Product, PromoCode

from djoser.views import User

from django.contrib.postgres.fields import JSONField


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='user')
    product_item = models.ManyToManyField(Product, related_name='product_item')
    total = models.DecimalField(default=00.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.user)

    @property
    def count_item(self):
        return self.product_item.count()

    def update(self, product, promo_code=None):
        self.product_item.add(product)
        if promo_code:
            self.total += product.price_with_promo(promo_code)
        else:
            self.total += product.unit_price
        self.save()

    def delete_product(self, product):
        self.product_item.remove(product)
        self.total -= product.unit_price
        self.save()


class Order(models.Model):
    user = models.ForeignKey(User)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)

    location = JSONField(blank=True, null=True)

    def __str__(self):
        return str(self.cart)


