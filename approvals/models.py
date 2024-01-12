from django.db import models
from django.contrib.auth.models import User
# Create your models here.

DEPARTMENTS = [
        ("ELECTRICAL", "Electrical and Electronics Engineering"),
        ("MECHANICAL", "Mechanical Engineering"),
        ("ELECTRONICS", "Electronics and Communications Engineering"),
        ("COMPUTER", "Computer Science Engineering"),
        ("CIVIL", "Civil Engineering"),
        ("CHEMICAL", "Chemical Engineering"),
        ("IT", "Information Technology"),
        ("AI", "Artificial Intelligence"),
        ("CDS", "Computational and Data Science"),
    ]

PROGRAMS = [
        ("BACHELOR", "Bachelors"),
        ("MASTER", "Masters"),
        ("PHD", "PhD"),
    ]

ROLES = [
    ("1", "MIS Officer"),
    ("2", "Head of Department"),
    ("3", "Dean"),
]


class CustomUser(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


class Role(models.Model):
    ROLES = [
    ("MIS", "MIS Officer"),
    ("HOD", "Head of Department"),
    ("DEAN", "Dean"),
]
    name = models.CharField(max_length=20, null=True, choices=ROLES)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email
    
class Student(CustomUser):
  
    student_id = models.CharField(max_length=20, null=True, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    department = models.CharField(max_length=100, null=True, choices=DEPARTMENTS)
    program_type = models.CharField(max_length=100, choices=PROGRAMS)

    
    def __str__(self):
        return self.name
    


class Employee(CustomUser):
    staff_id = models.CharField(max_length=20, null=True, unique=True)
    department = models.CharField(max_length=100, null=True, choices=DEPARTMENTS)
    role = models.CharField(max_length=30, null=True, choices=ROLES)
   
    def __str__(self):
        return self.name


class Template(models.Model):

    PARTICIPANTS = [
    ("1", "MIS Officer"),
    ("2", "Head of Department"),
    ("3", "Dean"),
    ]

    name = models.CharField(max_length=200, null=True)
    archived = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField
    participants = models.CharField(max_length=1, null=True, choices=PARTICIPANTS)

    def __str__(self):
        return self.name
    

class Request(models.Model):
    STATUS = [
    ("Waiting for approval", "Waiting for approval"),
    ("Approved by MIS Officer", "Approved by MIS Officer"),
    ("Approved by Head of Department", "Approved by Head of Department"),
    ("Approved by Dean", "Approved by Dean"),
    ]

    template_id = models.ForeignKey(Template, null=True, on_delete=models.SET_NULL)
    response = models.TextField(max_length=500, null=True)
    status = models.CharField(max_length=100, null=True, default='Waiting for approval', choices=STATUS)
    applicant = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.template_id.name