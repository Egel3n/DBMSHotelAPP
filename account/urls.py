from django.urls import path,include
from . import views

urlpatterns = [
    path("login",views.login_request,name="login"),
    path("register",views.register_request,name="register"),
    path("logout",views.logout_request,name="logout")
]
