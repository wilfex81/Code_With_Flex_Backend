from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import CommunityViewSet, CourseViewSet, UserViewSet


router = DefaultRouter()
router.register('user', UserViewSet, basename='user')
router.register('course', CourseViewSet, basename='course')
router.register('community', CommunityViewSet, basename='community')


urlpatterns = [
    path('user/', include(router.urls)),
    path('user/<int:pk>/', include(router.urls)),
    
    path('course/', include(router.urls)),
    path('course/<int:pk>/', include(router.urls)),
    
    path('community/', include(router.urls)),
    path('community/<int:pk>/', include(router.urls)),
]
