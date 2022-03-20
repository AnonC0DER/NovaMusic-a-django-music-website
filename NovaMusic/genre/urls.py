from django.urls import path
from genre import views

urlpatterns = [
    path('genre/<slug>-ID-<pk>/', views.GenrePage, name='genre')
]