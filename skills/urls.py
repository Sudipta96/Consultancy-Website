from django.urls import path 
from . import views

app_name = "skills"

urlpatterns = [

    path('<str:cat_slug>/', views.course_list_view, name="course_list"),
    path('<str:cat_slug>/<str:course_slug>', views.course_overview, name="course_overview"),
    path("resource/free-resources/", views.free_resources, name="free-resources"),
    # path('computer-skills/', views.computer_skills, name="computer-skills"),
    # path('communication-skills/', views.communication_skills, name="communication-skills"),
    # path('mental-health/', views.mental_health, name="mental-health"),
    # path('soft-skills/course-detail/', views.soft_skills, name="course-detail"),
    # path('free-courses/', views.free_courses, name="free-courses"),
    # path('free-resources/', views.free_resources, name="free-resources"),
]