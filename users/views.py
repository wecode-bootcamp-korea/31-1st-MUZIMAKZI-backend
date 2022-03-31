import json, bcrypt, jwt

from .models import User

from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.core.exceptions import ValidationError

from .validation import validate_email, validate_password

class SignUpView(View) :
    
    def post(self, request) :
        try :
            data = json.loads(request.body)
            
            if User.objects.filter(email = data["email"]).exists() :
                    return JsonResponse({"message" : "ALREADY EXITSTS EMAIL"}, status = 409)
            
            if not validate_email(data["email"]) :
                return JsonResponse({"message" : "INVALID EMAIL"}, status = 400)
            
            if not validate_password(data["password"]) :
                return JsonResponse({"message" : "INVALID PASSWORD"}, status = 400)
            
            hashed_password = bcrypt.hashpw(data["password"].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
            User.objects.create(
                first_name   = data['first_name'],
                last_name    = data['last_name'],
                email        = data["email"],
                password     = hashed_password,
                phone_number = data["phone_number"]
            )
            
            return JsonResponse({"message" : "SUCCESS"}, status = 201)
            
        except KeyError :
            JsonResponse({"message" : "KEY_ERROR"}, status = 400)
            
        except ValidationError :
            JsonResponse({"message" : "VALIDATION_ERROR"}, status = 400)
            
class SignInView(View) :
    
    def post(self, request) :
        try :
            data = json.loads(request.body)
                
            email = data['email']
            password = data['password']
                
            if not User.objects.filter(email=email).exists() :
                return JsonResponse({'message' : 'INVALID EMAIL OR PASSWORD'}, status = 401)
                
            check_user = User.objects.get(email=email)
            
            if not bcrypt.checkpw(password.encode('utf-8'), check_user.password.encode('utf-8')) :
                return JsonResponse({'message' : 'INVALID EMAIL OR PASSWORD'}, status = 401)
                
            access_token = jwt.encode({"id" : check_user.id}, settings.SECRET_KEY, settings.ALGORITHM)
                
            return JsonResponse({"message" : "SUCCESS",
                                    "access_token" : access_token}, status = 200)
                
        except KeyError :
            JsonResponse({"message" : "KEY_ERROR"}, status = 400)