from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',homep,name="home" ),
    path('paytm_integ/handlepayment/',handlerequest,name="handlerequest" ),
]
