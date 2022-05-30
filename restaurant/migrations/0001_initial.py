# Generated by Django 4.0.4 on 2022-05-30 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyTopping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'my_topping',
            },
        ),
        migrations.CreateModel(
            name='MyPizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_name', models.CharField(max_length=100)),
                ('pizza_topping', models.ManyToManyField(to='restaurant.mytopping')),
            ],
            options={
                'db_table': 'my_pizza',
            },
        ),
    ]
