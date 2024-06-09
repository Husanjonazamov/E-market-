from django.shortcuts import render
from category.models import Category
from store.models import Product
from rest_framework import generics
from .serializers import CategorySerializer, ProductSerializer



class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer