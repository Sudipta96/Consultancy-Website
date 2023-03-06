# Generated by Django 4.0 on 2023-03-06 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_rename_address_line_1_address_address_line'),
        ('student_forum', '0021_delete_studentfeedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(help_text='Write your review', max_length=400)),
                ('rating', models.CharField(choices=[('1', 'ONE STAR'), ('2', 'TWO STAR'), ('3', 'THREE STAR'), ('4', 'FOUR STAR'), ('5', 'FIVE STAR')], default='3', max_length=10)),
                ('will_be_displayed', models.BooleanField(default=False, help_text='If this field is checked, Review will be displayed in website.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feedback_given_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback_given_by', to='accounts.account')),
                ('verified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='feedback_verified_by', to='accounts.account')),
            ],
            options={
                'verbose_name': 'Student Feedback',
                'verbose_name_plural': 'Student Feedbacks',
            },
        ),
    ]