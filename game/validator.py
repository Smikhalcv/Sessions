from django.core.exceptions import ValidationError

def validate_bigger_zero(value):
    if value < 0:
        raise ValidationError('value must be bigger zero')