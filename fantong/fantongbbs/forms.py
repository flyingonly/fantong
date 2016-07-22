from django import forms
from .models import BBSPost,BBSUser
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = BBSPost
        fields = ('PTitle', 'PContent')

class ImageForm(forms.ModelForm):
    class Meta:
        model = BBSUser
        fields = ('UFollowUserNum',)