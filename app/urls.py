from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('create', views.create, name="create"),
    path('read/<int:pk>', views.read, name="read"),
    path('update<int:pk>', views.update, name="update"),
    path('delete/<int:pk>', views.delete, name="delete"),
]