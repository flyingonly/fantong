from django.shortcuts import render
from .models import BBSPost


def bbs_list(request):
	params = request.POST if request.method == 'POST' else None
	form = PostForm(params)
	if form.is_valid():
		post - form.save(commit=False)
		post.author = request.user
		post.save()
		form = PostForm()
	posts = BBSPost.objects.all()
	return render(request, 'index.html', {'posts': posts})