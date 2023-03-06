from django.urls import path
from . import views

app_name = "student_forum"

urlpatterns = [
    path("student-feedback", views.student_feedback_view, name="student_feedback"),
]