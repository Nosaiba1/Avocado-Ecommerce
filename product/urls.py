from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, OfferViewSet, PromocodeViewSet


router = DefaultRouter()
router.register(r'', ProductViewSet, 'product')
router.register(r'category', CategoryViewSet, 'category')
router.register(r'offer', OfferViewSet, 'offer')
router.register(r'promocode', PromocodeViewSet, 'promocode')

urlpatterns = [
    url(r'^', include(router.urls)),

]
