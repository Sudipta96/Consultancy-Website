from django.db import models
from accounts.models import Account

from django.core.validators import FileExtensionValidator
# from accounts.validators import validate_account_avatar_file_size
from django.core.exceptions import ValidationError

# to validate mobile number
# from django.core.validators import RegexValidator

# django ckeditor
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

# django-imagekit
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class Contact_Us(models.Model):
    name = models.CharField(max_length=200, help_text="Your full name")
    email = models.EmailField(verbose_name="email", max_length=60, help_text="Your email address")
    details = models.TextField(max_length=500, help_text="Tell us about your thoughts")
    checked = models.BooleanField(default=False, help_text="format:true means you have checked the contact message")
    received_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, help_text="User who has received the message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"


# to check resource person avatar image size
def validate_resource_person_avatar_file_size(value):
    filesize= value.size
    
    if filesize > 10485760:  # 10 mb in bytes
        raise ValidationError("Image size should be less than 10Mb.")
    else:
        return value


class ResourcePerson(models.Model):
    def get_resource_person_avatar_file_path(self, filename):
        status = self.get_person_status_display()
        return f'resource-persons/{status}/{filename}'
    
    RESOURCE_PERSON_STATUS_CHOICES = (
        ('M', "Managing Body"),
        ("F", "Parmanent Speaker"),
        ('G', "Guest Speaker"),
    )
    name = models.CharField(max_length=250, help_text="Full name")
    person_status = models.CharField(choices=RESOURCE_PERSON_STATUS_CHOICES, max_length=20)
    avatar = models.ImageField(upload_to=get_resource_person_avatar_file_path, 
                                default="default/default_avatar.jpg",
                                validators=[FileExtensionValidator( ['jpg','png']), validate_resource_person_avatar_file_size],    
                                help_text= "Supported Image Format: jpg and png. Max file size is 10mb."
                              )
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(160, 160)],
                                      format='JPEG',
                                      options={'quality': 75})
    
    organization_name = models.CharField(blank=True, max_length=200, help_text="Any other organization or university name where the person is associated or studied")
    organization_designation = models.CharField(blank=True, max_length=200, help_text="His/Her designation in that organization")
    description = RichTextField(max_length=1000, help_text="resource person bio or details")
    edited_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, help_text="User who has created or edit the form")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
      
    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Resource Person"
        verbose_name_plural = "Resource Persons"

