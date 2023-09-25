from django.shortcuts import render
from django.http import HttpResponse
from webapp.forms import CreateUserForm, LoginForm

# Create your views here.

def home(request):
    # return HttpResponse("HEllow World")
    return render(request, 'webapp/index.html', {})

def register_view(request):
    register_form = CreateUserForm()
    diction = {'register_form': register_form}
    return render(request, 'webapp/register-page.html', context=diction)
