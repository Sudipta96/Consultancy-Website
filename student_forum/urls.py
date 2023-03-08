from django.urls import path
from . import views

app_name = "student_forum"

urlpatterns = [
    path("student-feedback/", views.student_feedback_view, name="student_feedback"),
    path("student-admission/", views.student_admission_view, name="student_admission"),
    path("student-success-stories/", views.student_success_stories_view, name="student_success_stories"),
    path("student-success-stories/<str:story_slug>/", views.student_success_story_detail_view, name="student_success_story_detail"),
]