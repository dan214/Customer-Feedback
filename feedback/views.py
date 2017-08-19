from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Company


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









