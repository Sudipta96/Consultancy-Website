# Generated by Django 4.0 on 2023-03-03 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_account_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='full_name',
            new_name='fullname',
        ),
    ]