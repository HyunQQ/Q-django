from django import forms
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__' 모든 필드 사용시
        fields =('title','text')


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']