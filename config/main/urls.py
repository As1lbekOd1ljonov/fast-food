from django.urls import path

from .views import (
    CategoryApiView, CategoryDetailApiView,
    ProductApiView, ProductDetailApiView,
    OrderApiView, OrderDetailApiView
)

urlpatterns = [
    path('category/', CategoryApiView.as_view()),
    path('category/<int:pk>', CategoryDetailApiView.as_view()),

    path('product/', ProductApiView.as_view()),
    path('product/<int:pk>', ProductDetailApiView.as_view()),

    path('order/', OrderApiView.as_view()),
    path('order/<int:pk>', OrderDetailApiView.as_view()),
]