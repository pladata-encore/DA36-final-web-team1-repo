# Generated by Django 5.1.6 on 2025-02-11 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='categoryId',
        ),
        migrations.RemoveField(
            model_name='community',
            name='authorId',
        ),
        migrations.RemoveField(
            model_name='community',
            name='productId',
        ),
        migrations.RemoveField(
            model_name='community',
            name='voter',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Community',
        ),
    ]
