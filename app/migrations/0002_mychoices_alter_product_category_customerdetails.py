# Generated by Django 4.2 on 2023-04-27 07:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('FB', 'Football'), ('BB', 'Basketball'), ('VB', 'Volleyball'), ('HY', 'Hockey'), ('BM', 'Badminton'), ('TT', 'Table Tennis'), ('CS', 'Chess'), ('NB', 'Netball'), ('HB', 'Handball'), ('RB', 'Rugby'), ('SM', 'Swimming'), ('PL', 'Pool')], max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FB', 'Football'), ('BB', 'Basketball'), ('VB', 'Volleyball'), ('HY', 'Hockey'), ('BM', 'Badminton'), ('TT', 'Table Tennis'), ('CS', 'Chess'), ('NB', 'Netball'), ('HB', 'Handball'), ('RB', 'Rugby'), ('AL', 'All')], max_length=2),
        ),
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('ML', 'Male'), ('RM', 'Female')], max_length=2)),
                ('next_of_kin', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('contact', models.IntegerField()),
                ('sub_county', models.CharField(choices=[('Kasa', 'Kasarani'), ('Westi', 'Westlands'), ('Makadara', 'Makadara'), ('Starehe', 'Starehe'), ('Matahare', 'Matahare'), ('Roysambu', 'Roysambu'), ('Ruaraka', 'Ruaraka'), ('Langata', 'Langata'), ('Emba Central', 'Embakasi Central'), ('Emba North', 'Embakasi North'), ('Emba South', 'Embakasi South'), ('Meru South', 'Meru South'), ('Maara', 'Maara')], max_length=50)),
                ('school', models.CharField(max_length=300)),
                ('games_of_interest', multiselectfield.db.fields.MultiSelectField(choices=[('FB', 'Football'), ('BB', 'Basketball'), ('VB', 'Volleyball'), ('HY', 'Hockey'), ('BM', 'Badminton'), ('TT', 'Table Tennis'), ('CS', 'Chess'), ('NB', 'Netball'), ('HB', 'Handball'), ('RB', 'Rugby'), ('SM', 'Swimming'), ('PL', 'Pool')], max_length=30)),
                ('height_in_cm', models.IntegerField()),
                ('weight_in_kgs', models.IntegerField()),
                ('special_needs', models.CharField(choices=[('T', True), ('F', False)], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
