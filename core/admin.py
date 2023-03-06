from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
# to support svg image
# from django_svg_image_form_field import SvgAndImageFormField
from django import forms
# Register your models here.

admin.site.register(Page)

# class SvgImageForm(forms.ModelForm):
#     class Meta:
#         model = Icon
#         exclude = []
#         field_classes = {
#             'image': SvgAndImageFormField,
#         }

@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
     list_display = ("name", "created_at")
     # form = SvgImageForm

@admin.register(IndexSlider)
class IndexSliderAdmin(admin.ModelAdmin):
     list_display = ("heading", "created_at", "list_image_preview")
     readonly_fields = ["image_preview"]
     fieldsets = (
          ('Slider Edit Form', {'fields':("heading", "image", "image_preview", "short_note", "link", "link_text")}),
      )
     def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.image}" id="image-preview" style="width:150px; height:auto; border-radius:15px;" alt="">')
     list_image_preview.short_description = _("Preview")

     def image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.image}" id="image-preview" style="width:150px; height:auto;" alt="">')
     image_preview.short_description = _("Preview")


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('page_name',)}
    fields = ["page_name", "slug", "image", "heading", "short_note", "link", "link_text",]
         
class HeroSectionAdminInline(admin.StackedInline):
     model = HeroSection
     extra = 0

@admin.register(Preamble)
class PreambleAdmin(admin.ModelAdmin):
     list_display = ("tagline","read_more","created_at","list_image_preview")
     readonly_fields = ["image_preview"]
     fields = ["tagline", "index_page_image", "image_preview", "short_description", "long_description", "read_more", "hero_section"]
     
     
     def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image}" id="image-preview" style="width:100px; height:auto; border-radius:15px;" alt="">')
     list_image_preview.short_description = _("Preview")

     def image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image}" id="image-preview" style="width:150px; height:auto;" alt="">')
     image_preview.short_description = _("Preview")

@admin.register(WhatWeAre)
class WhatWeAreAdmin(admin.ModelAdmin):
     list_display = ("tagline","read_more","created_at","list_image_preview")
     readonly_fields = ["image_preview"]
     fieldsets = (
          ('Preamble Edit Form', {'fields':("tagline", "index_page_image", "image_preview", "short_description", "long_description", "read_more")}),
      )
     
     def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image}" id="image-preview" style="width:100px; height:auto; border-radius:15px;" alt="">')
     list_image_preview.short_description = _("Preview")

     def image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image}" id="image-preview" style="width:150px; height:auto;" alt="">')
     image_preview.short_description = _("Preview")

#      inlines = [
#           HeroSectionAdminInline
#       ]
     

class WhatWeDoCardItemAdminInline(admin.TabularInline):
     model = WhatWeDoCardItem
 

@admin.register(WhatWeDo)
class WhatWeDoAdmin(admin.ModelAdmin):
     inlines = [WhatWeDoCardItemAdminInline,]
     readonly_fields = ["what_we_do_item_inline"]
     fieldsets = (
          ('', {'fields':("what_we_do_item_inline", "read_more")}),
          ('Want to Add Hero Section-For Detail Page', {'fields':("hero_section", "long_description",)}),
        )
     class Media:
          css = { 'all' : ['css/custom_admin.css'], }

     def what_we_do_item_inline(self, *args, **kwargs):
          context = getattr(self.response, 'context_data', None) or {}
          inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
          return get_template(inline.opts.template).render(context, self.request)

     def render_change_form(self, request, *args, **kwargs):
          self.request = request
          self.response = super().render_change_form(request, *args, **kwargs)
          return self.response


     

@admin.register(OurVision)
class OurVisionAdmin(admin.ModelAdmin):
     list_display = ("tagline", "created_at","list_image_preview")
     readonly_fields = ["image_preview_1", "image_preview_2", "image_preview_3"]
     
     fieldsets = (
          ('Our Vision Edit Form', {'fields':("tagline", "short_description", "long_description", "index_page_image1","image_preview_1", "index_page_image2","image_preview_2", "index_page_image3", "image_preview_3", "read_more", "hero_section",)}),
      )
     
     def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image1}" id="image-preview" style="width:100px; height:auto; border-radius:15px;" alt="">')
     list_image_preview.short_description = _("Preview")

     def image_preview_1(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image1}" id="image-preview" style="width:150px; height:auto; border-radius:15px;" alt="">')
     image_preview_1.short_description = _("Preview")

     def image_preview_2(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image2}" id="image-preview" style="width:150px; height:auto; border-radius:15px;" alt="">')
     image_preview_2.short_description = _("Preview")

     def image_preview_3(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image3}" id="image-preview" style="width:150px; height:auto; border-radius:15px;" alt="">')
     image_preview_3.short_description = _("Preview")

