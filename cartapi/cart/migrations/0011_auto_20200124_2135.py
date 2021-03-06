# Generated by Django 2.2 on 2020-01-24 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20200124_2115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderproduct',
            options={'verbose_name_plural': 'Продукты заказов'},
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_product_order', to='cart.Order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='typedelivery',
            name='active_default',
            field=models.BooleanField(blank=True, default=False, verbose_name='Активный по умолчанию'),
        ),
        migrations.AlterField(
            model_name='typedelivery',
            name='active_more',
            field=models.BooleanField(blank=True, default=False, verbose_name='Активный если цена больше 300€'),
        ),
    ]
