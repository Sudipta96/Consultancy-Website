from django.contrib import admin
from .models import Event, Program, Gallery
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


# Register your models here.
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('short_title', "content_type", "event_status", "edited_by", "created_at", "list_image_preview")
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ["edit_form_image_preview"]
    fieldsets = (
          ('Event Create/Edit Form', {'fields':('title',"slug","title_intro","image_thumbnail","edit_form_image_preview","content_type", "event_status", "event_url","description","event_date")}),
    )
    def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.image_thumbnail}" id="image-preview" style="width:75px; height:auto; border-radius:10%" alt="">')
    list_image_preview.short_description = _("Preview")
    
    def edit_form_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.image_thumbnail}" id="image-preview" style="max-width: 100px; max-height: 130px; min-width: 75px;min-height: 100px; alt="">')
    edit_form_image_preview.short_description = _("Preview")

    def save_model(self, request, obj, form, change):
        obj.edited_by = request.user
        super(EventAdmin, self).save_model(request, obj, form, change)

class GalleryInlineAdmin(admin.TabularInline):
     model = Gallery

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("name","number_of_images","updated_at")
    inlines = [
         GalleryInlineAdmin
    ]


