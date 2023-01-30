from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from validate_email import validate_email


# Create your views here.

class EmailValidationView(View):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']

        #Making sure the email is valid.
        if not validate_email(email):
            return JsonResponse({'email_error': 'email is invalid'}, status=400)
        return JsonResponse({'email_valid': True})

        #Checking if the email exists in database.
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, email in use, choose another one'}, status=409)


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
