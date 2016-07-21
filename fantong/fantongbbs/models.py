from django.db import models

# Create your models here.


class User(models.Model):
    UAccount = models.EmailField()
    UName = models.CharField(max_length=50)
    UPassword = models.CharField(max_length=50)
    UImage = models.ImageField()
    UAdmin = models.BooleanField()
    UFollowUserNum = models.IntegerField()
    UFollowPostNum = models.IntegerField()
    UPostNum = models.IntegerField()
    UForbidden = models.BooleanField()

    def __str__(self):
        return self.UName


class Post(models.Model):
    PUserID = models.ForeignKey(User)  # 帖子作者关系
    PTitle = models.CharField(max_length=100)
    PContent = models.TextField()
    PTime = models.DateTimeField()
    PLastComTime = models.DateTimeField()
    LOCATION_CHOICE = (
        (u'海淀区', u'海淀区'),
        (u'朝阳区', u'朝阳区'),
        (u'东城区', u'东城区'),
        (u'西城区', u'西城区'),
        (u'丰台区', u'丰台区'),
        (u'石景山区', u'石景山区'),
        (u'大兴区', u'大兴区'),
        (u'通州区', u'通州区'),
        (u'昌平区', u'昌平区'),
        (u'房山区', u'房山区'),
        (u'顺义区', u'顺义区'),
        (u'门头沟区', u'门头沟区'),
        (u'怀柔区', u'怀柔区'),
        (u'平谷区', u'平谷区'),
        (u'延庆县', u'延庆县'),
        (u'密云县', u'密云县'),
    )
    CLASS_CHOICE = (
        (u'火锅', u'火锅'),
        (u'自助餐', u'自助餐'),
        (u'咖啡厅', u'咖啡厅'),
        (u'烧烤', u'烧烤'),
        (u'面包', u'面包'),
        (u'甜点', u'甜点'),
        (u'韩国料理', u'韩国料理'),
        (u'日本菜', u'日本菜'),
        (u'西餐', u'西餐'),
        (u'小吃快餐', u'小吃快餐'),
        (u'北京菜', u'北京菜'),
        (u'江浙菜', u'江浙菜'),
        (u'粤菜', u'粤菜'),
        (u'清真菜', u'清真菜'),
        (u'素菜', u'素菜'),
        (u'川菜', u'川菜'),
        (u'新疆菜', u'新疆菜'),
        (u'西北菜', u'西北菜'),
        (u'海鲜', u'海鲜'),
        (u'东南亚菜', u'东南亚菜'),
        (u'家常菜', u'家常菜'),
        (u'云南菜', u'云南菜'),
        (u'贵州菜', u'贵州菜'),
        (u'鲁菜', u'鲁菜'),
        (u'湖北菜', u'湖北菜'),
        (u'东北菜', u'东北菜'),
        (u'湘菜', u'湘菜'),
        (u'其他', u'其他'),
    )
    PRICE_CHOICE = (
        (u'50以下', u'50以下'),
        (u'50-100', u'50-100'),
        (u'100-300', u'100-300'),
        (u'300以上', u'300以上'),
    )
    PTagLocation = models.CharField(max_length=50, choices=LOCATION_CHOICE)
    PTagClass = models.CharField(max_length=50, choices=CLASS_CHOICE)
    PTagPrice = models.CharField(max_length=50, choices=PRICE_CHOICE)
    PKeywords = models.CharField(max_length=100)
    PDelete = models.BooleanField()
    PLikeNum = models.IntegerField()
    PSection = models.IntegerField()
    PParentID = models.ForeignKey('self', blank=True, null=True)  # 帖子父节点关系
    PEssential = models.BooleanField()
    PCheck = models.IntegerField()
    PLimit = models.IntegerField()

    def __str__(self):
        return self.PTitle


class FollowUser(models.Model):
    User1ID = models.ForeignKey(User, related_name='follower')
    User2ID = models.ForeignKey(User, related_name='followee')


class UserReportPost(models.Model):
    UserID = models.ForeignKey(User)
    PostID = models.ForeignKey(Post)
    ReportContent = models.TextField()


class UserLikePost(models.Model):
    UserID = models.ForeignKey(User)
    PostID = models.ForeignKey(Post)


class UserFollowPost(models.Model):
    UserID = models.ForeignKey(User)
    PostID = models.ForeignKey(Post)
