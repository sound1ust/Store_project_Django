# Generated by Django 3.2.17 on 2023-03-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_slogan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_name',
            field=models.TextField(max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='slogan',
            field=models.TextField(max_length=128),
        ),
    ]
