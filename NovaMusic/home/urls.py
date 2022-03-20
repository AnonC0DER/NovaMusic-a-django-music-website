from django.urls import path
from home import views

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('search/', views.SearchPage, name='search'),
]