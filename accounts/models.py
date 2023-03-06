from django.db import models
import uuid
# Create custom user model
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from django.core.mail import send_mail

from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator, FileExtensionValidator
from .validators import validate_account_avatar_file_size

# to validate mobile number
from django.core.validators import RegexValidator

# django imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class CustomAccountManager(BaseUserManager):

     """ A custom Manager to deal with email as unique identifier """
     def create_user(self, email, username, password, **extra_fields):

         """ Creates and saves a user with a given email and password """
         if not email:
              raise ValueError("The Email must be set!")

         email = self.normalize_email(email)
         user = self.model(email=email, username=username, **extra_fields)
         user.set_password(password)
         user.save(using=self._db)
         return user

     def create_staffuser(self, email, username, password, **extra_fields):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email, username,
            password=password,
            **extra_fields
        )
        user.staff = True
        user.save(using=self._db)
        return user
     
     def create_studentuser(self, email, username, password, **extra_fields):

        """
        Creates and saves a student user with the given email and password.
        """
        extra_fields.setdefault('is_student', True)
        
        if extra_fields.get('is_student') is not True:
             raise ValueError("Superuser must have is_student=True")
        if extra_fields.get('is_staff') is True:
             raise ValueError("Student must have is_staff=False")
        if extra_fields.get('is_superuser') is True:
             raise ValueError("Student must have is_superuser=False")
        return self.create_user(email, username, password, **extra_fields)

     def create_superuser(self, email, username, password, **extra_fields):
         extra_fields.setdefault('is_staff', True)
         extra_fields.setdefault('is_superuser', True)
         extra_fields.setdefault('is_active', True)

         if extra_fields.get('is_staff') is not True:
             raise ValueError("Superuser must have is_staff=True")
         if extra_fields.get('is_superuser') is not True:
             raise ValueError("Superuser must have is_superuser=True")
         return self.create_user(email, username, password, **extra_fields)


class Account(AbstractBaseUser, PermissionsMixin):
    def get_account_avatar_file_path(self, filename):
        return f'accounts/{self.username}/avatar/{filename}'
    
    GENDER_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHERS', 'OTHERS'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    fullname = models.CharField(max_length=200, help_text="Full Name")
    username = models.CharField(max_length=200, help_text="Username should be unique")
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    contact_number = models.CharField(validators=[RegexValidator(r'^(?:\+?88)?01[3-9]\d{8}$', message="Contact number must be entered in following formats: +8801757551134, 8801857871165 or 01915604232")],
                                      max_length = 14, blank=True,
                                      help_text="Supported Formats: +8801757551134, 8801757871165 or 01715604232")
    avatar = ProcessedImageField(upload_to=get_account_avatar_file_path, 
                                 default="default/default_avatar.jpg",
                                 validators=[FileExtensionValidator( ['jpg','png']), validate_account_avatar_file_size],
                                 processors=[ResizeToFill(160, 160)],
                                 format='JPEG',
                                 options={'quality': 75})
    bio = models.TextField(blank=True, max_length=400, help_text="account owner bio") 
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    is_student = models.BooleanField(
                _('student status'),
                default=False,
                help_text= _('Designates whether the user is student or not.')
    )
    is_staff = models.BooleanField(
                _('staff status'),
                default=False,
                help_text= _('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
                      _('active'),
                      default=True,
                      help_text= _('Designate whether this user should be treated as active.\
                                Unselect this instead of deleting accounts')

    )
    
    is_superuser = models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    email_confirmed = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomAccountManager()

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.username

    # methods belongs to User
    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
    

class Address(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="account_address")
    address_line = models.CharField(max_length=255, help_text="Road/Village/Town/House Info")
    district = models.CharField(max_length=100, help_text="District Name")
    upazilla = models.CharField(max_length=100, help_text="Upazilla Name")
    postal_code = models.IntegerField(blank=True, validators=[MinValueValidator(1000), MaxValueValidator(9350)])

    def __str__(self):
        return self.account.username
