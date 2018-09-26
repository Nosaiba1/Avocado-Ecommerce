from .models import UserProfile
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from djoser.serializers import TokenSerializer


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    wish_list = serializers.StringRelatedField(many=True)

    class Meta:

        model = UserProfile
        fields = ('user', 'is_active', 'gender', 'email', 'wish_list')

    def get_email(self, obj):
        return obj.user.email

