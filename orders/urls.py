from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, CartViewSet, test_session

router = DefaultRouter()
router.register(r'cart', CartViewSet, base_name='cart')
router.register(r'order', OrderViewSet, base_name='order')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test-session/$', test_session, name='test_session'),
]
