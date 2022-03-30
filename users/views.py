import json, bcrypt, jwt

from .models import User

from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.forms import ValidationError

from .validation import Validate_Email, Validate_Password

        
class SignUpView(View) :
    try :
        def post(self, request) :
            data = json.loads(request.body)
            
            if User.objects.filter(email = data["email"]) :
                    return JsonResponse({"MESSAGE" : "ALREADY EXITSTS EMAIL"}, status = 400)
            
            if not Validate_Email(data["email"]) :
                return JsonResponse({"MESSAGE" : "INVALID EMAIL"}, status = 400)
            
            if not Validate_Password(data["password"]) :
                return JsonResponse({"MESSAGE" : "INVALID PASSWORD"}, status = 400)
            
            
            hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            
        
            User.objects.create(
                first_name   = data['first_name'],
                last_name    = data['last_name'],
                email        = data["email"],
                password     = hashed_password,
                phone_number = data["phone_number"]
            )
            
            return JsonResponse({"MESSAGE" : "SUCCESS"}, status = 200)
            
            
    except KeyError :
        JsonResponse({"MESSAGE" : "KEY_ERROR"}, status = 400)
    except ValidationError :
        JsonResponse({"MESSAGE" : "VALIDATION_ERROR"}, status = 400)
        
        
        
        

class SignInView(View) :
    try:
        def post(self, request) :
            data = json.loads(request.body)
            
            email = data['email']
            password = data['password']
            
            if not User.objects.filter(email=email) :
                return JsonResponse({'MESSAGE' : 'INVALID EMAIL OR PASSWORD'}, status = 400)
            
            check_user = User.objects.get(email=email)
        
            if not bcrypt.checkpw(password.encode('utf-8'), check_user.password.encode('utf-8')) :
                return JsonResponse({'MESSAGE' : 'INVALID EMAIL OR PASSWORD'}, status = 400)
            
            access_token = jwt.encode({"id" : check_user.id}, settings.SECRET_KEY, settings.ALGORITHM)
            
            
            return JsonResponse({"MESSAGE" : "SUCCESS",
                                 "ACCESS TOKEN" : access_token}, status = 200)
            
        
    except KeyError :
        JsonResponse({"MESSAGE" : "KEY_ERROR"}, status = 400)