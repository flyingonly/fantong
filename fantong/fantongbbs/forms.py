from django import forms
from .models import BBSPost, BBSUser
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class PostForm(forms.ModelForm):
    class Meta:
        model = BBSPost
        fields = ('PTitle', 'PContent')


class ImageForm(forms.ModelForm):
    class Meta:
        model = BBSUser
        fields = ('UImage',)

class ChangepwdForm(forms.Form):
    old_pwd = forms.CharField(label='OLD PASSWORD', widget=forms.PasswordInput)
    new_pwd = forms.CharField(label='NEW PASSWORD', widget=forms.PasswordInput)
    new_pwd2 = forms.CharField(label='CONFIRM', widget=forms.PasswordInput)

    def pwd_validate(self, p1, p2):
        return p1 == p2
