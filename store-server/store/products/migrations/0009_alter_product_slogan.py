# Generated by Django 3.2.17 on 2023-03-18 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20230318_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slogan',
            field=models.TextField(max_length=128, null=True),
        ),
    ]
