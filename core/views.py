from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from .forms import ContactUsForm
# Create your views here.
def index(request):
    preamble_obj = Preamble.objects.latest("id")
    what_we_are_obj = WhatWeAre.objects.latest("id")
    what_we_do_obj = WhatWeDo.objects.latest("id")
    our_vision_obj = OurVision.objects.latest("id")
    our_mission_obj = OurMission.objects.latest("id")
    our_target_audience_obj = OurTargetAudience.objects.latest("id")
    our_aim_obj = AimAndObjectives.objects.latest("id")
    our_strategy_obj = OurStrategy.objects.latest("id")
    context = {
        "preamble_obj": preamble_obj,
        "what_we_are_obj": what_we_are_obj,
        "what_we_do_obj": what_we_do_obj,
        "our_vision_obj": our_vision_obj,
        "our_mission_obj": our_mission_obj,
        "our_target_audience_obj": our_target_audience_obj,
        "our_aim_obj": our_aim_obj,
        "our_strategy_obj": our_strategy_obj,
    }
    return render(request, "index.html", context=context)

def preamble_view(request):
    preamble_obj = Preamble.objects.latest("id")
    context = {
       "preamble_obj": preamble_obj,
    }
    return render(request, "about-us/preamble.html", context=context)

def what_we_are_view(request):
    what_we_are_obj = WhatWeAre.objects.latest("id")
    context = {
        "what_we_are_obj": what_we_are_obj,
    }
    return render(request, "about-us/what-we-are.html", context=context)

def what_we_do_view(request):
    what_we_do_obj = WhatWeDo.objects.latest("id")
    context = {
        "what_we_do_obj": what_we_do_obj,
    }
    return render(request, "about-us/what-we-do.html", context=context)


def our_vision_view(request):
    our_vision_obj = OurVision.objects.latest("id")
    context = {
        "our_vision_obj": our_vision_obj,
    }
    return render(request, "about-us/our-vision.html", context=context)

def our_mission_view(request):
    our_mission_obj = OurMission.objects.latest("id")
    context = {
        "our_mission_obj": our_mission_obj,
    }
    return render(request, "about-us/our-mission.html", context=context)


def our_target_audience_view(request):
    our_target_audience_obj = OurTargetAudience.objects.latest("id")
    context = {
        "our_target_audience_obj": our_target_audience_obj,
    }
    return render(request, "about-us/our-target-audience.html", context=context)

def our_aim_objectives_view(request):
    our_aim_obj = AimAndObjectives.objects.latest("id")
    context = {
        "our_aim_obj": our_aim_obj,
    }
    return render(request, "about-us/our-aim-objectives.html", context=context)

def our_strategy_view(request):
    our_strategy_obj = OurStrategy.objects.latest("id")
    context = {
        "our_strategy_obj": our_strategy_obj,
    }
    return render(request, "about-us/our-strategy.html", context=context)

def managing_body_view(request):
    managing_body = ResourcePerson.objects.filter(person_status="M")
    print(managing_body)
    hero_section_qs = HeroSection.objects.filter(slug="managing-body")
    if hero_section_qs:
        hero_section = hero_section_qs[0]
    else:
        hero_section = None
    context = {
      "managing_body": managing_body,
      "hero_section": hero_section,
    }
    return render(request, "resource-persons/managing-body.html",context=context)

def parmanent_speaker_view(request):
    parmanent_speakers = ResourcePerson.objects.filter(person_status="P")
    print(parmanent_speakers)
    hero_section_qs = HeroSection.objects.filter(slug="parmanent-speakers")
    if hero_section_qs:
        hero_section = hero_section_qs[0]
    else:
        hero_section = None

    context = {
      "parmanent_speakers": parmanent_speakers,
      "hero_section": hero_section,
    }
    return render(request, "resource-persons/parmanent-speakers.html",context=context)

def guest_speaker_view(request):
    guest_speakers = ResourcePerson.objects.filter(person_status="G")
    print(guest_speakers)
    hero_section_qs = HeroSection.objects.filter(slug="guest-speakers")
    if hero_section_qs:
        hero_section = hero_section_qs[0]
    else:
        hero_section = None
    context = {
      "guest_speakers": guest_speakers,
      "hero_section": hero_section,
    }
    return render(request, "resource-persons/guest-speakers.html",context=context)

def contact_us_view(request):
    context = {}
    if request.method == "POST":
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            print("form is valid")
            contact_form.save()
            messages.success(request, "Your message is received successfully")
            return redirect("core:contact_us")
        else:
            print(contact_form.errors)
            messages.warning(request, "Your submitted data is not valid. Please try again..")
            context["contact_form"] = contact_form
    return render(request, "contact/contact-us.html", context=context)