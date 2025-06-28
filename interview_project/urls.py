"""
URL configuration for interview_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from interview_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('verify-otp/', views.verify_otp, name='verify-otp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Forgot password
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-forgot-otp/', views.verify_forgot_otp, name='verify_forgot_otp'), # type: ignore

    # Interview experience
    path('experience/', views.experience, name='experience'),
    path('submit/', views.submit_experience, name='submit_experience'),
    
    # Static pages
    path('', views.home_page, name='home'),
    path('thank-you/', views.thank_you, name='thank_you'),
    
]
