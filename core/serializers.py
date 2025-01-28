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
    tenant = serializers.CharField(source='organization.name', read_only=True)

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields=['user_id','created_at','updated_at']


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'tenant','name','email','password','role','status'
        ]

class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=[
            'name','email','password','role','status'
        ]