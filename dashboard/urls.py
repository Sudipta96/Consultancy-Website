from django.urls import path
from . import views

urlpatterns = [
    path("university-list/", views.university_list_view, name="university_list"),
    path("company-list/", views.company_list_view, name="company_list"),
]