from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
        path('',views.home,name='home'),
        path('register',views.register,name='register'),
        path('login', views.login_user, name='login'),
        path('form',views.form,name='form'),
        path('logout/', views.logout, name='logout'),
    ]