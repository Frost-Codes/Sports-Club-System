# Generated by Django 4.2 on 2023-04-27 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mychoices_alter_product_category_customerdetails'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyChoices',
        ),
    ]
