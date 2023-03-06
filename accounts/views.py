from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import (
    SignUpForm, SignInForm,
)
from account_profile.forms import StudentCurrentEducationStatusForm

# user authentication and send_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token

# activate_account
# from django.utils.encoding import force_text // 3.0
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# end import

from django.contrib import messages
from django.conf import settings

from account_profile.models import (
     Subject, University, GraduationExamName,
     PostGraduationExamName, 
)  

from .models import Account
# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def signup_view(request):
    universities = University.objects.all()
    subjects = Subject.objects.all()
   
    if request.user.is_authenticated:
        print(f"You are already authenticated as {request.user.username}")
    
    if request.method == "POST":
        signup_form = SignUpForm(request.POST)
        uni_form = StudentCurrentEducationStatusForm(request.POST)
        
        if signup_form.is_valid() and uni_form.is_valid():
            print("form is valid")
            account = signup_form.save(commit=False)
            account.is_student = True
            account.is_active = False
            account.save()
            edu_info = uni_form.save(commit=False)
            edu_info.account = account
            edu_info.save()
            # send activatetion email
            if send_activation_mail(request, account):
                return redirect('accounts:account_activation_email_sent')
            else:
                messages.warning(request, "Something went wrong!!.")
                # what to do
                return redirect('accounts:signup')
        else:
            print(signup_form.errors)
            print(uni_form.errors)
            print("form is not valid")
    else:
        context = {}
        context['university_names'] = universities
        context['subject_names'] = subjects
    return render(request, "accounts/signup.html", context=context)

def signin_view(request):
    print("Submit name checking...")
    context = {}
    if request.method == "POST":
        signin_form = SignInForm(request.POST)
        if signin_form.is_valid():
            email = signin_form.cleaned_data.get('email').lower()
            password = signin_form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('core:home')
                # destination = get_redirect_if_exists(request)
                # if destination:
                #     return redirect(destination)
                # else:
                #     return redirect('demo:home')
            else:
                messages.warning(request, "Account does not exist!!. Please try again")
                return redirect('accounts:signin')
        else:
            context["signin_form"] = signin_form
    return render(request, "accounts/signin.html", context=context)

def signout_view(request):
    logout(request)
    messages.info(request, "You have been signed out.")
    return redirect("core:home")    
 
# creating and sending activation email
def send_activation_mail(request, user):
    subject = "Activate Your Dikkha Account"
    from_email = settings.DEFAULT_FROM_EMAIL
    current_site = get_current_site(request)
    message = render_to_string('accounts/account_activation_email.html',
                        {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': account_activation_token.make_token(user),
                        })
    if message is not None:
        user.email_user(subject, message, from_email)
        return True
    else:
        return False

def account_activation_email_sent(request):
    if request.user.is_authenticated:
        messages.info(request, f"You are already authenticated as {request.user.username}")
        return redirect("core:home")
    else:
        return render(request, 'accounts/account_activation_email_sent.html')    

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        account = Account.objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        account = None
    if account is not None and account_activation_token.check_token(account, token):
        account.is_active = True
        account.email_confirmed = True
        account.save()

        login(request, account, backend="django.contrib.auth.backends.AllowAllUsersModelBackend")
        messages.info(request, f"Your account has been activated")
        return redirect("core:home")
    else:
        return render(request, 'accounts/invalid_account.html')


def load_university_contents(request):
    selected_university_level = request.GET.get("selected_university_level")
    print(selected_university_level)
    data = {}
    if selected_university_level == "graduation":
        graduate_exam_names = GraduationExamName.objects.all()
        load_exam_names = render_to_string('accounts/load_university_exam_names.html', context={'exam_names': graduate_exam_names})
        load_which_years = render_to_string("accounts/load_graduate_level_years.html", context={}) 
        data["load_exam_names"] = load_exam_names
        data["load_which_years"] = load_which_years
        data["status"] = "success"
        
    elif selected_university_level == "post_graduation":
        post_graduate_exam_names = PostGraduationExamName.objects.all()
        load_exam_names = render_to_string('accounts/load_university_exam_names.html', context={'exam_names': post_graduate_exam_names})
        load_which_years = render_to_string("accounts/load_post_graduate_level_years.html", context={}) 
        data["load_exam_names"] = load_exam_names
        data["load_which_years"] = load_which_years
        data["status"] = "success"
    else:
        data["status"] = "failed"
        data["error"] = "unindentified_data"
    return JsonResponse(data, safe=False)

def account_profile(request):
    context = {}
    return render(request, "accounts/account_profile.html", context=context)

def account_address(request):
    context = {}
    return render(request, "accounts/account_address.html", context=context)
