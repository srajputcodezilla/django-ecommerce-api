# Generated by Django 4.2.6 on 2023-10-18 11:23

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category_name', models.CharField(blank=True, max_length=60, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
                ('discount', models.IntegerField(default=0, null=True)),
                ('discount_type', models.CharField(max_length=10, null=True)),
                ('stock_qnt', models.IntegerField(default=0, null=True)),
                ('avilable_qnt', models.IntegerField(default=0, null=True)),
                ('category', models.ForeignKey(db_column='ctaegory_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=60, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default=0, null=True)),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'details',
            },
        ),
    ]