from django.shortcuts import render
from .models import Post

def bbs_list(request):
	posts = Post.objects.all()
	return render(request, 'index.html', {'posts':posts})