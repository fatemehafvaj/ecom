# Github.com/Rasooll
from django.urls import path,include
from . import views

urlpatterns = [
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
]