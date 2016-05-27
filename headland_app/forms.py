from django import forms
from models import Post, UserProfile
from django.contrib.auth.models import User
from registration.forms import RegistrationForm
from awesome_avatar import forms as avatar_forms


class AvatarChangeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']


class UploadAndCropImageForm(forms.ModelForm):
    image = avatar_forms.AvatarField()


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user",)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


