from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import *
from .serializers import (
TenantGetSerializer,TenantPostSerializer,
TenantPutSerializer,UserGetSerializer,
UserPostSerializer,UserPutSerializer,LogGetSerializer,LogPostSerializer,
LogPutSerializer
)

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TenantView(generics.GenericAPIView):
    queryset=Tenant.objects.all()
    permission_classes=[AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields=['school_name','contact_email',]
    search_fields =['school_name','address','contact_email',]
    ordering_fields=['school_name','created_at']
    pagination_class=CustomPagination

    def get(self, request, *args, **kwargs):
        self.serializer_class = TenantGetSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        self.serializer_class = TenantPostSerializer
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


    def put(self, request, *args, **kwargs):
        self.serializer_class = TenantPutSerializer
        try:
            tenant = Tenant.objects.get(id=request.data.get('id'))
        except Tenant.DoesNotExist:
            return Response({"error": "Tenant not found"}, status=404)
        serializer = self.get_serializer(tenant, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)



class UserView(generics.GenericAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['email', 'role', 'status']
    search_fields = ['name', 'email']
    ordering_fields = ['name', 'created_at']
    pagination_class = CustomPagination
    serializer_class = UserGetSerializer  # Define a default serializer here

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = UserGetSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = UserGetSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = UserPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        try:
            user = User.objects.get(user_id=request.data.get('user_id'))
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        serializer = UserPutSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)



class LogListView(generics.GenericAPIView):
    queryset = Log.objects.all()
    
    def get_serializer_class(self):
        
        if self.request.method == "GET":
            return LogGetSerializer
        elif self.request.method == "POST":
            return LogPostSerializer
        elif self.request.method == "PUT":
            return LogPutSerializer
        return LogGetSerializer  # Default serializer

    def get(self, request, *args, **kwargs):
        logs = self.get_queryset()
        serializer = self.get_serializer(logs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, log_id, *args, **kwargs):
        try:
            log = self.get_queryset().get(log_id=log_id)
            serializer = self.get_serializer(log, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Log.DoesNotExist:
            return Response({"error": "Log not found"}, status=status.HTTP_404_NOT_FOUND)