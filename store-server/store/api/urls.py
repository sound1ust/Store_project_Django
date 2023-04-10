from django.urls import path, include

from rest_framework import routers

from api.views import ProductModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(prefix=r'products', viewset=ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
