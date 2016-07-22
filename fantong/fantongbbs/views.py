from django.shortcuts import render
from .models import BBSPost, BBSUser
from .forms import PostForm
from .forms import ImageForm


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


'''def bbs_list(request):
    params = request.POST if request.method == 'POST' else None
    form = ImageForm(params)
    if form.is_valid():
        data = form.cleaned_data
        user = BBSUser.objects.get(user=request.user)
        print(user)
        user.UFollowUserNum = data['UFollowUserNum']
        user.save()
    posts = BBSUser.objects.all()
    return render(request, 'index.html', {'posts': posts, 'form': form})
'''