from django.shortcuts import render
from .models import BBSPost
from .forms import PostForm


def bbs_list(request):
    params = request.POST if request.method == 'POST' else None
    form = PostForm(params)
    if form.is_valid():
        post = form.save(commit=False)
        post.PUserID = request.user
        post.save()
        form = PostForm()
    posts = BBSPost.objects.all()
    return render(request, 'index.html', {'posts': posts, 'form': form})

def changepassword(request, username):
	error = []
	if request.method == 'POST':
		form = ChangepwdForm(request.POST)
		if form.is_valid()
			data = form.cleaned_data
			user = authenticate(username=username, password=data['old_pwd'])
			if user is not None:
				if data['new_pwd'] == data['new_pwd2']:
					newuser = User.objects.get(username_exact = username)