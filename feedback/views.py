from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CompanyForm,FeedbackForm


from .models import Company


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
    if request.POST:
        form = FeedbackForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/thanks')
    else:
        form = FeedbackForm()
    return render(request,'create_review.html',{'form':form })









