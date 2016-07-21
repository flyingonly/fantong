from django.shortcuts import render
from .models import Post

def bbs_list(request):
	posts = Post.object.all()
	return render(request, 'templates/index.html', {'posts':posts})