from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory
from products.views import ProductsListView


class IndexViewTestCase(TestCase):
    def test_view(self):
        path = reverse('index')  # http://127.0.0.1:8000/
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Xstore')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductsListViewTestCase(TestCase):
    fixtures = ['categories.json', 'goods.json']

    def setUp(self):
        self.products = Product.objects.all()
        self.pagination = ProductsListView.paginate_by

    def _common_tests(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Каталог Xstore')
        self.assertTemplateUsed(response, 'products/products.html')

    def test_list(self):
        path = reverse('products:index')
        response = self.client.get(path)

        self._common_tests(response=response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products[:self.pagination])
        )

    def test_list_with_category(self):
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_tests(response=response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id)[:self.pagination])
        )
