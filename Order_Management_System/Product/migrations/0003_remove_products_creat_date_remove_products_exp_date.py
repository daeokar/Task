# Generated by Django 4.0.1 on 2022-05-12 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_orders_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='creat_date',
        ),
        migrations.RemoveField(
            model_name='products',
            name='exp_date',
        ),
    ]
