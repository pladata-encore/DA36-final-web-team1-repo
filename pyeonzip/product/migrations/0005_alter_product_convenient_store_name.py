# Generated by Django 5.1.6 on 2025-02-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_productcategoryid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='convenient_store_name',
            field=models.CharField(default='all', max_length=10),
        ),
    ]
