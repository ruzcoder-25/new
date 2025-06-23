from django.contrib.auth import login, logout
from django.db import transaction
from django.http import HttpResponse

from account.models import CustomUser
from django.shortcuts import render, redirect

from account.forms import RegisterForm, LoginForm, TransactionForm


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

# transaction

def user_list(request):
    users = CustomUser.objects.all()
    return render(request,'account/user_list.html',{'users':users,})

@transaction.atomic
def transaction_post(request):
    if request.method=='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            from_user = form.cleaned_data['from_user']
            to_user = form.cleaned_data['to_user']
            amount = form.cleaned_data['amount']
            fu = CustomUser.objects.filter(username=from_user).first()
            tu = CustomUser.objects.filter(username=to_user).first()

            if fu.balance<amount:
                return HttpResponse("Balansda yetarli mablag' mavjud emas")

            fu.balance -= amount
            fu.save()
            tu.balance += amount
            tu.save()

            return redirect('user-list')

    form = TransactionForm()
    return render(request,'account/transaction_post.html',{'form':form,})

def register_list(request):
    user = CustomUser.objects.all()
    return render(request,'account/register_list.html',{'users':user,})