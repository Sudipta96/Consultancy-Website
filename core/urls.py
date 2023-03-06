from django.urls import path 
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="home"),
    path("about-us/preamble", views.preamble_view, name="preamble"),
    path("about-us/what-we-are", views.what_we_are_view, name="what_we_are"),
    path("about-us/what-we-do", views.what_we_do_view, name="what_we_do"),
    path("about-us/our-vision", views.our_vision_view, name="our_vision"),
    path("about-us/our-mission", views.our_mission_view, name="our_mission"),
    path("about-us/our-target-audience", views.our_target_audience_view, name="our_target_audience"),
    path("about-us/our-aim-objectives", views.our_aim_objectives_view, name="our_aim_objectives"),
    path("about-us/our-strategy", views.our_strategy_view, name="our_strategy"),
    
    path("resource-persons/managing-body", views.managing_body_view, name="managing-body"),
    path("resource-persons/parmanent-speakers", views.parmanent_speaker_view, name="parmanent-speakers"),
    path("resource-persons/guest-speakers", views.guest_speaker_view, name="guest-speakers"),
    path("contact-us/", views.contact_us_view, name="contact_us"),
    
]