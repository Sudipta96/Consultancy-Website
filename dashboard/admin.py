from django.contrib import admin
from .models import RegistrationInfo, AdmissionInfo,StudentsPerUniversityInfo, StudentsPerCompanyInfo
# Register your models here.

@admin.register(RegistrationInfo)
class RegistrationInfoAdmin(admin.ModelAdmin):
    list_display = ("current_month", "current_year", "number_of_students")
    
@admin.register(AdmissionInfo)
class AdmissionInfoAdmin(admin.ModelAdmin):
    list_display = ("current_month", "current_year", "number_of_students")

@admin.register(StudentsPerUniversityInfo)
class StudentsPerUniversityInfoAdmin(admin.ModelAdmin):
    list_display = ("university", "number_of_students")

@admin.register(StudentsPerCompanyInfo)
class StudentsPerCompanyInfoAdmin(admin.ModelAdmin):
    list_display = ("company", "current_year", "number_of_students")

