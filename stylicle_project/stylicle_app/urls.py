from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/', views.contactus, name='contactus'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('user_login', views.user_login, name='user_login'),
]
