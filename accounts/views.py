from .models import UserProfile
from rest_framework import generics
from .serializers import UserProfileSerializer
from djoser import views as DjoserViews
from requests import Response


class ProfileViewSet(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user.profile
