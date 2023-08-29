from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.base),
    path('home/', views.home),
    path('contact/', views.contact),
    path('blog/', include('blog.urls')),
]
