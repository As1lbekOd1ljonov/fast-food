from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView


from .models import Category, Product, Order
from .pagination import CategoryPagination, ProductPagination, OrderPagination
from .permissions import Permission
from .serializer import  CategorySerializers, ProductSerializers, OrderSerializers
from .throttling import CategoryAnonThrottling, CategoryUserThrottling, ProductAnonThrottling, ProductUserThrottling, \
    OrderAnonThrottling, OrderUserThrottling


class CategoryApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    # permission_classes = [Permission]
    throttle_classes = [CategoryAnonThrottling,CategoryUserThrottling]
    pagination_class = CategoryPagination


class CategoryDetailApiView(RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    # permission_classes = [Permission]
    throttle_classes = [CategoryAnonThrottling, CategoryUserThrottling]



class ProductApiView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # permission_classes = [Permission]
    throttle_classes = [ProductAnonThrottling, ProductUserThrottling]
    pagination_class = ProductPagination



class ProductDetailApiView(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # permission_classes = [Permission]
    throttle_classes = [ProductAnonThrottling, ProductUserThrottling]



class OrderApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    # permission_classes = [Permission]
    throttle_classes = [OrderAnonThrottling, OrderUserThrottling]
    pagination_class = OrderPagination


class OrderDetailApiView(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    # permission_classes = [Permission]
    throttle_classes = [OrderAnonThrottling, OrderUserThrottling]