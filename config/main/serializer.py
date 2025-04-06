from rest_framework import serializers

from .models import Category, Product, Order


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"