from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('lokasi', views.lokasi, name='lokasi'),
    path('lokasi/delete/<int:lid>/', views.delete_lokasi, name='delete_lokasi'),
    path('e1', views.e1, name='e1'),
    path('e1/delete/<int:e1id>/', views.delete_e1, name='delete_e1'),
]