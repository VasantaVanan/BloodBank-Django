from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doner
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class DonerForm(forms.ModelForm):
    class Meta:
        model = Doner
        fields = ['name', 'age', 'blood_group', 'address', 'contact_no']