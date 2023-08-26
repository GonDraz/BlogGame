from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog),
    path('<slug:slug>/', views.post),
]
