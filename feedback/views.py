from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, DetailView


from .forms import UserCreationForm
from .models import Company


@login_required
def create_form(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            created_user = form.save(commit=False)
            created_user.save()
            return HttpResponseRedirect('/feedback/')
    else:
        form = UserCreationForm()

    return render(request,'createemployee.html',{'form':form })



def logout_view(request):
    logout(request)

class index(ListView):
    model = Company
    template_name = "index.html"

    def get_queryset(self, **kwargs):
        user = self.request.user
        return self.model.objects.filter(employee__email=user.email)





