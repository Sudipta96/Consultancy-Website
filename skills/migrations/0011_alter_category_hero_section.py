# Generated by Django 4.0 on 2023-03-05 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_herosection_page_name_alter_herosection_slug'),
        ('skills', '0010_category_hero_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='hero_section',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='category_hero_section', to='core.herosection'),
        ),
    ]
