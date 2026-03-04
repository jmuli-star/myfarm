
from django.urls import path
from . import views

urlpatterns = [
    path('', views.greeting, name = 'hello'),
    path('farm/', views.farm, name = 'farmer'),
    path('form/', views.forms, name = 'forms'),
    path('service/', views.service, name = 'service'),
  
   
]
