from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import (ArticleDetails, ArticleView, CommunitieDetails,
                       CommunityView, CourseDetails,
                       CourseView, DeveloperDetails,
                       DeveloperView, ProjectDetails, ProjectView, UserDetails,
                       UserView)

urlpatterns = [
    path('user/', UserView.as_view()),
    path('userdetails/<int:id>/', UserDetails.as_view()),
    
    path('course/', CourseView.as_view()),
    path('coursedetails/<int:id>/', CourseDetails.as_view()),
    
    
    path('developer/', DeveloperView.as_view()),
    path('developerdetails/<int:id>/', DeveloperDetails.as_view()),
    
    
    path('project/', ProjectView.as_view()),
    path('projectdetails/<int:id>/', ProjectDetails.as_view()),
    
    
    path('article/', ArticleView.as_view()),
    path('articledetails/<int:id>/', ArticleDetails.as_view()),
    
    
    path('community/', CommunityView.as_view()),
    path('communitydetails/<int:id>/', CommunitieDetails.as_view()),

]

# router = DefaultRouter()
# router.register('user', UserViewSet, basename='user')
# router.register('course', CourseViewSet, basename='course')
# router.register('community', CommunityViewSet, basename='community')


# urlpatterns = [
#     path('user/', include(router.urls)),
#     path('user/<int:pk>/', include(router.urls)),
    
#     path('course/', include(router.urls)),
#     path('course/<int:pk>/', include(router.urls)),
    
#     path('community/', include(router.urls)),
#     path('community/<int:pk>/', include(router.urls)),
# ]
