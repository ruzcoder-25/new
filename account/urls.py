from django.urls import path

from account import views

urlpatterns = [
    path('',views.register , name='register'),
    path('login/',views.login_view , name='login-view'),
    path('logout/',views.logout_view , name='logout-view'),

]