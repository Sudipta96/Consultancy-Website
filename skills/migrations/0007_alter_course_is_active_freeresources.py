# Generated by Django 4.0 on 2023-02-26 18:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import skills.models
import skills.validators


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0006_alter_course_preview_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(default=True, help_text='format: true=course visible', verbose_name='course visibility'),
        ),
        migrations.CreateModel(
            name='FreeResources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, help_text='Resource url text', max_length=200)),
                ('resource_url', models.URLField(blank=True, help_text='resource url or link.')),
                ('resource_file', models.FileField(blank=True, help_text='Required: resource file. Supported file format: pdf. Maximum file limit:20mb', null=True, upload_to=skills.models.FreeResources.get_resource_file_path, validators=[django.core.validators.FileExtensionValidator(['pdf']), skills.validators.validate_file_size])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(help_text='Required: Choose the course name.                                                   N.B: If you delete the course, related course resources will be automatically deleted', on_delete=django.db.models.deletion.CASCADE, related_name='course_resource', to='skills.course')),
            ],
        ),
    ]
