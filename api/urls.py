from django.urls import path
from .views import CategoryListView, ProductListAPIView




urlpatterns = [
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('product/', ProductListAPIView.as_view(), name='product-list'),
]