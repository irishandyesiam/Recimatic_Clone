# Generated by Django 4.2 on 2023-04-20 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppinglist',
            name='quantity',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='unit',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
