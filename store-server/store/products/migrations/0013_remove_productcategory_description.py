# Generated by Django 3.2.17 on 2023-03-23 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20230323_1811'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='description',
        ),
    ]