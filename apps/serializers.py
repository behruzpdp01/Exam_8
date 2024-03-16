from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.generics import ListAPIView

from rest_framework.serializers import ModelSerializer

from apps.models import User, Category, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # class
class RegisterModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    def validate(self, data):
        confirm_password = data.pop('confirm_password')
        print(confirm_password)
        print(data['password'])
        if confirm_password and confirm_password == data['password']:
            data['password'] = make_password(data['password'])
            return data
        raise ValidationError("Parol mos emas ")


    class Meta:
        model = User
        fields = 'username', 'password', 'email', 'confirm_password'
        extra_kwargs = {
            'password': {'write_only': True}
        }
