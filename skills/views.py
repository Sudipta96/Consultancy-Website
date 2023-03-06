from django.shortcuts import render
from .models import *

# Create your views here.
def course_list_view(request,cat_slug):
    category_qs = Category.objects.filter(slug=cat_slug)
    context = {}
    if category_qs:
       category = category_qs[0]
       courses = Course.objects.filter(category=category)
       context["category"] = category
       context["courses"] = courses
    return render(request, "skills/course-list.html", context=context)

def course_overview(request, cat_slug, course_slug):
    category_qs = Category.objects.filter(slug=cat_slug)
    context = {}
    if category_qs:
       category = category_qs[0]
       course = Course.objects.filter(slug=course_slug, category=category)[0]
       context["category"] = category
       context["course"] = course
    return render(request, "skills/course-overview.html", context=context)


def free_resources(request):
    # resources = FreeResources.objects.all()
    courses = Course.objects.all()
    print(courses)
    context = {
        # "resources": resources,
        "courses": courses,
    }
    return render(request, "skills/free-resources.html", context=context)

