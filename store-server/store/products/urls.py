from django.urls import path

from products.views import (AboutView, ProductsListView, basket_add,
                            basket_remove, product_detail)

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('<int:product_id>/', product_detail, name='product_detail'),
    path('about/', AboutView.as_view(), name='about'),
]
