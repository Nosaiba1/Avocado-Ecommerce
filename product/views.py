from django.shortcuts import render
from .models import Product, Offer, Category, PromoCode

from .serializers import ProductSerializer, CategorySerializer, OfferSerializer, PromoCodeSerializer
from rest_framework import viewsets, permissions
from .permissions import IsActiveAndAdmin, IsOwnerOrReadOnly
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
import pdb


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # pdb.set_trace()

    def get_permissions(self):
        permissions = []
        if self.action == ['update', 'create', 'destroy']:
            permissions.append(IsActiveAndAdmin)

        return permissions


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @list_route(methods=['get'])
    def products(self, request):
        queryset = self.filter_queryset(self, Product.name)
        return Response(queryset)


class OfferViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class PromocodeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PromoCode.objects.all()
    serializer_class = PromoCodeSerializer



