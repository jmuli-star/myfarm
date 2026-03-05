
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.greeting, name = 'hello'),
    path('farm/', views.farm, name = 'farmer'),
    path('form/', views.forms, name = 'forms'),
    path('service/', views.service, name = 'service'),
    path('farms/', FarmCreateAPIView.as_view(), name = 'farm-list'),
  
   
]
