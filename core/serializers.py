from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *


class TenantGetSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tenant
        fields= '__all__'

class TenantPostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tenant
        fields=['school_name','address','contact_email','contact_phone']

class TenantPutSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tenant
        fields=['school_name','address','contact_email','contact_phone']


class UserGetSerializer(serializers.ModelSerializer):
    tenant = serializers.CharField(source='tenant.name', read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['user_id', 'created_at', 'updated_at']


class UserPostSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['tenant', 'name', 'email', 'password', 'role', 'status']

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Hashes password before saving
        user.save()
        return user


class UserPutSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role', 'status']

    def validate_password(self, value):
        if value:
            try:
                validate_password(value)
            except ValidationError as e:
                raise serializers.ValidationError(e.messages)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)  # Hash the password before saving
        return super().update(instance, validated_data)

class LogGetSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)  # Fetch user name instead of ID
    tenant_name = serializers.CharField(source='tenant.name', read_only=True)  # Fetch tenant name instead of ID

    class Meta:
        model=Log
        fields=[
            'log_id','tenant_name','action_performed','user_name',
        ]

class LogPostSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model= Log 
        fields=[
            'tenant','action_performed','user'
        ]
        read_only_fields=[
            'log_id','timestamp'
        ]
class LogPutSerializer(serializers.ModelSerializer):
    #tenant_name= serializers.CharField(source='tenant.name', read_only=True)
    class Meta:
        model= Log
        fields=['action_performed']