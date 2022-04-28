
from django.db import models


# class UserProfile(models.Model):
#     user = models.OneToOneField(User)
#     name = models.CharField(max_length=32)
#     roles = models.ManyToManyField("Role", bank=True, null=True)

#     def __str__(self) -> str:
#         return super().__str__()
    
class User(models.Model):
    name = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    phone = models.IntegerField(unique=True)
    email = models.EmailField(max_length=100, unique=True)
    
    
   


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
        

    def __str__(self) -> str:
            return super().__str__()


class Communitie(models.Model):
    
    CHAMPIONS_LIST = [
        
        'Champions',(
            ('champion1', 'Champion one'),
            ('champion2', 'Champion two'),
            ('champion3', 'Champion three'),
        ),
    ]
    
    
    title = models.CharField(max_length=100)
    champions = models.CharField(max_length=50,
                                 choices = CHAMPIONS_LIST,
                                 default=0),
    upvotes = models.IntegerField(default=0)
    

    def __str__(self) -> str:
        return super().__str__()
    
    
#Add the three other models from this point
class Project(models.Model):
    
    framework = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100)
    community = models.CharField(max_length=100)
    complexity = models.CharField(max_length=100)
    modules = models.CharField(max_length=50)
    tasks = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return super().__str__()
        
    
class Article(models.Model):
    
    skill = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    project = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return super().__str__()
    

class Developers(models.Model):
    
    name = models.CharField(unique=True, max_length=100)
    specialty = models.CharField(max_length=100)
    community = models.CharField(max_length=100)
    programming_language = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    
    
    def __str__(self) -> str:
        return super().__str__()
    
    
