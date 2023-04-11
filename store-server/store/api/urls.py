from django.urls import include, path
from rest_framework import routers

from api.views import BasketModelViewSet, ProductModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(prefix=r'products', viewset=ProductModelViewSet)
router.register(prefix=r'baskets', viewset=BasketModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
