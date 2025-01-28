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
UserPostSerializer,UserPutSerializer,
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

