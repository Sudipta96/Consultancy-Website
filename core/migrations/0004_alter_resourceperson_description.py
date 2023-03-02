# Generated by Django 4.0 on 2023-02-26 21:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_resourceperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceperson',
            name='description',
            field=ckeditor.fields.RichTextField(help_text='resource person bio or details', max_length=1000),
        ),
    ]
