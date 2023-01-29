from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json


# Create your views here.

class UsernameValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']

        #Making sure the username contains only alphanumeric characters.
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'username should only contain alphanumeric characters'}, status=400)
        return JsonResponse({'username_valid': True})

        #Checking if the username exists in database.
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry, username in use, choose another one'}, status=409)


class RegistationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
