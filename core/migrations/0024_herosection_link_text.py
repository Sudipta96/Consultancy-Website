# Generated by Django 4.0 on 2023-03-05 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_page_alter_herosection_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='herosection',
            name='link_text',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
