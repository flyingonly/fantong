from django.shortcuts import render
from .models import BBSPost


def bbs_list(request):
    posts = BBSPost.objects.all()
    return render(request, 'index.html', {'posts': posts})
