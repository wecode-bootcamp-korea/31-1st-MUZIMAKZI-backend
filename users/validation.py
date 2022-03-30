import re

from django.forms import ValidationError

def Validate_Email(email) :
    
    validator = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    
    if not validator.match(email) :
        raise ValidationError
    
    return True

def Validate_Password(password) :
    
    validator = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$")
    
    if not validator.match(password) :
        raise ValidationError
    
    return True