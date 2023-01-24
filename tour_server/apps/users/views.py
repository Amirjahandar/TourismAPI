from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def phone_check_code(request):
    
    response = {
        "status": "success",
        "token": "akdfjiefa2931kdjfakjd2913434",
        "new_user": True
    }
    return JsonResponse(response)