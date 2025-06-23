# from django.core.exceptions import PermissionDenied
from tokenize import group

from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render, redirect

from account.models import RoleChoices, CustomUser


def check_user(func):
    def wrapper(request, *args, **kwargs):
        result = func(request,*args, **kwargs)
        if result is not None:
            if request.user.is_authenticated:
                return result
        return redirect('login-view')
    return wrapper


def admin_required(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.role != RoleChoices.ADMIN:
                return HttpResponse("Siz admin emassiz")
        else:
            return redirect('login-view')
        return func(request,*args,**kwargs)
    return wrapper


group , _ = Group.objects.get_or_create(name='Tahrirchi')
user = CustomUser.objects.get(username='salom')
user.groups.add(group)