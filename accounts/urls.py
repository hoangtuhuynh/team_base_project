# accounts/urls.py

from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'accounts' 

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
]
