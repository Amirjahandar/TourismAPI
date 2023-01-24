from django.urls import path, include
from .views import email_check_code
urlpatterns = [
    path('email_check_code/', email_check_code, name='email_check_code' ),
]