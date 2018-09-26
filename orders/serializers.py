from .models import Order, Cart
from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'unit_price')


class CartSerializer(serializers.ModelSerializer):
    product_item = ProductSerializer(many=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Cart
        fields = ('user', 'product_item', 'total')
        extra_kwargs = {'total': {'read_only': True}}

    def create(self, validated_data):
        item = validated_data.pop('product_item')
        validated_data['item'] = item
        return super(CartSerializer, self).create(validated_data)


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    location = serializers.JSONField()
    cart = CartSerializer(many=False, read_only=True)

    class Meta:
        model = Order
        fields = ('user', 'cart', 'location')

    def create(self, validated_data):
        session = self.context['request'].session
        cart = Cart.objects.get(id=session.get('user_cart'))
        validated_data['cart'] = cart

        new_cart = Cart.objects.create(user=self.context['request'].user)
        session.update({'user_cart': new_cart.id})

        return super(OrderSerializer, self).create(validated_data)


