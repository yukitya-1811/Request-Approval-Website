from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Employee)
admin.site.register(Template)
admin.site.register(Request)
admin.site.register(Role)
