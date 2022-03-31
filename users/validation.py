import re

from django.core.exceptions import ValidationError

def validate_email(email) :
    
    validator = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    
    if not validator.match(email) :
        raise ValidationError
    
    return True

def validate_password(password) :
    
    validator = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
    
    if not validator.match(password) :
        raise ValidationError
    
    return True