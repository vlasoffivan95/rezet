# Generated by Django 2.2 on 2020-01-22 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=250, verbose_name="Ім'я")),
                ('address', models.CharField(blank=True, default='', max_length=300, verbose_name='Адрес')),
                ('phone', models.CharField(blank=True, default='', max_length=300, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, default='', max_length=300, verbose_name='e-mail')),
                ('shipping_options', models.IntegerField(choices=[(1, 'Free shipping'), (2, 'Express shipping'), (3, 'Courier shipping'), (4, 'Free express shipping')], default=1, verbose_name='Варіанти доставки')),
            ],
            options={
                'verbose_name_plural': 'Замовлення',
            },
        ),
    ]