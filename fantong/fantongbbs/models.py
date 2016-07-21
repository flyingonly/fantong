from django.db import models

# Create your models here.

class User(models.Model):
	UAccount = models.EmailField()
	UName = models.CharField(maxlength = 50)
	UPassword = models.CharField(maxlength = 50)
	UImage = models.ImageField()
	UAdmin = models.BooleanField()
	UFollowUserNum = models.IntegerField()
	UFollowPostNum = models.IntegerField()
	UPostNum = models.IntegerField()
	UForbidden = models.BooleanField()

	def __str__(self):
		return self.UName

class Post(models.Model)
	PUserID = models.ForeignKey(User)#帖子作者关系
	PTitle = models.CharField(maxlength = 100)
	PContent = models.TextField()
	PTime = models.DateTimeField()
	PLastComTime = models.DateTimeField()
	PTagLocation = models.CharField(maxlength = 50)
	PTagClass = models.CharField(maxlength = 50)
	PTagPrice = models.CharField(maxlength = 50)
	PKeywords = models.CharField(maxlength = 100)
	PDelete = models.BooleanField()
	PLikeNum = models.IntegerField()
	PSection = models.IntegerField()
	PParentID = models.ForeignKey('self', blank = True, null = True)#帖子父节点关系
	PEssential = models.BooleanField()
	PCheck = models.IntegerField()
	PLimit = models.IntegerField()

	def __str__(self):
		return self.PTitle

class FollowUser(models.Model)
	User1ID = models.ForeignKey(User)
	User2ID = models.ForeignKey(User)

class UserReportPost(models.Model)
	UserID = models.ForeignKey(User)
	PostID = models.ForeignKey(Post)
	ReportContent = models.TextField()

class UserLikePost(models.Model)
	UserID = models.ForeignKey(User)
	PostID = models.ForeignKey(Post)

class UserFollowPost(models.Model)
	UserID = ForeignKey(User)
	PostID = ForeignKey(Post)