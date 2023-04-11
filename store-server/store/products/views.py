from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import HttpResponseRedirect, render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory


class IndexView(TitleMixin, ListView):
    model = Product
    template_name = 'products/index.html'
    title = 'Xstore'

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        return queryset.filter(is_new=True).order_by('name')


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 6
    title = 'Каталог Xstore'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        categories = cache.get('categories')
        if not categories:
            context['categories'] = ProductCategory.objects.all()
            cache.set('categories', context['categories'], 30)
        else:
            context['categories'] = categories
        return context


class AboutView(TitleMixin, TemplateView):
    template_name = 'products/about.html'
    title = 'О нас'


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    if product.details:
        gen_products_by_color = Product.objects.filter(details__contains={'Поколение': product.details['Поколение'],
                                                                          'Память': product.details['Память']})
        gen_products_by_ram = Product.objects.filter(details__contains={'Поколение': product.details['Поколение'],
                                                                        "Цвет": product.details['Цвет']})
    else:
        gen_products_by_ram, gen_products_by_color = {}, {}
    return render(request, 'products/product_detail.html',
                  {'product': product, 'gen_products_by_ram': gen_products_by_ram,
                   'gen_products_by_color': gen_products_by_color})


@login_required
def basket_add(request, product_id):
    Basket.create_or_update(product_id, request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])  # Возвращает текущую страницу


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
