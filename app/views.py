from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Course, Communitie, User
from .serializers import UserSerializer, CommunitieSerializer, CourseSerializer

class UserViewSet(viewsets.ViewSet):
    
    def list(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many =True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
     
    def retrieve(self, request, pk = None):
         
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk = pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    
    def update(self, request, pk = None):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommunityViewSet(viewsets.ViewSet):
    
    def list(self,request):
        community = Communitie.objects.all()
        serializer = CommunitieSerializer(community, many =True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommunitieSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
     
    def retrieve(self, request, pk = None):
         
        queryset = Communitie.objects.all()
        community = get_object_or_404(queryset, pk = pk)
        serializer = CommunitieSerializer(community)
        return Response(serializer.data)
    
    
    def update(self, request, pk = None):
        community = User.objects.get(pk=pk)
        serializer = CommunitieSerializer(community, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseViewSet(viewsets.ViewSet):
    
    def list(self,request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many =True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
     
    def retrieve(self, request, pk = None):
         
        queryset = User.objects.all()
        course = get_object_or_404(queryset, pk = pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    
    def update(self, request, pk = None):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
     
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)