from django.shortcuts import render, redirect
from .forms import loginform, registerform
from django.contrib.auth import authenticate, login, logout



def login_view(request):
    form = loginform(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        login(request, user)
        return redirect('post:index')
    return render(request, 'accounts/form.html', {'form': form, 'title': 'giriş yap'})


def register_view(request):
    form = registerform(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('post:index')
    return render(request, 'accounts/form.html', {'form': form, 'title': 'üye ol'})


def logout_view(request):
    logout(request)
    return redirect('post:index')
