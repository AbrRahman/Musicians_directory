from django.shortcuts import render,redirect
from musician.forms import MusicianForm,RegisterForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,update_session_auth_hash,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def add_musician(request):
    if request.method=="POST":
        musician_form=MusicianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect("add_musician")
    else:
        musician_form=MusicianForm()
    return render(request,"musician_form.html",{"form":musician_form})
def register(request):
    if(request.method=="POST"):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Register Successfully")
            return redirect("login")
    else:
        form=RegisterForm()
    return render(request,'register.html',{"form":form})

        
def user_login(request):
    if(request.method=="POST"):
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged In Successfully")
                return redirect("home")
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{"form":form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully")
    return redirect("home")
