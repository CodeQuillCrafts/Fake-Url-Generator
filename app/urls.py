from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('<str:furl>/', views.redirect_url, name='redirect_url'),
]
