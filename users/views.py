from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from users.models import CustomUser
from users.forms import CustomRegisterForm
#register
def register_view(request):
    if request.method == "POST":
        form = CustomRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {"form":form})

#auth_login
def auth_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/user_list/')
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {'form':form})


#auth_logout
def auth_logout_view(request):
    logout(request)
    return redirect('/login/')


#user_list
def user_list_view(request):
    if request.method == "GET":
        user_list = CustomUser.objects.all().order_by('-id')
    return render(request, 'user_list.html', {'user_list': user_list})