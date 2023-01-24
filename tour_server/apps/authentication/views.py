from django.shortcuts import render
from django.http import HttpResponse, JsonResponse




def email_check_code(request):
    response = {
    "email": "sth@gmail.com",
    "code": "85746",
    "new_password_required": False
    }

    return JsonResponse(response)