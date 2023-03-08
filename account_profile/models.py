import string
import random
from django.db import models
from accounts.models import Account
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class SSCEquivalentExamName(models.Model):
    name = models.CharField(max_length=30, help_text="Degree Name Like: S.S.C, Dakhil. O Level etc")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "SSC\Equivalent Exam"
        verbose_name_plural = "SSC\Equivalent Exam"


class GroupName(models.Model):
    name = models.CharField(max_length=20, help_text="Science, Commerce, Humanities etc")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SSCInfo(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="account_ssc_info")
    exam = models.ForeignKey(SSCEquivalentExamName, on_delete=models.PROTECT, help_text="examination type")
    institution = models.CharField(max_length=255, help_text="institution name")
    group = models.ForeignKey(GroupName, on_delete=models.PROTECT, help_text="GROUP Name")
    gpa = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account.username}" 

class HSCEquivalentExamName(models.Model):
    name = models.CharField(max_length=30, help_text="Degree Name Like: H.S.c, A Level, Alim etc")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "HSC\Equivalent Exam"
        verbose_name_plural = "HSC\Equivalent Exam"

class HSCInfo(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="account_hsc_info")
    exam = models.ForeignKey(HSCEquivalentExamName, on_delete=models.PROTECT, help_text="examination type")
    institution = models.CharField(max_length=255, help_text="institution name")
    group = models.ForeignKey(GroupName, on_delete=models.PROTECT, help_text="GROUP Name")
    gpa = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account.username}" 
    

class GraduationExamName(models.Model):
    name = models.CharField(max_length=30, help_text="Degree Name Like: B.B.A, B.Sc. etc")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Graduation Exam Name"
        verbose_name_plural = "Graduation Exam Name"
    

class PostGraduationExamName(models.Model):
    name = models.CharField(max_length=30, help_text="Degree Name Like: B.B.A, B.Sc. etc")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(max_length=30, help_text="University or Institution Name")
    short_name = models.CharField(blank=True, max_length=10, help_text="University or Institution Short Name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # suggested field logo, description

    @property
    def number_of_students(self):
        return len(self.student_current_university.all())

    def __str__(self):
        return self.name    

class Subject(models.Model):
    name = models.CharField(max_length=30, help_text="Subject Name: Computer Eng. or Accounting etc")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class StudentCurrentEducationInfo(models.Model):
    STUDENT_STATUS_CHOICES = (
        ("first_year", "1st Year"),
        ("second_year", "2nd Year"),
        ("third_year", "3rd Year"),
        ("fourth_year", "4th Year"),
        ("just_passed", "Just Passed"),
    ) 
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="account_current_edu_info")
    university_level = models.CharField(max_length=20)
    exam_name = models.CharField(max_length=30, help_text="examination type")
    university = models.ForeignKey(University, on_delete=models.PROTECT, related_name="student_current_university", help_text="university_name")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, help_text="subject name")
    which_year_student = models.CharField(choices=STUDENT_STATUS_CHOICES, blank=True, max_length=20)

    def __str__(self):
        return self.account.username


class GraduationInfo(models.Model):
    STUDENT_STATUS_CHOICES = (
        ("first_year", "1st Year"),
        ("second_year", "2nd Year"),
        ("third_year", "3rd Year"),
        ("fourth_year", "4th Year"),
        ("just_passed", "Just Passed"),
    ) 
    RESULT_TYPE_CHOICES = (
        ("Grade", "Grade"),
        ("Division", "Division")
    )
    DIVISION_OR_CLASS_CHOICES = (
        ("1st division", "1st division"),
        ("2nd division", "2nd division"),
        ("3rd division", "3rd division"),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="account_grad_info")
    exam = models.ForeignKey(GraduationExamName, on_delete=models.PROTECT, help_text="examination type")
    university = models.ForeignKey(University, on_delete=models.PROTECT, related_name="university_graduate", help_text="university_name")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, help_text="subject name")
    which_year_student = models.CharField(choices=STUDENT_STATUS_CHOICES, max_length=20)
    result_type = models.CharField(blank=True, max_length=25, choices=RESULT_TYPE_CHOICES)
    cgpa = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1.0), MaxValueValidator(4.0)])
    division = models.CharField(blank=True, max_length=25, choices=DIVISION_OR_CLASS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.account.username}" 

class PostGraduationInfo(models.Model):
    STUDENT_STATUS_CHOICES = (
        ("first_year", "1st Year"),
        ("second_year", "2nd Year"),
        ("just_passed", "Just Passed"),
    ) 
    RESULT_TYPE_CHOICES = (
        ("Grade", "Grade"),
        ("Division", "Division")
    )
    DIVISION_OR_CLASS_CHOICES = (
        ("1st division", "1st division"),
        ("2nd division", "2nd division"),
        ("3rd division", "3rd division"),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="account_post_grad_info")
    exam = models.ForeignKey(PostGraduationExamName, on_delete=models.PROTECT, help_text="examination type")
    university = models.ForeignKey(University, on_delete=models.PROTECT, related_name="university_post_graduate", help_text="university_name")
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT, help_text="subject name")
    which_year_student = models.CharField(STUDENT_STATUS_CHOICES, max_length=20)
    cgpa = models.FloatField(null=True, blank=True, validators=[MinValueValidator(1.0), MaxValueValidator(4.0)])
    division = models.CharField(blank=True, max_length=25, choices=DIVISION_OR_CLASS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.account.username}" 

    

class Certificate(models.Model):
    student = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="student_certificate")
    batch_id = models.CharField(blank = True, max_length=10)
    certificate_id = models.CharField(max_length=10,blank=True, unique=True)
    certificate = models.FileField(blank=True, help_text="certificate file")
    description = models.TextField(blank=True, max_length=300)
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, help_text="The person who create the certificate")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student.username
    
    

    




