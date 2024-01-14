from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ApplicationForm(ModelForm):
    class Meta:
        model = Request
        fields = ['template_id', 'response']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

class TemplateForm(ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'participants']