from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blog/', include('blog.urls'), name='blog'),
    path('accounts/', include('accounts.urls'), name='accounts'),
]
