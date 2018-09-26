from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter, Route, DynamicDetailRoute, \
    DynamicDetailRoute, SimpleRouter
from .views import ProfileViewSet

urlpatterns = [
    url(r'^profile/$', ProfileViewSet.as_view()),
]




