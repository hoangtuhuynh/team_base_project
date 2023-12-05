"""
URL configuration for FMFF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#this is urls.py in myproject folder
from django.contrib import admin
from django.urls import path, include, re_path
from FindMyFurryFriend import views
from django.views.generic import RedirectView
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FindMyFurryFriend.urls')),
    path('', views.landing, name='landing'),
    path('lost_pet_list/', views.lost_pet_list, name='lost_pet_list'),
    path('found_pet_list/', views.found_pet_list, name='found_pet_list'),
    path('add_found_pet/', views.add_found_pet, name='add_found_pet'),
    path('accounts/', include('accounts.urls')), 
    path('FindMyFurryFriend/', views.lost_pet_list, name='lost_pet_list'),
    path('add-lost-pet/', views.add_lost_pet, name='add_lost_pet'),
    path('lost-pet/<int:pet_id>/', views.lost_pet_detail, name='lost_pet_detail'),
    path('found-pet/<int:pet_id>/', views.found_pet_detail, name='found_pet_detail'),
     # Define a URL pattern for the root URL ("/") that redirects to the lost pets list
    path('', RedirectView.as_view(pattern_name='lost_pet_list', permanent=False)),
    path('emergency-contacts/list/', TemplateView.as_view(template_name='FindMyFurryFriend/list.html'), name='emergency_contacts_list'),
]

# Serve media files during development

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)