from django.shortcuts import render, render_to_response
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from .models import BBSPost, BBSUser, FollowUser, UserFollowPost, UserLikePost, Taginformation
from .forms import PostForm, IndexPostForm
from .forms import ChangepwdForm
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import os
from django.utils import timezone
import json

def rank(request, param):
    if request.user.is_anonymous():
        user = None
    else:
        user = request.user.bbsuser
    if param == "visit":
        posts = BBSPost.objects.filter(PParentID__isnull=True).filter(PDelete=False).order_by('-PVisitNum')
        mode = "访问量排行"
    elif param == "like":
        posts = BBSPost.objects.filter(PParentID__isnull=True).filter(PDelete=False).order_by('-PLikeNum')
        mode = "点赞数排行"
    elif param == "reply":
        posts = BBSPost.objects.filter(PParentID__isnull=True).filter(PDelete=False).order_by('-PReplyNum')
        mode = "回复数排行"
    else:
        posts = None
    return render(request, 'paihang.html', {'posts': posts, 'user': user, 'mode': mode})


def search_by_tag(request, inputword):
    if request.user.is_anonymous():
        user = None
    else:
        user = request.user.bbsuser
    searchs = inputword.split('_')
    posts = BBSPost.objects.filter(PParentID=None).filter(PDelete=False)
    if len(searchs) == 3:
        if searchs[0] != '':
            posts = posts.filter(PTagLocation__TInfo=searchs[0])
        if searchs[1] != '':
            posts = posts.filter(PTagClass__TInfo=searchs[1])
        if searchs[2] != '':
            posts = posts.filter(PTagPrice__TInfo=searchs[2])

    return render(request, 'multisearch.html', {'posts': posts, 'user': user})



@csrf_exempt
def ajax_get_tag(request):
    tags = list(Taginformation.objects.all())
    ans = []
    for tag in tags:
        ans.append([tag.TClass, tag.TInfo])
    return HttpResponse(json.dumps(ans), content_type="application/json")


@csrf_exempt
def ajax_change_nickname(request, userid):
    user = BBSUser.objects.get(user=userid)
    user.UNickname = request.POST['content']
    user.save()
    return HttpResponse("修改成功")


@csrf_exempt
def ajax_append_image(request):
    data = request.FILES['file']
    path = default_storage.save(data.name, ContentFile(data.read()))
    return HttpResponse(path)


@csrf_exempt
def ajax_append_files(request):
    data_list = request.FILES
    key_list = list(data_list.keys())
    ans_list = []
    for x in key_list:
        data = data_list[x]
        path = default_storage.save(data.name, ContentFile(data.read()))
        ans_list.append(path)
    return HttpResponse(json.dumps(ans_list), content_type="application/json")


@csrf_exempt
def ajax_deal(request):
    print(request)
    post = BBSPost()
    Parent = BBSPost.objects.get(id=int(request.POST['PParentID']))
    post.PUserID = request.user
    request.user.bbsuser.UPostNum += 1
    post.PParentID = Parent
    post.PContent = request.POST['PContent'].replace("\r\n","<br>")
    post.save()
    request.user.bbsuser.save()
    post.PParentID.PParentID.PLastComTime = post.PTime
    post.PParentID.PParentID.PReplyNum += 1
    post.PParentID.PParentID.save()
    return HttpResponse('hello')


def search_postbycontent(request,searchword):
    if request.POST.get('search'):
        return HttpResponseRedirect('/search/post/'+request.POST['search'].replace(" ", "_"))
    if request.user.is_anonymous():
        user = None
    else:
        user = request.user.bbsuser
    search = searchword.split("_")
    posts = BBSPost.objects.all()
    for searchthing in search:
        if searchthing != '':
            posts = posts.filter(PContent__contains=searchthing)
    return render(request, 'searchPost.html', {'posts': posts, 'user': user})

def search_userbyusername(request,searchword):
    if request.POST.get('search'):
        return HttpResponseRedirect('/search/user/'+request.POST['search'].replace(" ", ''))
    user = request.user.bbsuser
    users = BBSUser.objects.filter(UNickname__contains=searchword)
    return render(request, 'searchUser.html', {'users': users, 'user': user})


def update_time(request):
    return HttpResponseRedirect('/personal/' + request.user.username)


def bbs_list(request):
    if request.POST.get('search'):
        return HttpResponseRedirect('/search/post/'+request.POST['search'].replace(" ","_"))
    params = request.POST if request.method == 'POST' else None
    if request.user.is_anonymous():
        user = None
    else:
        user = BBSUser.objects.get(user=request.user)
    form = IndexPostForm(params)
    if form.is_valid():
        print(request.POST)
        post = form.save(commit=False)
        post.PUserID = request.user
        request.user.bbsuser.UPostNum += 1
        post.PContent = form.cleaned_data['PContent'].replace("\r\n","<br>")
        post.PTagLocation = Taginformation.objects.filter(TClass='位置').get(TInfo=request.POST['PTagLocation'])
        post.PTagClass = Taginformation.objects.filter(TClass='菜系').get(TInfo=request.POST['PTagClass'])
        post.PTagPrice = Taginformation.objects.filter(TClass='价位').get(TInfo=request.POST['PTagPrice'])
        post.save()
        request.user.bbsuser.save()
        form = IndexPostForm()
    posts = BBSPost.objects.filter(PParentID__isnull=True).filter(PDelete=False).order_by('-PLastComTime')
    tags = Taginformation.objects.all()
    return render(request, 'index.html', {'posts': posts, 'form': form, 'user': user, 'tags': tags})


