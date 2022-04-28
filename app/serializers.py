
from rest_framework import serializers
from .models import User, Communitie, Course



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        

class CommunitieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Communitie
        fields = '__all__'