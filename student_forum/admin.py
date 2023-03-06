from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
# Register your models here.




# # admin.site.register(StudentFeedback)
@admin.register(StudentFeedback)
class StudentFeedbackAdmin(admin.ModelAdmin):
    list_display = ( "rating", "will_be_displayed","created_at")

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
     list_display = ("name", "number_of_students")

@admin.register(CompanyInternship)
class CompanyInternshipAdminn(admin.ModelAdmin):
     list_display = ("company", "student", "created_at")


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ("student", "company", "updated_at", "edited_by", "list_image_preview")
    autocomplete_fields = ['student']
    prepopulated_fields = {'slug': ('story_tagline',)}
    readonly_fields = ["image_thumbnail_preview"]
    fieldsets = (
          ('Story Details', {'fields':("story_tagline","slug","image_thumbnail","image_thumbnail_preview","card_intro","story", )}),
          ('Person Details', {'fields':('student', "student_bio", "company",)}), 
    )    
    def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.image_thumbnail}" id="image-preview" style="width:75px; height:auto; border-radius:10%" alt="">')
    list_image_preview.short_description = _("Preview")
    
    def image_thumbnail_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.image_thumbnail}" id="image-preview" style="max-width: 100px; max-height: 130px; min-width: 75px;min-height: 100px; alt="">')
    image_thumbnail_preview.short_description = _("Preview")

    def save_model(self, request, obj, form, change):
        obj.edited_by = request.user
        super(SuccessStoryAdmin, self).save_model(request, obj, form, change)
    
admin.site.register(Admission)