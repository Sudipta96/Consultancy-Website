from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, "index.html", context=context)

def soft_skills(request):
    context = {}
    return render(request, "skills/soft-skills.html", context=context)

def computer_skills(request):
    context = {}
    return render(request, "skills/computer-skills.html", context=context)

def communication_skills(request):
    context = {}
    return render(request, "skills/communication-skills.html", context=context)

def mental_health(request):
    context = {}
    return render(request, "skills/mental-health.html", context=context)

def free_courses(request):
    context = {}
    return render(request, "skills/free-courses.html", context=context)

def free_resources(request):
    context = {}
    return render(request, "skills/free-resources.html", context=context)
