from django.shortcuts import render

from products.models import ProductCategory, Product


# Create your views here.


def index(request):
    context = {
        "title": "Store",
    }
    return render(request=request, template_name="products/index.html", context=context)


def products(request):
    context = {
        "title": "Store - Каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all(),
    }
    return render(request=request, template_name="products/products.html", context=context)
