# Generated by Django 2.2.4 on 2019-08-22 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='external_id')),
                ('name', models.CharField(max_length=30, verbose_name='product_name')),
                ('type', models.CharField(choices=[
                    ('SP', 'Simple Product'),
                    ('CP', 'Configurable Product'),
                    ('GP', 'Grouped Product'),
                    ('VP', 'Virtual Product'),
                    ('BP', 'Bundle Product'),
                    ('DP', 'Downloadable Product')], max_length=3, verbose_name='product_type')),
                ('price', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='price')),
                ('status', models.BooleanField(
                    default=True, help_text='Designates whether the product is active or not.',
                    verbose_name='active status')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, null=True,
                                                 related_name='product_created', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, null=True,
                                                 related_name='product_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'product',
            },
        ),
    ]
