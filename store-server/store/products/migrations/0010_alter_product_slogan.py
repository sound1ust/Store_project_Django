# Generated by Django 3.2.17 on 2023-03-18 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_slogan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slogan',
            field=models.TextField(blank=True, default='', max_length=128),
        ),
    ]
