# Generated by Django 4.0 on 2023-02-28 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
        ('student_forum', '0013_alter_studentfeedback_feedback_given_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='University',
        ),
        migrations.AlterField(
            model_name='studentfeedback',
            name='university',
            field=models.ForeignKey(help_text='University Name', on_delete=django.db.models.deletion.PROTECT, related_name='feedbacker_university', to='resume.university'),
        ),
    ]
