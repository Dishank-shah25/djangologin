# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.db import IntegrityError
import os

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            print("Received data:", data)  # Print the received data
            username = data.get('username')
            password = data.get('password')
            email = data.get('email')

            if not username or not password or not email:
                return JsonResponse({'error': 'All field are required'}, status=400)
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'User already exists'}, status=400)
            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists'}, status=400)
            user = User.objects.create(username=username, password=password, email=email)
            return JsonResponse({'message': 'User created successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def login_user(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            print("Received login data:", data)
            username = data.get('username')
            password = data.get('password')
            try:
                user = User.objects.get(username=username)
                print(f"User found: {user.username}, checking password...")

            except User.DoesNotExist:
                return JsonResponse({'error': 'Invalid username or password'}, status=400)

            if password == user.password:
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                print("Password check failed")
                return JsonResponse({'error': 'Invalid username or password'}, status=400)
        else:
            return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all().values('username', 'email', 'password')
        users_list = list(users)  # Convert QuerySet to list
        return JsonResponse(users_list, safe=False, status=200)
    else:
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)
