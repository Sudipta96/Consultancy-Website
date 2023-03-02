from django.db import models
from student_forum.models import University,Company

# Create your models here.
class RegistrationInfo(models.Model):
    number_of_students = models.IntegerField(default=0)
    current_month = models.CharField(max_length=20)
    current_year = models.CharField(max_length=4)

    # def __str__(self):
    #     return f"{self.number_of_students}"

    class Meta:
        verbose_name = "Registration Num/Month"
        verbose_name_plural = "Registration Num/Month"

class AdmissionInfo(models.Model):
    number_of_students = models.IntegerField(default=0)
    current_month = models.CharField(max_length=20)
    current_year = models.CharField(max_length=4)

    class Meta:
        verbose_name = "Admission Num/Month"
        verbose_name_plural = "Admission Num/Month"

class StudentsPerUniversityInfo(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name="university_per_info")
    number_of_students = models.IntegerField(default=0)

    class Meta:
        verbose_name = "No. of Students/University"
        verbose_name_plural = "No. of Students/University"

class StudentsPerCompanyInfo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="students_per_company_info")
    number_of_students = models.IntegerField(default=0)
    current_year = models.CharField(blank=True, max_length=4)

    class Meta:
        verbose_name = "No. of Students/Company"
        verbose_name_plural = "No. of Students/Company"


    

