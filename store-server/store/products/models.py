from django.db import models
from django.urls import reverse

from users.models import User


def get_upload_to(instance, filename):
    return f'products_images/{instance.product.category}/{instance.product.name}/{filename}'


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category', args=[str(self.id)])


class Product(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    promo_image = models.ImageField(upload_to='promo_images', blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    is_new = models.BooleanField(default=False)
    short_name = models.CharField(max_length=128)
    slogan = models.CharField(max_length=128, default='', blank=True)
    details = models.JSONField()

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Продукт: {self.name} | Категория: {self.category.name}"


class ProductImage(models.Model):
    image = models.ImageField(upload_to=get_upload_to)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'Изображение для {self.product.name}'


class BasketQuerySet(models.QuerySet):
    def total_quantity(self):
        return sum(map(lambda basket: basket.quantity, self))

    def total_sum(self):
        return sum(map(lambda basket: basket.sum(), self))


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f"Корзина для {self.user.username} | Продукт: {self.product.name}"

    def sum(self):
        return self.product.price * self.quantity

    def de_json(self):
        basket_item = {
            'product_name': self.product.name,
            'quantity': self.quantity,
            'price': float(self.product.price),
            'sum': float(self.sum()),
        }
        return basket_item
