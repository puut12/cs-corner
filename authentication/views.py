import json
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User

@csrf_exempt
def login_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({
                "status": "success",
                "message": "Login success!",
                "username": user.username, # [cite: 195]
                "user_id": user.id 
            }, status=200)
        else:
            return JsonResponse({
                "status": "error",
                "message": "Invalid credentials. Please check your username or password."
            }, status=401)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

@csrf_exempt
def register_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        if not username or not password:
            return JsonResponse({"status": "error", "message": "Username and password are required."}, status=400)
        
        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "error", "message": "Username already exists."}, status=400)
            
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return JsonResponse({"status": "success", "message": "User created successfully!"}, status=201)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)

@csrf_exempt
def logout_flutter(request):
    if request.method == 'POST':
        username = request.user.username
        logout(request)
        return JsonResponse({
            "status": "success",
            "message": "Logged out successfully!",
            "username": username
        }, status=200)
    return JsonResponse({"status": "error", "message": "Invalid request method."}, status=400)