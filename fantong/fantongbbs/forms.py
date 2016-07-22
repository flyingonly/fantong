from django import forms
from .models import BBSPost


class PostForm(forms.ModelForm):
    class Meta:
        model = BBSPost
        fields = ('PTitle', 'PContent')
