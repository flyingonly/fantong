from django import forms
from .models import Post
from django.contrib.auth.models import User
from registration.forms import RegistrationForm


class RegistrationForm(RegistrationForm):
    UFollowUserNum = forms.IntegerField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "UFollowUserNum")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.BBSUser.UFollowUserNum = self.cleaned_data["UFollowUserNum"]
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'content')