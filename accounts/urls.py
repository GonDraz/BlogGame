# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('logout/', views.logout, name='logout'),
    path(
        "signin/", views.AuthorSignInView.as_view(), name="signin"
    ),
    path(
        "profile/",
        login_required(views.AuthorProfileView.as_view()),
        name="profile",
    ),



]
