
from django.urls import path
from .views import *

urlpatterns = [
    path('phone_check_code', phone_check_code, name='phone_check_code')
]
