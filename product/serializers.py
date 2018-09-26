from .models import Product, Category, Offer, PromoCode
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ('name', 'pic', 'unit_price', 'details', 'has_offer_value',
                  'category', 'is_available')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('product', 'offer_percentage', 'offer_details')


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = (
            'product', 'code', 'usage_limit', 'expiring_date',
            'code_percentage'
        )
