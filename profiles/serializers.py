from rest_framework import serializers
from django.contrib.auth.models import User

from profiles.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'phone_number']


    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        user = instance.user

        # آپدیت اطلاعات کاربر
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.save()

        # آپدیت اطلاعات پروفایل
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.save()

        return instance