from django.contrib import admin
from .models import Product, Category, Offer, PromoCode

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Offer)
admin.site.register(PromoCode)


