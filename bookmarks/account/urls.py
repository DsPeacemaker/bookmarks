from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.use_login, name='login'),
]