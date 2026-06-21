from django import forms
from .models import Subject
from django.contrib.auth.models import User
from django. contrib.auth. forms import UserCreationForm


class SignupForm(UserCreationForm):
    email=forms. EmailField(required=True)
    class Meta:
        model=User
        fields=('username','password1','password2', 'email')



class SubjectForm(forms.ModelForm):


    class Meta:

        model=Subject

        fields=[

            "name",

            "hours",

            "streak",

            "completed"

        ]
