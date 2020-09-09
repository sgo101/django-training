from django.core import validators

def email_validation_function(value):
    valid = False
    try:
        validators.email_validator(value)
        valid = True
    except:
        valid = False

    return valid

e = "hello@gmaill.com"
res = email_validation_function("hello@gmaill.com")
if res:
    print('Valid')
else:
    print('not valid')