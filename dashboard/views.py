from django.shortcuts import render
from account_profile.models import University
from student_forum.models import Company
# Create your views here.


def university_list_view(request):
    universities = University.objects.all().distinct()
    count = len(universities)
    context = {
        "universities": universities,
        "count": count,
    }
    return render(request, "dashboard/university-list.html", context=context)


def company_list_view(request):
    companies = Company.objects.all()
    count = len(companies)
    context = {
        "companies": companies,
        "count": count,
    }
    return render(request, "dashboard/company-list.html", context=context)

