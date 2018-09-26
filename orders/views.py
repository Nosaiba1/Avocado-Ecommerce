from rest_framework import viewsets, permissions, response, status
from rest_framework.decorators import list_route
from .models import Order, Cart
from .serializers import OrderSerializer, CartSerializer
from product.models import Product, PromoCode

from django.http import HttpResponse


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)
        # return Cart.objects.filter(cart__user=self.request.user)

    @list_route(methods=['post'])
    def add_to_cart(self, request):
        cart_id = request.session.get('user_cart')
        if not cart_id:
            cart_id = Cart.objects.create(user=self.request.user).id
            request.session.update({'user_cart': cart_id})
        cart = Cart.objects.get(id=cart_id)  # another sol. for 1
        # cart = request.user.cart_set.get(id=cart_id)  # 1
        try:
            pk = request.data.get('product')
            product = Product.objects.get(pk=pk)
            code = request.data.get('promo')
            try:
                promo = PromoCode.objects.get(code=code)
                cart.update(product, promo)
            except PromoCode.DoesNotExist:
                cart.update(product)
        except Product.DoesNotExist:
            return response.Response({"error": "product not found"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CartSerializer(cart)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def delete_from_cart(self, request):
        cart_id = request.session.get('user_cart')
        if not cart_id:
            cart_id = Cart.objects.create(user=request.user).id
            request.session.update({'user_cart': cart_id})
        cart = Cart.objects.get(id=cart_id)
        pk = request.data.get('product')
        product = Product.objects.get(pk=pk)
        cart.product_item.remove(product)
        cart.delete_product(product)
        return response.Response(status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


def test_session(request):

    return HttpResponse(request.session.set_test_cookie()
)

