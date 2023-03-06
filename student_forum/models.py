import uuid
import string
import random
from django.db import models
from accounts.models import Account 
# from resume.models import University

# for validation
# to validate mobile number
from django.core.validators import FileExtensionValidator, RegexValidator
from django.core.exceptions import ValidationError

# django-imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# django-ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
from account_profile.models import StudentCurrentEducationInfo

    
# Create your models here.
class StudentFeedback(models.Model):
    RATING_CHOICES = (
        ('1', "ONE STAR"),
        ('2', "TWO STAR"),
        ('3', "THREE STAR"),
        ('4', "FOUR STAR"),
        ("5", "FIVE STAR")
    )
    # name = models.CharField(max_length=200, help_text="Your Full Name")
    # email = models.EmailField(verbose_name="email", max_length=60, help_text="Your Email Address")
    # university = models.ForeignKey(University, on_delete=models.PROTECT, related_name="feedbacker_university", help_text="University Name")
    review = models.TextField(max_length=400, help_text="Write your review")
    rating = models.CharField(choices=RATING_CHOICES,max_length=10,default="3")
    feedback_given_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="feedback_given_by")
    # verified_by = models.ForeignKey(Account, null=True, blank=True, on_delete=models.SET_NULL, related_name="feedback_verified_by")
    # is_verified = models.BooleanField(default=False, help_text="Review is verified or not")
    # is_checked = models.BooleanField(default=False, help_text="Review is checked by signals")
    will_be_displayed = models.BooleanField(default=False, help_text="If this field is checked, Review will be displayed in website.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.feedback_given_by.username
    
    @property
    def get_feedback_giver_university_name(self):
        try:
            edu_obj = StudentCurrentEducationInfo.objects.get(account=self.feedback_given_by)
            print(edu_obj.university.name)
            return edu_obj.university.name
        except StudentCurrentEducationInfo.DoesNotExist:
            print("No unviversity is associated with this account")
            pass

    
    class Meta:
        verbose_name = "Student Feedback"
        verbose_name_plural = "Student Feedbacks"

class Company(models.Model):
    name = models.CharField(max_length=250, help_text="Company name where student gets internship or placement")
    # suggested fields: logo, description

    def __str__(self):
        return self.name  
    
    @property
    def number_of_students(self):
        return len(self.company_internship.all())
    
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"


class CompanyInternship(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name="company_internship")
    student = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="student_internship")
    short_description = models.TextField(blank=True, max_length=300, help_text="Any details you want to add...")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"{self.company.name} - {self.student.username}"
    
    class Meta:
        verbose_name = "Company Internship"
        verbose_name_plural = "Company Internship"

        constraints = [
            models.UniqueConstraint(fields=['company', 'student'], name='unique_company_internship')
        ]


# to check resource person avatar image size
def validate_success_story_card_image_file_size(value):
    filesize= value.size

    if filesize > 5242880:  # 5 mb in bytes
        raise ValidationError("Image size should be less than 5Mb.")
    else:
        return value


class SuccessStory(models.Model):
    def get_success_story_card_image_file_path(self, filename):
        return f'success-stories/{filename}'
    
    student = models.ForeignKey(Account, related_name="success_story_holder", on_delete=models.SET_NULL, null=True, help_text="The person who belongs to the story")
    student_bio = models.TextField(max_length=255, help_text="This bio will be displayed in sucess story page.")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, help_text="The company name where the student got internship or placement") 
    image_thumbnail = ProcessedImageField(upload_to=get_success_story_card_image_file_path,
                                default="default/default_card.jpg",
                                validators=[FileExtensionValidator( ['jpg','png']), validate_success_story_card_image_file_size],
                                processors=[ResizeToFill(480, 320)],
                                format='JPEG',
                                options={'quality': 90},
                                help_text="This image will be displayed in list view card")
    card_intro = models.TextField(max_length=255, help_text="This introduction will be displayed in list card")
    story_tagline = models.CharField(max_length=150)
    slug = models.SlugField(max_length=80, unique=True)
    story = RichTextUploadingField(max_length=3000, help_text="The success story")
    edited_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, help_text="The person who create or edit the story")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.story_tagline[:15]}'
    
    class Meta:
        verbose_name = "Success Story"
        verbose_name_plural = "Success Stories"
    
    # def save(self, *args, **kwargs):
    #     account = Account.objects.filter(email=self.student_email)
    #     if account:
    #         self.student = account[0]
    #     else:
    #         raise ValidationError("This email does not belongs to any student. Please correct it.")
    #     super(SuccessStory, self).save(*args, **kwargs)
    
class StudentAdmissionTransactionInfo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    student = models.ForeignKey(Account, related_name="student_admission_transaction", on_delete=models.CASCADE, help_text="Student belongs to this transaction")
    transaction_id = models.CharField(max_length=10)
    added_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, help_text="The person who has added this transaction info")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.student.username
    

from django.core.exceptions import ValidationError

def validate_account_avatar_file_size(value):
    filesize= value.size
    
    if filesize > 5242880:
        raise ValidationError("Image size should be less than 5Mb.")
    else:
        return value

class Admission(models.Model):
    def get_student_admission_avatar_file_path(self, filename):
        return f'admission/{self.student.username}/{filename}'
    
    student = models.ForeignKey(Account, related_name="student_admission", on_delete=models.CASCADE, help_text="Student belongs to this admission")
    full_name = models.CharField(max_length=100)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    father_name = models.CharField(max_length=100) 
    mother_name = models.CharField(max_length=100)
    contact_number = models.CharField(validators=[RegexValidator(r'^(?:\+?88)?01[3-9]\d{8}$', message="Contact number must be entered in following formats: +8801757551134, 8801857871165 or 01915604232")],
                                      max_length = 14, blank=True,
                                      help_text="Supported Formats: +8801757551134, 8801757871165 or 01715604232")
    avatar = ProcessedImageField(upload_to=get_student_admission_avatar_file_path, 
                                 default="default/default_avatar.jpg",
                                 validators=[FileExtensionValidator( ['jpg','png']), validate_account_avatar_file_size],
                                 processors=[ResizeToFill(160, 160)],
                                 format='JPEG',
                                 options={'quality': 75})
    transaction_id = models.CharField(max_length=10, unique=True)
    national_id = models.IntegerField(blank=True, unique=True)
    birth_cirtificate_id = models.IntegerField(blank=True, unique=True)
    is_verified = models.BooleanField(default=False, help_text="admission is verified or not")
    is_checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

