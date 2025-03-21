from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Class, Subject
from .serializers import (
    ClassGetSerializer,
    ClassPostSerializer,
    ClassPutSerializer,
    SubjectGetSerializer,
    SubjectPostSerializer,
    SubjectPutSerializer,
)

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

def home(request):
    return HttpResponse("School Management System")

class ClassView(generics.GenericAPIView):
    queryset = Class.objects.all()
    permission_classes = [IsAuthenticated]  # You can change to AllowAny if needed
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['class_name', 'section', 'tenant']
    search_fields = ['class_name', 'section']
    ordering_fields = ['class_name', 'section']
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        self.serializer_class = ClassGetSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        self.serializer_class = ClassPostSerializer
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        self.serializer_class = ClassPutSerializer
        try:
            class_instance = Class.objects.get(class_id=request.data.get('class_id'))
        except Class.DoesNotExist:
            return Response({"error": "Class not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(class_instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectView(generics.GenericAPIView):
    queryset = Subject.objects.all()
    permission_classes = [IsAuthenticated]  # You can change to AllowAny if needed
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['subject_name', 'class_assigned', 'tenant']
    search_fields = ['subject_name']
    ordering_fields = ['subject_name']
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        self.serializer_class = SubjectGetSerializer
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        self.serializer_class = SubjectPostSerializer
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        self.serializer_class = SubjectPutSerializer
        try:
            subject = Subject.objects.get(subject_id=request.data.get('subject_id'))
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(subject, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)