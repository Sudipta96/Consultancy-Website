# Generated by Django 4.0 on 2023-03-01 12:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import student_forum.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_address'),
        ('student_forum', '0016_companyinternship_unique_company_internship'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAdmissionTransactionInfo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('transaction_id', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.ForeignKey(help_text='The person who has added this transaction info', null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.account')),
                ('student', models.ForeignKey(help_text='Student belongs to this transaction', on_delete=django.db.models.deletion.CASCADE, related_name='student_admission_transaction', to='accounts.account')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('father_name', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(blank=True, help_text='Supported Formats: +8801757551134, 8801757871165 or 01715604232', max_length=14, validators=[django.core.validators.RegexValidator('^(?:\\+?88)?01[3-9]\\d{8}$', message='Contact number must be entered in following formats: +8801757551134, 8801857871165 or 01915604232')])),
                ('avatar', imagekit.models.fields.ProcessedImageField(default='default/default_avatar.jpg', upload_to=student_forum.models.Admission.get_student_admission_avatar_file_path, validators=[django.core.validators.FileExtensionValidator(['jpg', 'png']), student_forum.models.validate_account_avatar_file_size])),
                ('transaction_id', models.CharField(max_length=10, unique=True)),
                ('national_id', models.IntegerField(blank=True, unique=True)),
                ('birth_cirtificate_id', models.IntegerField(blank=True, unique=True)),
                ('is_verified', models.BooleanField(default=False, help_text='admission is verified or not')),
                ('is_checked', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(help_text='Student belongs to this admission', on_delete=django.db.models.deletion.CASCADE, related_name='student_admission', to='accounts.account')),
            ],
        ),
    ]