class IndexSlider(models.Model):
    image = models.ImageField()
    heading = models.CharField(blank=True, max_length=35)
    short_note = models.CharField(blank=True, max_length=150)
    link = models.URLField(blank=True, max_length=200)
    link_text = models.CharField(blank=True, max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Index Slider"
    

class Icon(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class HeroSection(models.Model):
    PAGE_CHOICES = (
        ("PREAMBLE", "PREAMBLE"),
        ("WHAT-WE-ARE", "WHAT-WE-ARE"),
        ("WHAT-WE-DO", "WHAT-WE-DO"),
        ("OUR-VISION", "OUR-VISION"),
        ("OUR-MISSION", "OUR-MISSION"),
        ("OUR-TARGET-AUDIENCE", "OUR-TARGET-AUDIENCE"),
        ("OUR-AIM-OBJECTIVES", "OUR-AIM-OBJECTIVES"),
        ("OUR-STRATEGY", "OUR-STRATEGY"),
    )
    page = models.CharField(choices=PAGE_CHOICES, max_length=30, default="PREAMBLE")
    image = models.ImageField()
    heading = models.CharField(blank=True, max_length=35)
    short_note = models.CharField(blank=True, max_length=150)
    link = models.URLField(blank=True, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.page   
    
class Preamble(models.Model):
    tagline = models.CharField(max_length=100)
    index_page_image = models.ImageField(upload_to="pages/preamble", default="default/default_avatar.jpg")
    short_description = RichTextField(max_length=300, help_text="Preamble short description for index page")
    long_description = RichTextField(max_length=1000, help_text="Preamble detail description for single page")
    read_more = models.BooleanField(default=False, help_text="represents read more button")
    hero_section = models.ForeignKey(HeroSection, on_delete=models.PROTECT, related_name="preamble", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Preamble"

class WhatWeAre(models.Model):
    tagline = models.CharField(max_length=100)
    index_page_image = models.ImageField(upload_to="pages/what-we-are", default="default/default_avatar.jpg")
    short_description = RichTextField(max_length=300, help_text="short description for index page")
    long_description = RichTextField(max_length=1000, help_text="Detail description for single page")
    read_more = models.BooleanField(default=False, help_text="represents read more button")
    hero_section = models.ForeignKey(HeroSection, on_delete=models.PROTECT, related_name="what_we_are", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "What We Are"

   
class WhatWeDo(models.Model):
    read_more = models.BooleanField(default=False, help_text="represents read more button")
    long_description = RichTextUploadingField(blank=True, max_length=1000, help_text="Detail description for single page")
    hero_section = models.ForeignKey(HeroSection, on_delete=models.PROTECT, related_name="what_we_do", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "What We Do"

class WhatWeDoCardItem(models.Model):
    icon = models.ForeignKey(Icon, on_delete=models.PROTECT,related_name="what_we_do_icon")
    heading = models.CharField(max_length=50)
    short_note = models.TextField(max_length=255, help_text="Short Description")
    what_we_do = models.ForeignKey(WhatWeDo, on_delete=models.PROTECT, related_name="what_we_do_item")    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 




class OurVision(models.Model):
    tagline = models.CharField(max_length=100)
    index_page_image1 = models.ImageField(upload_to="pages/what-we-do", default="default/default_avatar.jpg")
    index_page_image2 = models.ImageField(upload_to="pages/what-we-do", default="default/default_avatar.jpg")
    index_page_image3 = models.ImageField(upload_to="pages/what-we-do", default="default/default_avatar.jpg")
    short_description = models.TextField(max_length=200, help_text="Short Description")
    long_description = RichTextUploadingField(max_length=1000, help_text="Detail description for single page")
    read_more = models.BooleanField(default=False, help_text="represents read more button")
    hero_section = models.ForeignKey(HeroSection, on_delete=models.PROTECT, related_name="our_vision", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Our Vision"
    
class OurMission(models.Model):
    tagline = models.CharField(max_length=100)
    index_page_image1 = models.ImageField(upload_to="pages/what-we-do", default="default/default_avatar.jpg")
    index_page_image2 = models.ImageField(upload_to="pages/what-we-do", default="default/default_avatar.jpg")
    index_page_image3 = models.ImageField(upload_to="pages/what-we-do", default="default/default_avatar.jpg")
    short_description = models.TextField(max_length=200, help_text="Short Description")
    long_description = RichTextUploadingField(max_length=1000, help_text="Detail description for single page")
    read_more = models.BooleanField(default=False, help_text="represents read more button")
    hero_section = models.ForeignKey(HeroSection, on_delete=models.PROTECT, related_name="our_mission", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Our Mission"
    

class OurTargetAudience(models.Model):
    hero_section = models.ForeignKey(HeroSection, on_delete=models.PROTECT, related_name="target_audience", blank=True, null=True)
    long_description = RichTextUploadingField(blank=True, max_length=1000, help_text="Detail description for single page")
    read_more = models.BooleanField(default=False, help_text="represents read more button")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Our Target Audience"

class TargetCardItem(models.Model):
    icon = models.ForeignKey(Icon, on_delete=models.PROTECT,related_name="target_item_icon")
    heading = models.CharField(max_length=50)
    short_note = models.TextField(max_length=255, help_text="Short Description")
    target = models.ForeignKey(OurTargetAudience, on_delete=models.PROTECT, related_name="target_item")    
    is_visible_in_index_page =  models.BooleanField(default=True, verbose_name="Index page visibility")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name 


class AimAndObjectives(models.Model):
    index_page_image = models.ImageField(upload_to="pages/what-we-do", default="default/default_avatar.jpg")
    short_listing = models.TextField(blank=True, max_length=200, help_text="Short Listing")
    long_description = RichTextUploadingField(blank=True, max_length=1000, help_text="Detail description for single page")
    hero_section = models.ForeignKey(HeroSection, on_delete=models.PROTECT, related_name="aim_objectives", blank=True, null=True)
    read_more = models.BooleanField(default=False, help_text="represents read more button")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "Aim & Objectives"

class AimItem(models.Model):
    aim_parent =  models.ForeignKey(AimAndObjectives,null=True, blank=True, on_delete=models.PROTECT, related_name="aim_item")
    aim =  models.CharField(max_length=255)

    def __str__(self):
        return "Aim Items"
    
class OurStrategy(models.Model):
    hero_section = models.ForeignKey(HeroSection, on_delete=models.PROTECT, related_name="our_strategy", blank=True, null=True)
    long_description = RichTextUploadingField(blank=True, max_length=1000, help_text="Detail description for single page")
    read_more = models.BooleanField(default=False, help_text="represents read more button")
    
    def __str__(self):
        return "Our Strategy"
    

class StrategyCardItem(models.Model):
    icon = models.ForeignKey(Icon, on_delete=models.PROTECT,related_name="strategy_item_icon")
    heading = models.CharField(max_length=50)
    short_note = models.TextField(max_length=255, help_text="Short Description")
    display_in_index = models.BooleanField(default=True, help_text="Format:True: Will display in index page or not")
    created_at = models.DateTimeField(auto_now_add=True)
    strategy = models.ForeignKey(OurStrategy, on_delete=models.PROTECT, related_name="strategy_item")    
    
    def __str__(self):
        return self.heading