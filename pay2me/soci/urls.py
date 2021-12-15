# social_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paytm_integ.urls')),

    # Adding social auth path
    # path('social-auth/', include('social_django.urls', namespace="social")),

    # path("", views.home, name="home"),
#     path("login/", views.login, name="login"),
#     path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]