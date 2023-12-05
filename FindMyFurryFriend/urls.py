# FindMyFurryFriend/urls.py
from django.urls import path
from . import views
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'FindMyFurryFriend'

urlpatterns = [
    path('', views.login, name='login'),
    path('register/',views.register,name='register'),
    path('home/',views.landing,name='landing'),
    path('lost_pet_list/', views.lost_pet_list, name='lost_pet_list'),
    path('found_pet_list/', views.found_pet_list, name='found_pet_list'),
    path('lost-pets/', views.lost_pet_list, name='lost_pet_list'),
    path('add-lost-pet/', views.add_lost_pet, name='add_lost_pet'),
    path('add_found_pet/', views.add_found_pet, name='add_found_pet'),
    path('lost-pet/<int:pet_id>/', views.lost_pet_detail, name='lost_pet_detail'),
    path('TN-api/', views.TN_api, name='TN_api'),
    path('emergency-contacts/list/', TemplateView.as_view(template_name='FindMyFurryFriend/list.html'), name='emergency_contacts_list'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
