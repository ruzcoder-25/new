from django.contrib.auth import login, logout
from account.models import CustomUser
from django.shortcuts import render, redirect

from account.forms import RegisterForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # password=form.cleaned_data.get('password')
            # user = form.save(commit=False)
            # user.set_password(password)
            form.save()
            return redirect('login-view')
    else:
        form = RegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'account/register.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            user = CustomUser.objects.filter(username=username).first()
            if user is not None:
                login(request, user)
                return redirect('book-list')
    else:
        form = LoginForm()
    context = {
        'form': form,
    }
    return render(request, 'account/login_view.html', context)

def logout_view(request):
    logout(request)
    return redirect('book-list')

