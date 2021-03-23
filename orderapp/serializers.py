from django.contrib.auth.models import User
from rest_framework import serializers

from orderapp.models import Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SingleCustomerserializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ('user', 'avatar', 'description')
