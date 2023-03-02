from django.db import models


# for validation
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from .validators import validate_file_size

from django.utils.text import slugify

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# django-imagekit
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from accounts.models import Account


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, help_text="Category name for course")
    description = models.TextField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

# to check resource person avatar image size
def validate_image_thumbnail_file_size(value):
    filesize= value.size

    if filesize > 5242880:  # 5 mb in bytes
        raise ValidationError("Image size should be less than 5Mb.")
    else:
        return value

class Course(models.Model):
    def get_image_thumbnail_file_path(self, filename):
        return f'courses/{self.name}/image-thumbnail/{filename}'
    
    def get_preview_video_file_path(self, filename):
        return f'courses/{self.name}/preview-video/{filename}'
    
    name = models.CharField(max_length=255, unique=True, help_text="Required: course name")
    slug = models.SlugField(max_length=200, unique=True, verbose_name=("course safe URL"))
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="course_category")
    total_duration = models.CharField(max_length=50, help_text="Required: course duration in hours/minutes or in weeks/months format")
    image_thumbnail = ProcessedImageField(upload_to=get_image_thumbnail_file_path,
                                default="default/default_card.jpg",
                                validators=[FileExtensionValidator( ['jpg','png']), validate_image_thumbnail_file_size],
                                processors=[ResizeToFill(480, 320)],
                                format='JPEG',
                                options={'quality': 80},
                                help_text="This image will be displayed in list view card")
    title_intro = RichTextField(max_length=300, help_text="Required: title introduction - maximum  3 to 4 lines")
    what_you_will_learn = RichTextUploadingField(max_length=1000, help_text="Required: what you will learn content - maximum 1000 characters")
    description =  RichTextUploadingField(max_length=3000, help_text="Required: Long Description - maximum 3000 characters")
    preview_video_file = models.FileField(null=True, blank=True, validators=[FileExtensionValidator( ['mp4']), validate_file_size], 
                                          help_text="Course preview video. Supported file format: mp4. Maximum file limit:20mb")
    preview_video_url = models.URLField(max_length = 200, blank=True, help_text="preview video url like youtube video url.")
    is_active = models.BooleanField(
        default=True,
        verbose_name=("course visibility"),
        help_text=("format: true=course visible"),
    )
    edited_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, help_text="User who create or edit the course")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def save(self):
    #     self.slug = slugify(self.name)
    #     super(Course, self).save()

    def __str__(self):
        return self.name
    
class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_chapter", 
                                       help_text="Required: Choose the course name. \
                                                  N.B: If you delete the course, related course chapters will be automatically deleted")
    chapter_name = models.CharField(max_length=100, help_text="Required:Chapter name")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.course.name}-{self.chapter_name}'

class FreeResources(models.Model):
    def get_resource_file_path(self, filename):
        return f'course/{self.course.name}/resources/{filename}'
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_resource", 
                                       help_text="Required: Choose the course name. \
                                                  N.B: If you delete the course, related course resources will be automatically deleted")
    text = models.CharField(max_length=200, blank=True, help_text="Resource url text")
    resource_url = models.URLField(max_length = 200, blank=True, help_text="Resource url or link. If you add url dont upload file.")
    resource_file = models.FileField(null=True, blank=True, upload_to=get_resource_file_path, validators=[FileExtensionValidator( ['pdf']), validate_file_size], 
                                     help_text="Resource file.If you upload file,don't add resource_file url. Supported file format: pdf. Maximum file limit:20mb")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Resource: {self.course.name}'

    





    