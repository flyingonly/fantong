from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class BBSUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    UNickname = models.TextField(blank=True)
    UImage = models.ImageField(null=True, blank=True)
    UAdmin = models.BooleanField(default=False)
    UFollowUserNum = models.IntegerField(default=0)
    UFollowPostNum = models.IntegerField(default=0)
    UPostNum = models.IntegerField(default=0)
    UForbidden = models.BooleanField(default=False)
    UForbiddenToTime = models.DateTimeField(null=True, blank=True)


class Taginformation(models.Model):
    TInfo = models.CharField(max_length=50, blank=True)
    TAG_CLASS = (
        (u'价位', u'价位'),
        (u'菜系', u'菜系'),
        (u'位置', u'位置'),
    )
    TClass = models.CharField(max_length=50, blank=True, choices=TAG_CLASS)


    def __str__(self):
        return self.TInfo


class BBSPost(models.Model):
    PUserID = models.ForeignKey(User)  # 帖子作者关系
    PTitle = models.CharField(max_length=100, blank=True)
    PContent = models.TextField()
    PTime = models.DateTimeField(default=timezone.now)
    PLastComTime = models.DateTimeField(default=timezone.now)
    PTagLocation = models.ForeignKey(
        Taginformation, limit_choices_to={'TClass': u'位置'}, related_name='loc', blank=True, null=True, on_delete=models.SET_NULL)
    PTagClass = models.ForeignKey(
        Taginformation, limit_choices_to={'TClass': u'菜系'}, related_name='cla', blank=True, null=True, on_delete=models.SET_NULL)
    PTagPrice = models.ForeignKey(
        Taginformation, limit_choices_to={'TClass': u'价位'}, related_name='pri', blank=True, null=True, on_delete=models.SET_NULL)
    PKeywords = models.CharField(max_length=100, blank=True)
    PDelete = models.BooleanField(default=False)
    PLikeNum = models.IntegerField(default=0)
    PSection = models.IntegerField(default=1)
    PParentID = models.ForeignKey('self', blank=True, null=True)  # 帖子父节点关系
    PEssential = models.BooleanField(default=False)
    PCheck = models.IntegerField(default=0)
    PLimit = models.IntegerField(default=0)
    PReplyNum = models.IntegerField(default=0)
    PTop = models.IntegerField(default=0)
    PVisitNum = models.IntegerField(default=0)

    def __str__(self):
        return self.PTitle


class FollowUser(models.Model):
    User1ID = models.ForeignKey(User, related_name='follower')
    User2ID = models.ForeignKey(User, related_name='followee')


class UserReportPost(models.Model):
    UserID = models.ForeignKey(User)
    PostID = models.ForeignKey(BBSPost)
    ReportContent = models.TextField()


class UserLikePost(models.Model):
    UserID = models.ForeignKey(User)
    PostID = models.ForeignKey(BBSPost)


class UserFollowPost(models.Model):
    UserID = models.ForeignKey(User)
    PostID = models.ForeignKey(BBSPost)
