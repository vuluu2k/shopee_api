# Generated by Django 4.2.7 on 2023-11-27 05:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_slug_alter_variation_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='origin_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='variation',
            name='retail_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='variation',
            name='wholesale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
