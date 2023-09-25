from django.shortcuts import render, redirect
from django.http import HttpResponse
from webapp.forms import CreateUserForm, LoginForm

# Create your views here.

def home(request):
    # return HttpResponse("HEllow World")
    return render(request, 'webapp/index.html', {})

def register(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            # return redirect('')

    diction = {'register_form': register_form}
    return render(request, 'webapp/register-page.html', context=diction)

# def dashboard(request):
#     pass

# def user-logout(request):
#     pass

# def my-login(request):
#     pass
