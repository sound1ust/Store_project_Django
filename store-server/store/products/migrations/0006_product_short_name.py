# Generated by Django 3.2.17 on 2023-03-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_is_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='short_name',
            field=models.TextField(default='', max_length=128),
        ),
    ]
