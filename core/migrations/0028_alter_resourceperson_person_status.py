# Generated by Django 4.0 on 2023-03-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_herosection_page_name_alter_herosection_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceperson',
            name='person_status',
            field=models.CharField(choices=[('M', 'Managing Body'), ('P', 'Parmanent Speaker'), ('G', 'Guest Speaker')], max_length=20),
        ),
    ]