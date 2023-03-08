from django.shortcuts import render
from .models import Event, Program, Gallery
import datetime
from django.utils import timezone
# Create your views here.

def upcoming_events_view(request):
    # now = datetime.datetime.now()
    now = timezone.now()
    print(now)
    upcoming_events = Event.objects.filter(event_date__gte = now).order_by("event_date")
    featured_upcoming_events = Event.objects.filter(event_date__gte = now, is_featured=True)
    featured_event = featured_upcoming_events[0]
    print(featured_event)
    context = {
        "upcoming_events": upcoming_events,
        "featured_event": featured_event,
    }
    print(upcoming_events)
    return render(request, "newsletter/upcoming-events.html", context=context)


def past_events_view(request):
    now = datetime.datetime.now()
    past_events = Event.objects.filter(event_date__lte = now).order_by("event_date")
    print(past_events)
    context = {
        "past_events": past_events,
    }
    return render(request, "newsletter/past-events.html", context=context)

def upcoming_event_detail_view(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    context = {
        "event": event,
    }
    return render(request, "newsletter/event-detail.html", context=context)

def past_event_detail_view(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    context = {
        "event": event,
    }
    return render(request, "newsletter/event-detail.html", context=context)

def gallery(request):
    programs = Program.objects.all()
    # Gallery.objects.all()
    context = {
        "programs": programs,
    }
    return render(request, 'newsletter/gallery.html',context=context)