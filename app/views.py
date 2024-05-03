from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from app.models import(
    Article, 
    Communitie, 
    Course, 
    Developers, 
    Project, 
    User
)

from .serializers import (
    ArticleSerializer, 
    CommunitieSerializer,
    CourseSerializer, 
    DevelopersSerializer, 
    ProjectSerializer, 
    UserSerializer
)


class UserView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve a list of users",
        responses={200: openapi.Response("List of users", UserSerializer(many=True))},
    )
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new user",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["name", "username", "phone", "email"],
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "phone": openapi.Schema(type=openapi.TYPE_INTEGER),
                "email": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
            },
        ),
        responses={
            201: "Created",
            400: "Bad Request",
        },
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class UserDetails(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve user details",
        responses={200: openapi.Response("User details", UserSerializer())},
    )
    def get(self, request, id):
        """
        Retrieve user details.
        """
        user = self.get_objects(id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update user details",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["name", "username", "phone", "email"],
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "username": openapi.Schema(type=openapi.TYPE_STRING),
                "phone": openapi.Schema(type=openapi.TYPE_INTEGER),
                "email": openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
            },
        ),
        responses={
            200: "OK",
            400: "Bad Request",
        },
    )
    def put(self, request, id):
        """
        Update user details.
        """
        user = self.get_objects(id)
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete user",
        responses={
            204: "No Content",
            404: "Not Found",
        },
    )
    def delete(self, request, id):
        """
        Delete user.
        """
        user = self.get_objects(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CourseView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve list of courses",
        responses={200: openapi.Response("List of courses", CourseSerializer(many=True))},
    )
    def get(self, request):
        """
        Retrieve list of courses.
        """
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new course",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "instructor", "course_details", "type_of_course", "lessons_offered", "assessment", "programming_languages", "frameworks", "price"],
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "instructor": openapi.Schema(type=openapi.TYPE_STRING),
                "course_details": openapi.Schema(type=openapi.TYPE_STRING),
                "type_of_course": openapi.Schema(type=openapi.TYPE_STRING),
                "lessons_offered": openapi.Schema(type=openapi.TYPE_STRING),
                "assessment": openapi.Schema(type=openapi.TYPE_STRING),
                "programming_languages": openapi.Schema(type=openapi.TYPE_STRING),
                "frameworks": openapi.Schema(type=openapi.TYPE_STRING),
                "price": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        ),
        responses={
            201: "Created",
            400: "Bad Request",
        },
    )
    def post(self, request):
        """
        Create a new course.
        """
        serializer = CourseSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class CourseDetails(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve course details",
        responses={200: openapi.Response("Course details", CourseSerializer())},
    )
    def get(self, request, id):
        """
        Retrieve course details.
        """
        course = self.get_objects(id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update course details",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "instructor", "course_details", "type_of_course", "lessons_offered", "assessment", "programming_languages", "frameworks", "price"],
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "instructor": openapi.Schema(type=openapi.TYPE_STRING),
                "course_details": openapi.Schema(type=openapi.TYPE_STRING),
                "type_of_course": openapi.Schema(type=openapi.TYPE_STRING),
                "lessons_offered": openapi.Schema(type=openapi.TYPE_STRING),
                "assessment": openapi.Schema(type=openapi.TYPE_STRING),
                "programming_languages": openapi.Schema(type=openapi.TYPE_STRING),
                "frameworks": openapi.Schema(type=openapi.TYPE_STRING),
                "price": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        ),
        responses={
            200: "OK",
            400: "Bad Request",
        },
    )
    def put(self, request, id):
        """
        Update course details.
        """
        course = self.get_objects(id)
        serializer = CourseSerializer(course, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete course",
        responses={
            204: "No Content",
            404: "Not Found",
        },
    )
    def delete(self, request, id):
        """
        Delete course.
        """
        course = self.get_objects(id)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CommunityView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve list of communities",
        responses={200: openapi.Response("List of communities", CommunitieSerializer(many=True))},
    )
    def get(self, request):
        """
        Retrieve list of communities.
        """
        communities = Communitie.objects.all()
        serializer = CommunitieSerializer(communities, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new community",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "champions", "upvotes"],
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "champions": openapi.Schema(type=openapi.TYPE_STRING),
                "upvotes": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        ),
        responses={
            201: "Created",
            400: "Bad Request",
        },
    )
    def post(self, request):
        """
        Create a new community.
        """
        serializer = CommunitieSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class CommunitieDetails(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve community details",
        responses={200: openapi.Response("Community details", CommunitieSerializer())},
    )
    def get(self, request, id):
        """
        Retrieve community details.
        """
        community = self.get_objects(id)
        serializer = CommunitieSerializer(community)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update community details",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "champions", "upvotes"],
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING),
                "champions": openapi.Schema(type=openapi.TYPE_STRING),
                "upvotes": openapi.Schema(type=openapi.TYPE_INTEGER),
            },
        ),
        responses={
            200: "OK",
            400: "Bad Request",
        },
    )
    def put(self, request, id):
        """
        Update community details.
        """
        community = self.get_objects(id)
        serializer = CommunitieSerializer(community, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete community",
        responses={
            204: "No Content",
            404: "Not Found",
        },
    )
    def delete(self, request, id):
        """
        Delete community.
        """
        community = self.get_objects(id)
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    
class ArticleView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve list of articles",
        responses={200: openapi.Response("List of articles", ArticleSerializer(many=True))},
    )
    def get(self, request):
        """
        Retrieve list of articles.
        """
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new article",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["skill", "course", "project"],
            properties={
                "skill": openapi.Schema(type=openapi.TYPE_STRING),
                "course": openapi.Schema(type=openapi.TYPE_STRING),
                "project": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            201: "Created",
            400: "Bad Request",
        },
    )
    def post(self, request):
        """
        Create a new article.
        """
        serializer = ArticleSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve article details",
        responses={200: openapi.Response("Article details", ArticleSerializer())},
    )
    def get(self, request, id):
        """
        Retrieve article details.
        """
        article = self.get_objects(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update article details",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["skill", "course", "project"],
            properties={
                "skill": openapi.Schema(type=openapi.TYPE_STRING),
                "course": openapi.Schema(type=openapi.TYPE_STRING),
                "project": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: "OK",
            400: "Bad Request",
        },
    )
    def put(self, request, id):
        """
        Update article details.
        """
        article = self.get_objects(id)
        serializer = ArticleSerializer(article, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete article",
        responses={
            204: "No Content",
            404: "Not Found",
        },
    )
    def delete(self, request, id):
        """
        Delete article.
        """
        article = self.get_objects(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
class DeveloperView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve list of developers",
        responses={200: openapi.Response("List of developers", DevelopersSerializer(many=True))},
    )
    def get(self, request):
        """
        Retrieve list of developers.
        """
        developer = Developers.objects.all()
        serializer = DevelopersSerializer(developer, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new developer",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["name", "specialty", "community", "programming_language", "framework"],
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "specialty": openapi.Schema(type=openapi.TYPE_STRING),
                "community": openapi.Schema(type=openapi.TYPE_STRING),
                "programming_language": openapi.Schema(type=openapi.TYPE_STRING),
                "framework": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            201: "Created",
            400: "Bad Request",
        },
    )
    def post(self, request):
        """
        Create a new developer.
        """
        serializer = DevelopersSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeveloperDetails(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve developer details",
        responses={200: openapi.Response("Developer details", DevelopersSerializer())},
    )
    def get(self, request, id):
        """
        Retrieve developer details.
        """
        developer = self.get_object(id)
        serializer = DevelopersSerializer(developer)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update developer details",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["name", "specialty", "community", "programming_language", "framework"],
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "specialty": openapi.Schema(type=openapi.TYPE_STRING),
                "community": openapi.Schema(type=openapi.TYPE_STRING),
                "programming_language": openapi.Schema(type=openapi.TYPE_STRING),
                "framework": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: "OK",
            400: "Bad Request",
        },
    )
    def put(self, request, id):
        """
        Update developer details.
        """
        developer = self.get_object(id)
        serializer = DevelopersSerializer(developer, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete developer",
        responses={
            204: "No Content",
            404: "Not Found",
        },
    )
    def delete(self, request, id):
        """
        Delete developer.
        """
        developer = self.get_object(id)
        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectView(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve list of projects",
        responses={200: openapi.Response("List of projects", ProjectSerializer(many=True))},
    )
    def get(self, request):
        """
        Retrieve list of projects.
        """
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Create a new project",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["framework", "programming_language", "community", "complexity", "modules", "tasks"],
            properties={
                "framework": openapi.Schema(type=openapi.TYPE_STRING),
                "programming_language": openapi.Schema(type=openapi.TYPE_STRING),
                "community": openapi.Schema(type=openapi.TYPE_STRING),
                "complexity": openapi.Schema(type=openapi.TYPE_STRING),
                "modules": openapi.Schema(type=openapi.TYPE_STRING),
                "tasks": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            201: "Created",
            400: "Bad Request",
        },
    )
    def post(self, request):
        """
        Create a new project.
        """
        serializer = ProjectSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
class ProjectDetails(APIView):
    @swagger_auto_schema(
        operation_summary="Retrieve project details",
        responses={200: openapi.Response("Project details", ProjectSerializer())},
    )
    def get(self, request, id):
        """
        Retrieve project details.
        """
        project = self.get_object(id)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Update project details",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["framework", "programming_language", "community", "complexity", "modules", "tasks"],
            properties={
                "framework": openapi.Schema(type=openapi.TYPE_STRING),
                "programming_language": openapi.Schema(type=openapi.TYPE_STRING),
                "community": openapi.Schema(type=openapi.TYPE_STRING),
                "complexity": openapi.Schema(type=openapi.TYPE_STRING),
                "modules": openapi.Schema(type=openapi.TYPE_STRING),
                "tasks": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={
            200: "OK",
            400: "Bad Request",
        },
    )
    def put(self, request, id):
        """
        Update project details.
        """
        project = self.get_object(id)
        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Delete project",
        responses={
            204: "No Content",
            404: "Not Found",
        },
    )
    def delete(self, request, id):
        """
        Delete project.
        """
        project = self.get_object(id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
        
