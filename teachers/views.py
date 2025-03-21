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
TeacherGetSerializer,TeacherPostSerializer,
TeacherPutSerializer
)


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TeacherView(generics.GenericAPIView):
    queryset = Teacher.objects.all()
    
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['user', 'tenant','subject_specialization','hiring_date']
    search_fields = ['user', 'teacher_id', ]
    ordering_fields = ['user', 'hiring_date']
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        self.serializer_class = TeacherGetSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        self.serializer_class = TeacherPostSerializer
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, *args, **kwargs):
        self.serializer_class = TeacherPutSerializer
        try:
            teacher = Teacher.objects.get(id=request.data.get('id'))
        except Teacher.DoesNotExist:
            return Response({"error": "Teacher not found"}, status=404)
        serializer = self.get_serializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
