from django.db import router
from django.urls import path
from django.urls.conf import include

from rest_framework.routers import DefaultRouter

from shop_api import views


router = DefaultRouter()
router.register('shop-item',views.ShopItemViewSet)

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]