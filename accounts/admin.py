from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
# Register your models here.

@admin.register(Account)
class CustomAccountAdmin(UserAdmin):
     search_fields = ('email','username')
     list_display = ("id", 'email','username','is_active','is_staff','last_login',"date_joined", "list_image_preview")
 
     list_filter = ('email','username','is_active','is_staff')
     ordering = ('username',)
     readonly_fields = ["image_preview"]
     fieldsets = (
          ('User Info', {'fields':('email', 'first_name', "last_name", 'username', "gender", 'contact_number', 'avatar', "image_preview")}),
          ('Permissions', {'fields':('is_staff','is_active', "user_permissions"),}),
     )
     # 'groups' -- use this keyword in fieldset to add group field 
     add_fieldsets = (
          (None, {
               'classes': ('wide',),
               'fields': ('username','email','password1','password2')}
          ),
     )
     def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.avatar}" id="image-preview" style="max-width: 50px; max-height: 75px; min-width: 25px;min-height: 35px; border-radius:50%" alt="">')
     list_image_preview.short_description = _("Preview")

     def image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.avatar}" id="image-preview" style="max-width: 100px; max-height: 130px; min-width: 75px;min-height: 100px; alt="">')
     image_preview.short_description = _("Preview")


admin.site.register(Address)