from django.urls import path
from . import views

urlpatterns = [
    path('', views.bookTickets, name='book'),
    path('booked/', views.done, name='done'),
]
