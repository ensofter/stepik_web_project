from django import forms
from .models import Question, Answer
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class AskForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('title', 'text')

class AnswerForm(forms.ModelForm):


    class Meta:
        model = Answer
        fields = ('text', 'question')

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True,)
    email = forms.EmailField(max_length=24)
    password1 = forms.PasswordInput()
    password2 = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField()

