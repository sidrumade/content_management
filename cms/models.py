from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError


# Create your models here.


def validate_pincode(value):
    if len(value) != 6:
        raise ValidationError('Pincode must be exactly 6 characters long')

##Author model
class Author(models.Model):
    email = models.EmailField(null=False)
    password = models.CharField(max_length=100 ,null=False,validators=[MinLengthValidator(8)])
    fullname =models.CharField(max_length=100,null=False)
    phone = PhoneNumberField(validators=[MinLengthValidator(10)])
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    pincode = models.CharField(max_length=6,null=False, validators=[validate_pincode])
