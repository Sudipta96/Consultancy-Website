# Generated by Django 4.0 on 2023-02-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_account_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='bio',
            field=models.TextField(blank=True, help_text='account owner bio', max_length=400),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(help_text='Username should be unique', max_length=200),
        ),
    ]
