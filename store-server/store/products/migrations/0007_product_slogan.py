# Generated by Django 3.2.17 on 2023-03-18 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slogan',
            field=models.TextField(default='', max_length=128),
        ),
    ]
