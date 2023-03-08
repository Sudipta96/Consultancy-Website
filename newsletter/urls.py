from django.urls import path 
from .import views

app_name  = "newsletter"

urlpatterns = [
    path("upcoming-events/", views.upcoming_events_view, name="upcoming_events"),
    path("upcoming-events/<str:event_slug>/", views.upcoming_event_detail_view, name="upcoming_event_detail"),
    path("past-events/", views.past_events_view, name="past_events"),
    path("past-events/<str:event_slug>/", views.past_event_detail_view, name="past_event_detail"),
    path("gallery/", views.gallery, name="gallery"),
]