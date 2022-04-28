from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    phone = models.IntegerField(default = 0)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.name


class Courses(models.Model):
    
    COURSE_DETAILS = [
        ('Difficulty levels'(
                'Basic',(
                    ('easy', 'Easy'),
                    ('medium', 'Medium'),
                    ('hard', 'Hard'),
                ),
                'Intermediate',(
                    ('easy', 'Easy'),
                    ('medium', 'Medium'),
                    ('hard', 'Hard'),
                ),
                'Hard',(
                    ('easy', 'Easy'),
                    ('medium', 'Medium'),
                    ('hard', 'Hard'),
                ),
            
                )
            
        )
        
        ('Course Type '(
                ('instructor-led', 'Instructor-Led'),
                ('on-demand', 'On-Demand'),
                ('both', 'Both'),
            )
            
        )
        
        ('Lessons'(
                'Lesson 1',(
                    ('lecturer_one', 'Lecturer_One'),
                    ('lecturer_two', 'Lecturer_Two'),
                    ('lecturer_three', 'Lecturer_Three'),
                ),
                'Lesson 2',(
                    ('lecturer_one', 'Lecturer_One'),
                    ('lecturer_two', 'Lecturer_Two'),
                    ('lecturer_three', 'Lecturer_Three'),
                ),
                'Lesson 3',(
                    ('lecturer_one', 'Lecturer_One'),
                    ('lecturer_two', 'Lecturer_Two'),
                    ('lecturer_three', 'Lecturer_Three'),
                ),
            
                )
            
        )
        
        ('Practical Assessment '(
                ('assessment_one', 'Assessment-One'),   
            )   
        )
        
        
        
    ]    
    
    
    SPECIALTY = [
        ('Programming Languages'(
                    ('java', 'Java'),
                    ('python', 'Python'),
                    ('javascript', 'JavaScript'),
                ),
                )
        
        ('Frameworks'(
                'Java',(
                    ('spring', 'Spring'),
                    ('hibernate', 'Hibernate'),
                    ('struts', 'Struts'),
                ),
                'Python',(
                    ('flask', 'Flask'),
                    ('django', 'Django'),
                ),
                'Javascript',(
                    ('reactjs', 'ReactJs'),
                    ('vuejs', 'VueJs'),
                    ('nodejs', 'NodeJs'),
                ),
                ),
        )
    ]
    
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    course_details = models.CharField(
        max_length=50,
        choices= COURSE_DETAILS
    )
    specialty = models.CharField(
        max_length=50,
        choices=SPECIALTY
    )
    price = models.IntegerField(default = 0)
        

    def __str__(self) -> str:
        return super().__str__()


class Communities(models.Model):
    
    CHAMPIONS_LIST = [
        
        'Champions'(
            ('champion1', 'Champion1'),
            ('champion2', 'Champion2'),
            ('champion3', 'Champion3'),
        )
    ]
    
    
    title = models.CharField(max_length=100)
    champions = models.CharField(max_length=50,
                                 choices = CHAMPIONS_LIST,
                                 default=0),
    upvotes = models.IntegerChoices(default=0)
    

    def __str__(self) -> str:
        return super().__str__()