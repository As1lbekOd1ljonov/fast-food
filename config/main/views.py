from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Category, Product, Order
from .serializer import  CategorySerializers, ProductSerializers, OrderSerializers


class CategoryApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailApiView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers



class ProductApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDetailApiView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class OrderApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


class OrderDetailApiView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers