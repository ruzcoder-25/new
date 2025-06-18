
from django.shortcuts import render, redirect


def check_user(func):
    def wrapper(request, *args, **kwargs):
        result = func(request,*args, **kwargs)
        if result is not None:
            if request.user.is_authenticated:
                return result
        return redirect('login-view')
    return wrapper
