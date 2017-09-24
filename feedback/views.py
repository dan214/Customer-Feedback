from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CompanyForm,FeedbackForm
from django.core import serializers
import json

from .models import Company
from django.core.mail import send_mail,EmailMultiAlternatives


def detail(request, company_id):

    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404("Company does not exist")
    company_list = Company.objects.all()
    context = {
        "company_list": company_list,
        "company": company,

    }
    return render(request,'detail.html',context)


def review(request, company_id):
    if request.POST:
        form = FeedbackForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = FeedbackForm()

    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404("Company does not exist")
    context = {
        "company": company,
        "form": form,

    }
    return render(request, 'company_reviews.html', context)


def index(request):
    is_employee = request.user.groups.filter(name='Employees').exists()
    is_manager = request.user.groups.filter(name='Managers').exists()

    if is_employee:
        company_list = Company.objects.filter(employee=request.user)
        context = {
            "companies": company_list,
            "is_employee": is_employee,
            "is_manager": is_manager
        }

        return render(request, 'employee_index.html', context)
    elif request.user.is_staff:
        company_list = Company.objects.all()
        employees = User.objects.filter(groups__name='Employees')
        managers = User.objects.filter(groups__name='Managers')

        context = {
            "companies": company_list,
            "employees": employees,
            "managers": managers
        }

        return render(request, 'admin_index.html', context)
    elif is_manager:
        employees = User.objects.filter(groups__name='Employees')
        companies = Company.objects.all()

        context = {
            "employees": employees,
            "companies": companies
        }

        return render(request,'manager_index.html', context)
    else:
        companies = Company.objects.all()

        context = {
            "companies": companies,
        }

        return render(request,'customer_index.html', context)


def thanks(request):
    return render(request,'thank-you.html')

@login_required(login_url='/accounts/login/')
def create_company(request):
    if request.POST:
        form = CompanyForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = CompanyForm()
    return render(request,'create_company.html',{'form':form })

def create_review(request,company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404("Company does not exist")
    if request.POST:
        form = FeedbackForm(request.POST)
        url = '/'
        data = json.dumps(url)

        if form.is_valid():

            instance = form.save(commit=False)
            instance.company = company
            instance.save()
            sendEmployeeEmailOnAddReview(company,form)
            return HttpResponse(data, content_type='application/json')
    else:
        form = FeedbackForm()
    context = {
        "company": company,
        "form": form,

    }

    return render(request,'create_review.html',context)

from django.template.loader import render_to_string

def sendEmployeeEmailOnAddReview(company,form):
    subject, from_email, to = "Tech Greatness.com : A customer has added a review","irungu214@gmail.com", \
                              company.employee.email

    context = {
        "employee": company.employee.get_full_name(),
        "company": company,
        "form": form,
        "first_name": form.cleaned_data['first_name'],
        "last_name": form.cleaned_data['last_name'],
        "comment": form.cleaned_data['comment'],
    }

    msg_plain = render_to_string('add_review_email_template.txt', context)
    msg_html = render_to_string('add_review_email_template.html', context)

    send_mail(subject,msg_plain,from_email,[to],fail_silently=False,html_message=msg_html)








