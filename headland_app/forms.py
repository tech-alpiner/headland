from django import forms
from models import Post
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)