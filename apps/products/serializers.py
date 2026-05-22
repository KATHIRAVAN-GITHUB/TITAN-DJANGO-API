from rest_framework import serializers
from .models import ProductCard

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCard
        fields = "__all__"