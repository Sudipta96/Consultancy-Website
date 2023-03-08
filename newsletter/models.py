from django.db import models
from accounts.models import Account

from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

from ckeditor_uploader.fields import RichTextUploadingField


# django-imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.

# to check resource person avatar image size
def validate_image_thumbnail_file_size(value):
    filesize= value.size

    if filesize > 5242880:  # 5 mb in bytes
        raise ValidationError("Image size should be less than 5Mb.")
    else:
        return value
    
class Event(models.Model):
    def get_image_thumbnail_file_path(self, filename):
        return f'newsletter/events/{self.slug}/image-thumbnail/{filename}'
    
    CONTENT_TYPE_CHOICES = (
        ("Link", "Link"),
        ("Blog", "Blog"),
    )

    EVENT_STATUS_CHOICES = (
        ("Current", "Current"),
        ("Upcoming", "Upcoming"),
    )

    title = models.CharField(max_length=150, help_text="News or Event Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name=("course safe URL"), help_text="Slug should be unique. Slug will be automatically created from title. No need to edit slug field and keep the title unique to create unique slug.")
    title_intro = models.TextField(max_length=300, help_text="Small description will be displayed in list card.")
    image_thumbnail = ProcessedImageField(upload_to=get_image_thumbnail_file_path,
                                default="default/default_card.jpg",
                                validators=[FileExtensionValidator( ['jpg','png']), validate_image_thumbnail_file_size],
                                processors=[ResizeToFill(480, 320)],
                                format='JPEG',
                                options={'quality': 80},
                                help_text="This image will be displayed in list view card")
    content_type = models.CharField(choices=CONTENT_TYPE_CHOICES, max_length=20)
    # event_status = models.CharField(choices=EVENT_STATUS_CHOICES, max_length=20)
    event_url = models.URLField(max_length = 255, blank=True, help_text="Event Outside URl. If you fill this, keep description empty.")
    event_date = models.DateTimeField(null=True,blank=True,help_text="Current or upcoming event date")
    venue = models.CharField(blank=True, max_length=100, help_text="Venue")
    description = RichTextUploadingField(blank=True, max_length=3000, help_text="Maximum 3000 characters. Event or News Blog Description.If you fill this, keep event url empty.")
    is_featured = models.BooleanField(default=False, help_text="display in head section in event page")
    edited_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, help_text="User who create or edit the news or event")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    @property
    def short_title(self):
        return self.title if len(self.title) < 30 else (self.title[:30] + '...')
    
    def clean(self):
        if self.content_type == "Link" and self.event_url == "":
            raise ValidationError("Please add event url because you choose content type is link")
        if self.content_type == "Link" and self.description != "":
            raise ValidationError("Please remove description because you choose content_type is link")
        if self.content_type == "Blog" and self.description == "":
            raise ValidationError("Please add description because you choose content type is blog")
        if self.content_type == "Blog" and self.event_url != "":
            raise ValidationError("Please remove event url because you choose content_type is blog")
        super(Event, self).clean()
        
class Program(models.Model):
    name = models.CharField(max_length=150, help_text="Program or event name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    @property
    def number_of_images(self):
        return len(self.program_gallery.all())

class Gallery(models.Model):
    def get_image_thumbnail_file_path(self, filename):
        return f'newsletter/gallery/{self.program.name}/{filename}'
    
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="program_gallery")
    image1 = ProcessedImageField(upload_to=get_image_thumbnail_file_path,
                                default="default/default_card.jpg",
                                validators=[FileExtensionValidator( ['jpg','png']), validate_image_thumbnail_file_size],
                                processors=[ResizeToFill(480, 320)],
                                format='JPEG',
                                options={'quality': 80},
                                help_text="This image will be displayed in gallery")
    
    image2 = ProcessedImageField(upload_to=get_image_thumbnail_file_path,
                                default="default/default_card.jpg",
                                validators=[FileExtensionValidator( ['jpg','png']), validate_image_thumbnail_file_size],
                                processors=[ResizeToFill(480, 320)],
                                format='JPEG', 
                                options={'quality': 80},
                                help_text="This image will be displayed in gallery")
    
    image3 = ProcessedImageField(upload_to=get_image_thumbnail_file_path,
                                default="default/default_card.jpg",
                                validators=[FileExtensionValidator( ['jpg','png']), validate_image_thumbnail_file_size],
                                processors=[ResizeToFill(480, 320)],
                                format='JPEG', 
                                options={'quality': 80},
                                help_text="This image will be displayed in gallery")
    # caption = models.CharField(max_length=150,default="galllery image", help_text="Image caption")
    # is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.program.name} - {self.caption}"
    
    
    
    

    
    