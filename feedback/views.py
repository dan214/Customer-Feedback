from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CompanyForm


from .models import Company

@login_required(login_url='/accounts/login/')
def detail(request, company_id):
    try:
        company = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404("Company does not exist")
    return render(request,'detail.html',{'company': company})


def logout_view(request):
    logout(request)


@login_required(login_url='/accounts/login/')
def index(request):
    company_list = Company.objects.filter(employee= request.user)

    context = {
        "objects":company_list,
    }

    return render(request, 'index.html', context)

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










