# Generated by Django 4.0.1 on 2022-05-13 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_orders_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ManyToManyField(to='Product.users'),
        ),
    ]
