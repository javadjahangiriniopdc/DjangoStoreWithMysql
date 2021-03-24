from django.contrib.auth.models import User
from rest_framework import serializers

from orderapp.models import Customer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class Customerserializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = ('user', 'avatar', 'description')


class CreateCustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Customer
        fields = ('user', 'description')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        customer, created = Customer.objects.update_or_create(user=user,
                                                             description=validated_data.pop('description'))
        return customer
    # user = serializers.CharField(source=User)
    # description = serializers.CharField(max_length=128, required=True, allow_null=False, allow_blank=False,
    #                                     write_only=True)
    #
    # def validate(self, attrs):
    #     return attrs
    #
    # def update(self, instance, validated_data):
    #     instance.user_profile.first_name = validated_data.get('first_name', instance.user_profile.first_name)
    #     instance.user_profile.last_name = validated_data.get('last_name', instance.user_profile.last_name)
    #     instance.user_name = validated_data.get('user_name', instance.user_name)
    #     instance.email = validated_data.get('email', instance.email)
    #
    #     return instance
    #
    # def create(self, validated_data):
    #     user_name = validated_data.get('user_name')
    #     password = validated_data.get('password')
    #     email = validated_data.get('email')
    #     first_name = validated_data.get('first_name')
    #     last_name = validated_data.get('last_name')
    #     description = validated_data.get('description')
    #     customer = Customer()
    #     customer.user = User.objects.create_user(username=user_name, password=password, email=email,
    #                                              first_name=first_name,
    #                                              last_name=last_name)
    #     customer.description = description
    #
    #     return customer