def get_user(request, param):
    if request.POST.get('search'):
        return HttpResponseRedirect('/search/user/'+request.POST['search'].replace(" ", ''))
    if not request.user.is_anonymous():
        if User.objects.filter(username=param).exists():
            if param == request.user.username or request.user.bbsuser.UAdmin:
                hostUser = User.objects.get(username=param)
                posts = BBSPost.objects.filter(PUserID=hostUser)
                if BBSUser.objects.filter(user=hostUser).exists():
                    user = BBSUser.objects.get(user=hostUser)
                else:
                    newuser = BBSUser()
                    newuser.user = hostUser
                    newuser.UNickname = hostUser.username
                    user = newuser
                    newuser.save()
                return render(request, 'personal.html', {'posts': posts, 'user': user})
            else:
                visitedUser = User.objects.get(username=param)
                visitedUser = BBSUser.objects.get(user=visitedUser)
                posts = BBSPost.objects.filter(PUserID=visitedUser.user)
                if FollowUser.objects.filter(User1ID=request.user, User2ID=visitedUser.user).exists():
                    haveFollowed = True
                else:
                    haveFollowed = False
                return render(request, 'visitPersonal.html', {'visitedUser': visitedUser, 'posts': posts, 'haveFollowed': haveFollowed})
        else:
            return HttpResponse("该用户不存在")
    else:
        return HttpResponse("请登录以查看他人信息")

@csrf_exempt
def follow_user_deal(request):
    user1 = User.objects.get(id=int(request.POST['user1ID']))
    user1 = BBSUser.objects.get(user=user1)
    user2 = User.objects.get(id=int(request.POST['user2ID']))
    user2 = BBSUser.objects.get(user=user2)

    if FollowUser.objects.filter(User1ID=user1.user, User2ID=user2.user).exists():
        FollowUser.objects.get(User1ID=user1.user, User2ID=user2.user).delete()
        user1.UFollowUserNum -= 1
        user1.save()
    else:
        newFollowUser = FollowUser()
        newFollowUser.User1ID = user1.user
        newFollowUser.User2ID = user2.user
        newFollowUser.save()
        user1.UFollowUserNum += 1
        user1.save()
    return HttpResponse('follow success')

@csrf_exempt
def follow_post_deal(request):
    user = User.objects.get(id=int(request.POST['userID']))
    user = BBSUser.objects.get(user=user)
    post = BBSPost.objects.get(id=int(request.POST['postID']))

    if UserFollowPost.objects.filter(UserID=user.user, PostID=post).exists():
        UserFollowPost.objects.get(UserID=user.user, PostID=post).delete()
        user.UFollowPostNum -= 1
        user.save()
    else:
        newFollowPost = UserFollowPost()
        newFollowPost.UserID = user.user
        newFollowPost.PostID = post
        newFollowPost.save()
        user.UFollowPostNum += 1
        user.save()
    return HttpResponse('follow success')

@csrf_exempt
def like_post_deal(request):
    user = User.objects.get(id=int(request.POST['userID']))
    user = BBSUser.objects.get(user=user)
    post = BBSPost.objects.get(id=int(request.POST['postID']))

    if UserLikePost.objects.filter(UserID=user.user, PostID=post).exists():
        UserLikePost.objects.get(UserID=user.user, PostID=post).delete()
        post.PLikeNum -= 1
        post.save()
    else:
        newLikePost = UserLikePost()
        newLikePost.UserID = user.user
        newLikePost.PostID = post
        newLikePost.save()
        post.PLikeNum += 1
        post.save()
    return HttpResponse('follow success')

def bbs_post_detail(request, param):
    if request.POST.get('search'):
        return HttpResponseRedirect('/search/post/'+request.POST['search'].replace(" ","_"))
    threadID = int(param)
    if request.user.is_anonymous():
        user = None
    else:
        user = BBSUser.objects.get(user=request.user)
    PPost = BBSPost.objects.get(id=threadID)
    PPost.PVisitNum += 1
    params = request.POST if request.method == 'POST' else None
    form = PostForm(params)
    if form.is_valid():
        post = form.save(commit=False)
        post.PContent = form.cleaned_data['PContent'].replace("\r\n","<br>")
        post.PUserID = request.user
        request.user.bbsuser.UPostNum += 1
        PPost.PReplyNum += 1
        post.PParentID = PPost
        post.save()
        request.user.bbsuser.save()
        form = PostForm()
        post.PParentID.PLastComTime = post.PTime
        post.PParentID.save()
    PPost.save()
    posts = list(BBSPost.objects.filter(id=threadID)) + \
        list(BBSPost.objects.filter(PParentID=threadID).filter(PDelete=False))
    for i in range(1, len(posts)):
        posts[i] = [posts[i]] + \
            list(BBSPost.objects.filter(PParentID=posts[i].id).filter(PDelete=False))
    form = PostForm()
    if user == None or posts[0].PUserID == user.user:
        return render(request, 'postDetail.html', {'posts': posts, 'form': form, 'user': user})
    else:
        if UserFollowPost.objects.filter(UserID=request.user, PostID=posts[0]).exists():
            haveFollowed = True
        else:
            haveFollowed = False
        if UserLikePost.objects.filter(UserID=request.user, PostID=posts[0]).exists():
            haveLiked = True
        else:
            haveLiked = False
        return render(request, 'postDetail.html', {'posts': posts, 'form': form, 'user': user, 'haveFollowed': haveFollowed, 'haveLiked': haveLiked})


