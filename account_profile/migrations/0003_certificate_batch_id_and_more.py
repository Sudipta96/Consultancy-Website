# Generated by Django 4.0 on 2023-03-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0002_certificatetemplate'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='batch_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='certificate_id',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
