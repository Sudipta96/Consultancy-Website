# Generated by Django 4.0 on 2023-03-04 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_alter_graduationinfo_which_year_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graduationinfo',
            name='which_year_student',
            field=models.CharField(choices=[('first_year', '1st Year'), ('second_year', '2nd Year'), ('third_year', '3rd Year'), ('fourth_year', '4th Year'), ('just_passed', 'Just Passed')], max_length=20),
        ),
        migrations.AlterField(
            model_name='postgraduationinfo',
            name='which_year_student',
            field=models.CharField(max_length=20, verbose_name=(('first_year', '1st Year'), ('second_year', '2nd Year'), ('just_passed', 'Just Passed'))),
        ),
    ]