@csrf_exempt
def delete_post_deal(request):
    post = BBSPost.objects.get(id=int(request.POST['postID']))
    print(post.id)
    comPosts = BBSPost.objects.filter(PParentID=post)
    for comPost in comPosts:
        miniPosts = BBSPost.objects.filter(PParentID=comPost)
        for miniPost in miniPosts:
            miniPost.PUserID.bbsuser.UPostNum -= 1
            miniPost.PUserID.bbsuser.save()
            miniPost.PDelete = True
            miniPost.save()
        comPost.PUserID.bbsuser.UPostNum -= 1
        comPost.PUserID.bbsuser.save()
        comPost.PDelete = True
        comPost.save()
    post.PUserID.bbsuser.UPostNum -= 1
    post.PUserID.bbsuser.save()
    post.PDelete = True
    post.save()
    if post.PParentID:
        return HttpResponse("delete comment success")
    else:
        return HttpResponse("delete thread success")

def change_password(request, username):
    error = []
    user = BBSUser.objects.get(user=request.user)
    if request.method == 'POST':
        form = ChangepwdForm(request.POST)
        print('as')
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=username, password=data['old_pwd'])
            if user is not None:
                if data['new_pwd'] == data['new_pwd2']:
                    newuser = User.objects.get(username__exact=username)
                    newuser.set_password(data['new_pwd'])
                    newuser.save()
                    return HttpResponseRedirect('/accounts/login/')
                else:
                    error.append('Please input the same password')
            else:
                error.append('Please correct the old password')
        else:
            error.append('Please input the required domain')
    else:
        form = ChangepwdForm()
    return render_to_response('changepassword.html', {'form': form, 'error': error, 'user': user}, context_instance=RequestContext(request))


def change_image(request, username):
    files = request.FILES if request.method == 'POST' else None
    user = BBSUser.objects.get(user__username=username)
    if files:
        user = BBSUser.objects.get(user__username=username)
        user.UImage = files['UImage']
        user.save()
    posts = BBSUser.objects.all()
    return render(request, 'revisehead.html', {'posts': posts, 'user': user})

@csrf_exempt
def forbid_user_deal(request):
    user = User.objects.get(id=int(request.POST['toBeForbiddenUserID']))
    user = BBSUser.objects.get(user=user)
    if user.UForbidden:
        user.UForbidden = False
    else:
        user.UForbidden = True
    user.save()
    return HttpResponse('forbid success')

@csrf_exempt
def delete_user_deal(request, param):
    if request.user.bbsuser.UAdmin:
        user = User.objects.get(username=param)
        #删除帖子
        posts = BBSPost.objects.filter(PUserID=user).order_by('-PTime')
        for post in posts:
            comPosts = BBSPost.objects.filter(PParentID=post)
            for comPost in comPosts:
                miniPosts = BBSPost.objects.filter(PParentID=comPost)
                for miniPost in miniPosts:
                    miniPost.PUserID.bbsuser.UPostNum -= 1
                    miniPost.PUserID.bbsuser.save()
                    UserFollowPost.objects.filter(PostID=miniPost).delete()
                    UserLikePost.objects.filter(PostID=miniPost).delete()
                    miniPost.delete()
                comPost.PUserID.bbsuser.UPostNum -= 1
                comPost.PUserID.bbsuser.save()
                UserFollowPost.objects.filter(PostID=comPost).delete()
                UserLikePost.objects.filter(PostID=comPost).delete()
                comPost.delete()
            post.PUserID.bbsuser.UPostNum -= 1
            post.PUserID.bbsuser.save()
            UserFollowPost.objects.filter(PostID=post).delete()
            UserLikePost.objects.filter(PostID=post).delete()
            post.delete()
        #删除用户关注关系
        FollowUser.objects.filter(User1ID=user).delete()
        followUsers = FollowUser.objects.filter(User2ID=user)
        for followUser in followUsers:
            followUser.User1ID.bbsuser.UFollowUserNum -= 1
        followUsers.delete()
        #删除用户收藏帖子关系
        UserFollowPost.objects.filter(UserID=user).delete()
        #删除用户点赞帖子关系
        UserLikePost.objects.filter(UserID=user).delete()

        user.bbsuser.delete()
        user.delete()
        return HttpResponse('用户已被删除')
    else:
        return HttpResponse('没有权限')