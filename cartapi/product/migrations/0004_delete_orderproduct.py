# Generated by Django 2.2 on 2020-01-23 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_orderproduct'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]