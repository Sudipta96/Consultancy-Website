from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("summery/", views.summery, name="summery"),
    path("university-list/", views.university_list_view, name="university_list"),
    path("company-list/", views.company_list_view, name="company_list"),
]