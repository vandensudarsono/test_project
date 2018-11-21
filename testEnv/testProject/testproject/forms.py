# testproject/forms.py

from django import forms
from testproject.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User#Form
        fields = ('username', 'password', 'email')

class UserProfileInfoForm(forms.ModelForm):
   class Meta():
        model = UserProfileInfo
        fields = ('portofolio_site', 'profile_pic')


