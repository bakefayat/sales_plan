"""farman URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include

from accounts.views import Login, RegisterPendingView, RegisterCompleteView
from accounts.views import RegisterCreateView, activate


urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", Login.as_view(), name="login"),
    path("register/pending/", RegisterPendingView.as_view(), name="register-pending"),
    path("register/complete/", RegisterCompleteView.as_view(), name="register-complete"),
    path("activate/<str:uidb64>/<str:token>/", activate, name="activate"),
    path("register/", RegisterCreateView.as_view(), name="register"),
    path('', include('sales.urls'), name='sales'),
]
