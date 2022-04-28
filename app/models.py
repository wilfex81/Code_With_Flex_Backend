
from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.IntegerField(default = 0)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    
    
    COURSE_DETAILS = [
        ('Difficulty levels',(
                    ('easy', 'Easy'),
                    ('medium', 'Intermediate'),
                    ('hard', 'Hard'),
                )
            
        ),
        
    ]
    TYPE_OF_COURSE = [
        ('Course Type ',(
                ('instructor-led', 'Instructor-Led'),
                ('on-demand', 'On-Demand'),
                ('both', 'Both'),
            )
            
        ),
    ]
    
    LESSONS_OFFERED=[
         ('Lessons',(
                    ('1', 'Lesson one'),
                    ('2', 'Lesson two'),
                    ('3', 'Lesson three'),
                )
            
        ),
    ]
    ASSESSMENTS=[
          ('Practical Assessment',(
                ('assessment_one', 'Assessment-One'),   
            )   
        ),
    ]
          
    PROGRAMMING_LANGUAGES = [
        ('Programming Languages',(
                    ('java', 'Java'),
                    ('python', 'Python'),
                    ('javascript', 'JavaScript'),
                )
                ),
    ]
    FRAMEWORKS=[
          ('Frameworks',(
                    ('java', 'Spring'),
                    ('python', 'Django'),
                    ('javascript', 'ReactJs'),
                )
               
         ),
    ] 
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    course_details = models.CharField(
        max_length=50,
        choices= COURSE_DETAILS
    )
    type_of_course = models.CharField(
        max_length=50,
        choices=TYPE_OF_COURSE
    )
    lessons_offered = models.CharField(
        max_length=50,
        choices= LESSONS_OFFERED
    )
    assessment = models.CharField(
        max_length=50,
        choices= ASSESSMENTS
    )
    programming_languages = models.CharField(
        max_length=50,
        choices= PROGRAMMING_LANGUAGES
    )
    frameworks = models.CharField(
        max_length=50,
        choices=FRAMEWORKS
    )
    price = models.IntegerField(default = 0)
        

    def __str__(self):
        return self.title


class Communitie(models.Model):
    
    CHAMPIONS_LIST = [
        
        'Champions',(
            ('champion1', 'Champion1'),
            ('champion2', 'Champion2'),
            ('champion3', 'Champion3'),
        ),
    ]
    
    
    title = models.CharField(max_length=100)
    champions = models.CharField(max_length=50,
                                 choices = CHAMPIONS_LIST,
                                 default=0),
    upvotes = models.IntegerField(default=0)
    

    def __str__(self) -> str:
        return super().__str__()