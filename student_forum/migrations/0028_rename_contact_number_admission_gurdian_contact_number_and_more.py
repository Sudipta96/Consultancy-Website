# Generated by Django 4.0 on 2023-03-08 01:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_forum', '0027_alter_successstory_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admission',
            old_name='contact_number',
            new_name='gurdian_contact_number',
        ),
        migrations.AddField(
            model_name='admission',
            name='personal_contact_number',
            field=models.CharField(blank=True, help_text='Supported Formats: +8801757551134, 8801757871165 or 01715604232', max_length=14, validators=[django.core.validators.RegexValidator('^(?:\\+?88)?01[3-9]\\d{8}$', message='Contact number must be entered in following formats: +8801757551134, 8801857871165 or 01915604232')]),
        ),
    ]