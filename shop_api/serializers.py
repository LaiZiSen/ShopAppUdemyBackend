from rest_framework import serializers
from shop_api import models

class ShopItemSerializer (serializers.ModelSerializer):
    """Serializer for ShopItem"""
    class Meta:
        model = models.ShopItem
        fields = ('id','title','description','imageUrl','isFavourite','price')