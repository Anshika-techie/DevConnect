from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path(
    'forgot-password/',
    views.forgot_password,
    name='forgot_password'
),
path(
    'complete-profile/',
    views.complete_profile,
    name='complete_profile'
),

path(
    'skip-profile/',
    views.skip_profile,
    name='skip_profile'
),
path('upload-profile-image/', views.upload_profile_image),
path('upload-cover-image/', views.upload_cover_image),
path(
    'remove-profile-image/',
    views.remove_profile_image,
    name='remove_profile_image'
),
path(
    'remove-cover-image/',
    views.remove_cover_image,
    name='remove_cover_image'
),
]