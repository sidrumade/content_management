from rest_framework import serializers
from django.core.validators import MinLengthValidator
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('email', 'password', 'fullname', 'phone', 'address', 'city', 'state', 'country', 'pincode')

    def validate_phone(self, value):
        if len(value) < 10:
            raise serializers.ValidationError('Phone number must be at least 10 characters long')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        return value

    def validate_pincode(self, value):
        if value is None or value < 100000 or value > 999999:
            raise serializers.ValidationError('Pincode must be exactly 6 characters long')
        return value
