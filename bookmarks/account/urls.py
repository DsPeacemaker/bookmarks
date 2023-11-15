from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # предыдущий url входа
    path('login/', views.use_login, name='login'),

    # url адресс входа и выхода
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
]

