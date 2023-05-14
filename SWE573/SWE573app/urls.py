from django.urls import path
from . import views


urlpatterns = [
    path('signUp', views.signUp, name='signUp'),
    path('', views.home, name='home'),
    path('ProfilePage/<slug:slug>/', views.profile_editing, name='profile_page'),
    path('ProfileScreen/<slug:slug>/', views.profile_screen, name='profile_screen'),
    path('PostData', views.post, name='post'),
    path('ScreenPost/<slug:slug>/', views.screenpost, name='screenpost'),
]