from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(SSCEquivalentExamName)
admin.site.register(GroupName)
admin.site.register(SSCInfo)
admin.site.register(HSCEquivalentExamName)
admin.site.register(HSCInfo)

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
     list_display = ("name", "short_name", "number_of_students")

@admin.register(StudentCurrentEducationInfo)
class StudentCurrentEducationInfoAdmin(admin.ModelAdmin):
     list_display = ("account", "exam_name", "subject", "which_year_student", "university")

admin.site.register(Subject)
admin.site.register(GraduationExamName)
admin.site.register(PostGraduationExamName)
admin.site.register(GraduationInfo)
admin.site.register(PostGraduationInfo)
admin.site.register(Certificate)
