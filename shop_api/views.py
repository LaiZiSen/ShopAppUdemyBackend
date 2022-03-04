from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import viewsets

from shop_api import serializers, models


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ShopItemViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating ShopItem"""
    serializer_class = serializers.ShopItemSerializer
    queryset = models.ShopItem.objects.all()

    def perform_create(self, serializer):
        return super().perform_create(serializer)