# Generated by Django 4.0 on 2023-03-05 13:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_icon_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourmission',
            name='short_description',
            field=ckeditor.fields.RichTextField(help_text='Short Description', max_length=700),
        ),
        migrations.AlterField(
            model_name='ourvision',
            name='short_description',
            field=ckeditor.fields.RichTextField(help_text='Short Description', max_length=600),
        ),
    ]
