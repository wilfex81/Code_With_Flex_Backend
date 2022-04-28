from django.contrib import admin
from .models import Communities, Courses, Users

admin.site.register(Communities, 
                    Users,
                    Courses)
