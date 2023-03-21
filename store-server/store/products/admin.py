from django.contrib import admin

from products.models import Basket, Product, ProductCategory, Color

admin.site.register(ProductCategory)
admin.site.register(Color)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'promo_image', 'name', 'description', ('short_name', 'slogan'), ('price', 'quantity'), 'category', 'is_new','colors')
    search_fields = ('name',)
    ordering = ('name', )
    filter_horizontal = ('colors',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
