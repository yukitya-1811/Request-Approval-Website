from django.db import models

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
    ("MIS", "MIS Officer"),
    ("HOD", "Head of Department"),
    ("DEAN", "Dean"),
]


class CustomUser(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


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
    id = models.CharField(max_length=10,null=True)
    name = models.CharField(max_length=200, null=True)
    archived = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField

    def __str__(self):
        return self.name
    

class Request(models.Model):
    STATUS = [
    ("WAITING", "Waiting for approval"),
    ("APPROVED", "Approved"),
    ]


    id = models.CharField(max_length=10,null=True)
    template_id = models.OneToOneField(Template)
    response = models.TextField(max_length=500, null=True)
    status = models.CharField(max_length=20, null=True, choices=STATUS)
    participants = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    