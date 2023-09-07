from rest_framework import serializers
from django.core.exceptions import ValidationError
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['email', 'password', 'fullname', 'phone', 'address', 'city', 'state', 'country', 'pincode']

    def validate_email(self, value):
        # Add your custom validation for email
        return value

    def validate_password(self, value):
        # Add your custom validation for password
        return value

    def validate_pincode(self, value):
        value_str = str(value)
        if len(value_str) != 6:
            raise serializers.ValidationError('Pincode must be exactly 6 characters long')
        return value
