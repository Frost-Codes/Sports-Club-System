# Generated by Django 4.2 on 2023-04-27 12:20

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_customerdetails_next_of_kin_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdetails',
            name='contact',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='games_of_interest',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Football', 'Football'), ('Basketball', 'Basketball'), ('Volleyball', 'Volleyball'), ('Hockey', 'Hockey'), ('Badminton', 'Badminton'), ('Table Tennis', 'Table Tennis'), ('Chess', 'Chess'), ('Netball', 'Netball'), ('Handball', 'Handball'), ('Rugby', 'Rugby'), ('Swimming', 'Swimming'), ('Pool', 'Pool')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='next_of_kin',
            field=models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Relative', 'Relative'), ('Other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='customerdetails',
            name='next_of_kin_contact',
            field=models.IntegerField(),
        ),
    ]