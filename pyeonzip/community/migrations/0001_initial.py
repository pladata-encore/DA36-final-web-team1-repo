# Generated by Django 5.1.6 on 2025-02-11 04:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryId', models.AutoField(primary_key=True, serialize=False)),
                ('categoryName', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('communityId', models.AutoField(primary_key=True, serialize=False)),
                ('communityTitle', models.CharField(max_length=100)),
                ('communityContent', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateField()),
                ('authorId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='User_community', to=settings.AUTH_USER_MODEL)),
                ('categoryId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='community.category')),
                ('productId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product_community', to='product.product')),
                ('voter', models.ManyToManyField(blank=True, null=True, related_name='Community_voters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
