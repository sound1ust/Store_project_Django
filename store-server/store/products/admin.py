from django.contrib import admin

from products.models import Basket, Product, ProductCategory, ProductImage

admin.site.register(ProductCategory)
admin.site.register(ProductImage)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('promo_image', 'name', 'description', ('short_name', 'slogan'), ('price', 'quantity'),
              'category', 'is_new',)
    search_fields = ('name',)
    ordering = ('name', )
    inlines = [ProductImageInline]


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0

