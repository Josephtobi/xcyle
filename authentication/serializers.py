from django.contrib.auth import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from authentication.models import User





class RegisterSerializer(serializers.ModelSerializer):
    

    password= serializers.CharField(max_length=120, min_length=6, write_only=True )

    class Meta:
        model=User
        fields=('username','email','password')


    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password= serializers.CharField(max_length=120, min_length=6, write_only=True )

    class Meta:
        model=User
        fields=('email','password','token','username')
        read_only_fields=['token']
