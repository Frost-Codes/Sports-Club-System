# Generated by Django 4.2 on 2023-05-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_county_county_alter_town_town_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='town',
            name='shipping_cost',
            field=models.PositiveIntegerField(default=100),
        ),
    ]