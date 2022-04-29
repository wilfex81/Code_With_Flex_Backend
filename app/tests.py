from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User

class UserTests(APITestCase):
    def test_create_user(self):
        
        url = reverse('user')
        data = {'name': 'Brian', 'username': 'dev', 'phone': '072564812', 'email': 'brian@gmail.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED )
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Brian')
        print('Test passed')

# class CourseTests(APITestCase):
#     def test_create_course(self):
        
#         url = reverse('course')
#         data = {'title': 'Frontend'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 1)
#         self.assertEqual(User.objects.get().title, 'Frontend')


class DeveloperTests(APITestCase):      
    def test_create_developer(self):
        
        url = reverse('developer')
        data = {'name': 'Elvis', 'specialty': 'django', 'community': 'community', 'programming_language': 'python', 'framework' :' django'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'Elvis')
        print("Test Passed")


class ProjectTests(APITestCase):     
    def test_create_project(self):
        
        url = reverse('project')
        data = {'framework': 'django', 'programming_language': 'python','community': 'my community', 'complexity': 'Basic' , 'modules': 'module1', 'tasks': 'task1'   }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().framework, 'django')
        print("Test Passed")

# class CommunityTests(APITestCase):
    
#     def test_create_community(self):
            
#         url = reverse('community')
#         data = {'title': 'my community'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(User.objects.count(), 1)
#         self.assertEqual(User.objects.get().title, 'my community')

class ArticleTests(APITestCase):
    
    def test_create_article(self):
            
        url = reverse('article')
        data = {'skill': 'django', 'course': 'Backend', 'project': 'Assigned'  }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().skill, 'django')
        print("Test Passed")