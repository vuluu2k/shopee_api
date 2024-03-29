# Generated by Django 4.2.7 on 2024-01-16 10:30

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Shipping'), (2, 'Delivered'), (3, 'Cancel')], default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.TextField()),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), default=list, size=None)),
                ('currency', models.CharField(default='VND', max_length=255)),
                ('stock', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=1)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('sold', models.IntegerField(default=0)),
                ('historical_sold', models.IntegerField(default=0)),
                ('brand', models.CharField(default='', max_length=255)),
                ('price', models.FloatField(default=0)),
                ('price_max', models.FloatField(default=0)),
                ('price_min', models.FloatField(default=0)),
                ('hidden_price_display', models.FloatField(blank=True, default='', null=True)),
                ('price_before_discount', models.FloatField(default=0)),
                ('discount', models.FloatField(default=0)),
                ('size_chart', models.TextField(default='')),
                ('is_category_failed', models.CharField(default='', max_length=255, null=True)),
                ('video_info_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), default=list, size=None)),
                ('item_type', models.IntegerField(default=0)),
                ('reference_item_id', models.CharField(default='', max_length=255, null=True)),
                ('transparent_background_image', models.TextField(default='', null=True)),
                ('is_adult', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('tier_variation', models.JSONField()),
                ('thumbnail', models.TextField()),
                ('price', models.FloatField(default=0)),
                ('remain_quantity', models.IntegerField(default=0)),
                ('retail_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('origin_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('wholesale_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('star', models.IntegerField(default=5)),
                ('like', models.IntegerField(default=0)),
                ('attachment', models.TextField(default='')),
                ('message', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.variation')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.order')),
                ('variation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.variation')),
            ],
            options={
                'unique_together': {('order', 'variation')},
            },
        ),
    ]
