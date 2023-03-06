from django.shortcuts import render,redirect
from .forms import StudentFeedbackForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def student_feedback_view(request):
    # student_    StudentFeedback.objects.all().distinct("feedback_given_by")

    context = {}
    if request.method == "POST":
        feedback_form = StudentFeedbackForm(request.POST)
        print(feedback_form)
        if feedback_form.is_valid():
            print("form is valid")
            feedback = feedback_form.save(commit=False)
            feedback.feedback_given_by = request.user
            feedback.save()
            
            messages.success(request, "Your feedback has been received successfully")
        else:
            messages.warning(request, "Form is not valid. Please fill it up again.")
            print(feedback_form.errors)
            print("Form is not Valid")
            context["feedback_form"] = feedback_form
    else:
        student_feedbacks = StudentFeedback.objects.filter(will_be_displayed=True)
        for feedback in student_feedbacks:
            print(feedback.rating)
            print(type(feedback.rating))
        context["student_feedbacks"] = student_feedbacks

    return render(request, "student-forum/student-feedback.html", context=context)

def student_success_stories_view(request):
    success_stories = SuccessStory.objects.all()
    context = {
        "success_stories": success_stories,
    }
    return render(request, "student-forum/student-success-stories.html", context=context)

def student_success_story_detail_view(request, story_slug):
    story_qs = SuccessStory.objects.filter(slug=story_slug)
    if story_qs:
        story = story_qs[0]
    else:
        story = None
    context = {
        "story": story,
    }
    return render(request, "student-forum/student-success-story.html", context=context)