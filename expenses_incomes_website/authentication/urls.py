from .views import RegistationView
from django.urls import path

urlpatterns = [
    path('register', RegistationView.as_view(), name='register'),
]
