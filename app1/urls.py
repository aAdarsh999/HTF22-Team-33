from django.contrib import admin
from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("dashboard/",views.dashboard,name = 'dashboard'),
    path("upload/",views.upload,name = "upload"),
    path("save/",views.save,name = "upload"),
    path("logout/",views.logout_user,name = "logout"),
    path("login/",views.login,name="login"),
    path('', HomeView.as_view(), name='home')
]
