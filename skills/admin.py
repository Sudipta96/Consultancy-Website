from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ["name", "slug", "description", "is_active", "hero_section"]
     

class ChapterInline(admin.TabularInline):
    model = Chapter
    fieldsets = (
          ('Course Chapter', {'fields':("chapter_name",)}),
    )

class FreeResourcesInline(admin.TabularInline):
    model = FreeResources

class LearningItemAdminInline(admin.TabularInline):
     model = LearningItem

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "edited_by", "updated_at","list_image_preview")
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ["edit_form_image_preview"]
    fieldsets = (
          ('Course Editing Form', {'fields':("name", "slug","category","image_thumbnail","edit_form_image_preview","number_of_lectures", "total_duration", "title_intro", "what_you_will_learn", "description","preview_video_file", "preview_video_url", "is_active")}),
    )
    def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.image_thumbnail}" id="image-preview" style="width:100px; height:auto; max-height: 130px; border-radius:10%" alt="">')
    list_image_preview.short_description = _("Preview")
    
    def edit_form_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.image_thumbnail}" id="image-preview" style="width: 150px; height:auto; max-height: 200px;  alt="">')
    edit_form_image_preview.short_description = _("Preview")

    def save_model(self, request, obj, form, change):
        obj.edited_by = request.user
        super(CourseAdmin, self).save_model(request, obj, form, change)
    
    inlines = [
      LearningItemAdminInline, ChapterInline, FreeResourcesInline
    ]


    