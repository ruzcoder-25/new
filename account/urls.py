from django.urls import path

from account import views

urlpatterns = [
    path('',views.register , name='register'),
    path('login/',views.login_view , name='login-view'),
    path('logout/',views.logout_view , name='logout-view'),
    path('user_list/',views.user_list , name='user-list'),
    path('transaction/',views.transaction_post , name='transaction-post'),
    path('register_list/',views.register_list , name='register-list'),

]