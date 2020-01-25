# Generated by Django 2.2 on 2020-01-24 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_typedelivery_active_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='order',
            name='price_shipping',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Цена доставки'),
        ),
    ]