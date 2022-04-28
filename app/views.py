
from django.http import HttpResponse, JsonResponse

from django.shortcuts import get_object_or_404, render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Article, Communitie, Course, Developers, Project, User

from .serializers import (ArticleSerializer, CommunitieSerializer,
                          CourseSerializer, DevelopersSerializer,
                          ProjectSerializer, UserSerializer)


class UserView(APIView):
    
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
class UserDetails(APIView):
    
    def get_objects(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return HttpResponse(status= status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        user = self.get_objects(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, id):
        user = self.get_objects(id)
        serializer = UserSerializer(user, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        user = self.get_objects(id)
        user.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class CourseView(APIView):
    
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CourseSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
class CourseDetails(APIView):
    
    def get_objects(self, id):
        try:
            return Course.objects.get(id=id)
        except Course.DoesNotExist:
            return HttpResponse(status= status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        course = self.get_objects(id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    
    def put(self, request, id):
        course = self.get_objects(id)
        serializer = CourseSerializer(course, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        course = self.get_objects(id)
        course.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


class CommunityView(APIView):
    
    def get(self, request):
        community = Communitie.objects.all()
        serializer = CommunitieSerializer(community, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommunitieSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
class CommunitieDetails(APIView):
    
    def get_objects(self, id):
        try:
            return Communitie.objects.get(id=id)
        except Communitie.DoesNotExist:
            return HttpResponse(status= status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        community = self.get_objects(id)
        serializer = CommunitieSerializer(community)
        return Response(serializer.data)
    
    def put(self, request, id):
        community = self.get_objects(id)
        serializer = CommunitieSerializer(community, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        community = self.get_objects(id)
        community.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
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
    
class ArticleView(APIView):
    
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
class ArticleDetails(APIView):
    
    def get_objects(self, id):
        try:
            return Article.objects.get(id=id)
        except Article.DoesNotExist:
            return HttpResponse(status= status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        article = self.get_objects(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    def put(self, request, id):
        article = self.get_objects(id)
        serializer = ArticleSerializer(article, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        article = self.get_objects(id)
        article.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    
class DeveloperView(APIView):
    
    def get(self, request):
        developer = Developers.objects.all()
        serializer = DevelopersSerializer(developer, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DevelopersSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class DeveloperDetails(APIView):
    
    def get_object(self, id):
        try:
            return Developers.objects.get(id=id)
        except Developers.DoesNotExist:
            return HttpResponse(status= status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        developer= self.get_object(id)
        serializer = DevelopersSerializer(developer)
        return Response(serializer.data)
    
    def put(self, request, id):
        developer = self.get_object(id)
        serializer = DevelopersSerializer(developer, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        developer = self.get_object(id)
        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectView(APIView):
    
    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many =True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
class ProjectDetails(APIView):
    
    def get_object(self, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)
        
    def get(self, request, id):
        project = self.get_object(id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, id):
        project = self.get_object(id)
        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        project = self.get_object(id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
        
        
# class UserViewSet(viewsets.ViewSet):
    
#     def list(self,request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many =True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = UserSerializer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)

#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
     
#     def retrieve(self, request, pk = None):
         
#         queryset = User.objects.all()
#         user = get_object_or_404(queryset, pk = pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
    
#     def update(self, request, pk = None):
#         user = User.objects.get(pk=pk)
#         serializer = UserSerializer(user, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
     
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CommunityViewSet(viewsets.ViewSet):
    
#     def list(self,request):
#         community = Communitie.objects.all()
#         serializer = CommunitieSerializer(community, many =True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = CommunitieSerializer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)

#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
     
#     def retrieve(self, request, pk = None):
         
#         queryset = Communitie.objects.all()
#         community = get_object_or_404(queryset, pk = pk)
#         serializer = CommunitieSerializer(community)
#         return Response(serializer.data)
    
    
#     def update(self, request, pk = None):
#         community = User.objects.get(pk=pk)
#         serializer = CommunitieSerializer(community, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
     
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
