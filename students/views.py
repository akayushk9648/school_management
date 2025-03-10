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
StudentGetSerializer,StudentPostSerializer,StudentPutSerializer,
AttendanceGetSerializer,AttendancePostSerializer,AttendancePutSerializer
)

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class StudentView(generics.GenericAPIView):
    queryset=Student.objects.all()
    permission_classes=[AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields=['user','tenant','date_of_birth','admission_date','gender']
    search_fields =['user','tenant','roll_number','parent_contact']
    ordering_fields=['user','roll_number','admission_date']
    pagination_class=CustomPagination

    def get(self, request, *args, **kwargs):
        self.serializer_class = StudentGetSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        self.serializer_class = StudentPostSerializer
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


    def put(self, request, *args, **kwargs):
        self.serializer_class = StudentPutSerializer
        try:
            student = Student.objects.get(id=request.data.get('id'))
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)
        serializer = self.get_serializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    
class AttendanceView(generics.GenericAPIView):
    queryset=Attendance.objects.all()
    permission_classes=[AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields=['date','status']
    search_fields =['student']
    ordering_fields=['date','student']
    pagination_class=CustomPagination

    def get(self, request, *args, **kwargs):
        self.serializer_class = AttendanceGetSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        self.serializer_class = AttendancePostSerializer
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    


    def put(self, request, *args, **kwargs):
        self.serializer_class = StudentPutSerializer
        try:
            attendance = Attendance.objects.get(id=request.data.get('id'))
        except Tenant.DoesNotExist:
            return Response({"error": "Attendance not found"}, status=404)
        serializer = self.get_serializer(attendance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    