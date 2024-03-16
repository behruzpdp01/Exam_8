from cProfile import Profile

from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ModelSerializer

from apps.models import User, Category, Product
from apps.permision import IsOwnerOrReadOnly
from apps.send_email import send_emails
from apps.serializers import RegisterModelSerializer, CategoryModelSerializer,ProductModelSerializer


# Create your views here.



class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
    pagination_class = None


class ProductUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    serializer_class = ProductModelSerializer
    http_method_names = ['put', 'delete', 'patch']
class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer
    # def create(self, request, *args, **kwargs):
    #     send_emails(to_email=kwargs['email'])
    #     return super().create(request, *args, **kwargs)
    #
    #

