from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("accounts/register", views.register_request, name="register"),
    path("accounts/login", views.login_request, name="login"),
    path("accounts/logout", views.logout_request, name="logout")
]