# Generated by Django 4.0 on 2023-03-05 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_icon_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='icon',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
