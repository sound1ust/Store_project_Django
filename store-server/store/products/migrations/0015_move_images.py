from django.db import migrations


def move_images(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    ProductImage = apps.get_model('products', 'ProductImage')
    for product in Product.objects.all():
        ProductImage.objects.create(product=product, image=product.image)


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_productimage'),
    ]

    operations = [
        migrations.RunPython(move_images),
    ]
