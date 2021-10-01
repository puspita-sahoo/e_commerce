from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm



def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = SignUpForm()
    else:
        fm = SignUpForm()
    return render(request, "registration/signup.html", {'form':fm})

def logout(request):
    return redirect('/user_login/')
