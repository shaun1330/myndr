from django.urls import path, reverse
from app import views
from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path("", views.home_view, name="home"),
    path("tasks/", views.tasks_view, name='tasks'),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]