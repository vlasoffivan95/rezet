# Generated by Django 2.2 on 2020-01-22 08:57

from django.db import migrations, models
import django.db.models.deletion
import product.fields
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Назва')),
            ],
            options={
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Назва')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Ціна')),
                ('description', models.TextField(blank=True, verbose_name='Короткий опис')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_category', to='product.Category', verbose_name='категорія')),
            ],
            options={
                'verbose_name_plural': 'Продукт',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', product.fields.ThumbnailImageField(blank=True, upload_to=product.models.make_upload_path, verbose_name='Зображення')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image_product', to='product.Product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name_plural': 'Фото продуктів',
            },
        ),
    ]