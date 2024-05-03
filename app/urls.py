from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import (ArticleDetails, ArticleView, CommunitieDetails,
                       CommunityView, CourseDetails,
                       CourseView, DeveloperDetails,
                       DeveloperView, ProjectDetails, ProjectView, UserDetails,
                       UserView)

urlpatterns = [
    path('user/', UserView.as_view(), name = 'user'),
    path('userdetails/<int:id>/', UserDetails.as_view()),
    
    path('course/', CourseView.as_view(), name = 'course'),
    path('coursedetails/<int:id>/', CourseDetails.as_view()),
    
    
    path('developer/', DeveloperView.as_view(), name = 'developer'),
    path('developerdetails/<int:id>/', DeveloperDetails.as_view()),
    
    
    path('project/', ProjectView.as_view(), name = 'project'),
    path('projectdetails/<int:id>/', ProjectDetails.as_view()),
    
    
    path('article/', ArticleView.as_view(), name = 'article'),
    path('articledetails/<int:id>/', ArticleDetails.as_view()),
    
    
    path('community/', CommunityView.as_view(), name = 'community'),
    path('communitydetails/<int:id>/', CommunitieDetails.as_view()),

]