@admin.register(OurMission)
class OurMissionAdmin(admin.ModelAdmin):
     list_display = ("tagline", "created_at","list_image_preview")
     readonly_fields = ["index_page_side_image_preview",]
     
     fieldsets = (
          ('Our Vision Edit Form', {'fields':("tagline", "short_description", "long_description", "index_page_side_image", "index_page_side_image_preview", "read_more", "hero_section",)}),
      )
     
     def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_side_image}" id="image-preview" style="width:100px; height:auto; border-radius:15px;" alt="">')
     list_image_preview.short_description = _("Preview")

     def index_page_side_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_side_image}" id="image-preview" style="width:150px; height:auto; border-radius:15px;" alt="">')
     index_page_side_image_preview.short_description = _("Preview")

     # def image_preview_2(self, obj):
     #      return mark_safe(f'<img src="/media/{obj.index_page_image2}" id="image-preview" style="width:150px; height:auto; border-radius:15px;" alt="">')
     # image_preview_2.short_description = _("Preview")

     # def image_preview_3(self, obj):
     #      return mark_safe(f'<img src="/media/{obj.index_page_image3}" id="image-preview" style="width:150px; height:auto; border-radius:15px;" alt="">')
     # image_preview_3.short_description = _("Preview")


class TargetCardItemAdminInline(admin.TabularInline):
     model = TargetCardItem
     extra = 3

@admin.register(OurTargetAudience)
class OurTargetAudienceAdmin(admin.ModelAdmin):
     inlines = [TargetCardItemAdminInline,]
     readonly_fields = ["target_item_inline"]
     fieldsets = (
          ('', {'fields':("target_item_inline", "read_more")}),
          ('Want to Add Hero Section-For Target Audience Detail Page', {'fields':("hero_section", "long_description",)}),
        )
     class Media:
          css = { 'all' : ['css/custom_admin.css'], }

     def target_item_inline(self, *args, **kwargs):
          context = getattr(self.response, 'context_data', None) or {}
          inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
          return get_template(inline.opts.template).render(context, self.request)

     def render_change_form(self, request, *args, **kwargs):
          self.request = request
          self.response = super().render_change_form(request, *args, **kwargs)
          return self.response



class AimItemAdminInline(admin.TabularInline):
     model = AimItem


@admin.register(AimAndObjectives)
class AimAndObjectivesAdmin(admin.ModelAdmin):
     inlines = [AimItemAdminInline,]
     readonly_fields = ["aim_item_inline","image_preview"]
     fieldsets = (
          ('', {'fields':("aim_item_inline",)}),
          ('Other Options', {'fields':("index_page_image", "image_preview", "read_more",)}),
          ('Want to Add Hero Section-For Detail Page', {'fields':("hero_section", "long_description",)}),
        )
     class Media:
          css = { 'all' : ['css/custom_admin.css'], }

     def image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.index_page_image}" id="image-preview" style="width:150px; height:auto; border-radius:15px;" alt="">')
     image_preview.short_description = _("Preview")

     def aim_item_inline(self, *args, **kwargs):
          context = getattr(self.response, 'context_data', None) or {}
          inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
          return get_template(inline.opts.template).render(context, self.request)

     def render_change_form(self, request, *args, **kwargs):
          self.request = request
          self.response = super().render_change_form(request, *args, **kwargs)
          return self.response

class StrategyCardItemAdminInline(admin.TabularInline):
     model = StrategyCardItem


from django.template.loader import get_template
@admin.register(OurStrategy)
class OurStrategyAdmin(admin.ModelAdmin):
        inlines = (StrategyCardItemAdminInline,)
        fields = ('strategy_item_inline', "long_description", "read_more", "hero_section")
        readonly_fields= ('strategy_item_inline',)  # we set the method as readonly field
        
        class Media:
             css = { 'all' : ['css/custom_admin.css'], }

        def strategy_item_inline(self, *args, **kwargs):
          context = getattr(self.response, 'context_data', None) or {}
          inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop(0)
          return get_template(inline.opts.template).render(context, self.request)

        def render_change_form(self, request, *args, **kwargs):
          self.request = request
          self.response = super().render_change_form(request, *args, **kwargs)
          return self.response
        
        
       
@admin.register(Contact_Us)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "checked", "received_by", "created_at")
    fieldsets = (
          ('Contact Message', {'fields':("name","email","details","checked")}),
     )
    
    def save_model(self, request, obj, form, change):
        obj.received_by = request.user
        super(ContactUsAdmin, self).save_model(request, obj, form, change)

@admin.register(ResourcePerson)
class ResoucePersonAdmin(admin.ModelAdmin):
    list_display = ("name", "person_status","edited_by","updated_at","list_image_preview")
    readonly_fields = ["image_preview"]
    fieldsets = (
          ('Person Details', {'fields':("name", "person_status","avatar","image_preview", "description","organization_name","organization_designation")}),
    )
    def save_model(self, request, obj, form, change):
        obj.edited_by = request.user
        super(ResoucePersonAdmin, self).save_model(request, obj, form, change)
    
    def list_image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.avatar}" id="image-preview" style="width:75px; height:auto; border-radius:10%" alt="">')
    list_image_preview.short_description = _("Preview")

    def image_preview(self, obj):
          return mark_safe(f'<img src="/media/{obj.avatar}" id="image-preview" style="max-width: 100px; max-height: 130px; min-width: 75px;min-height: 100px; alt="">')
    image_preview.short_description = _("Preview")
