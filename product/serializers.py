from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):  # create class to serializer model
    # creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = Product
        fields = ("name", "category","category_name","id","price","discount","discount_type","stock_qnt","avilable_qnt")
class CategorySerializer(serializers.ModelSerializer):  # create class to serializer model
    # creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = Category
        fields = ("name","category_id")
class ProductDetailsSerializer(serializers.ModelSerializer):  # create class to serializer model
    # creator = serializers.ReadOnlyField(source='creator.username')
    class Meta:
        model = ProductDetail
        fields = ("product","product_name","description","image_url","price")
