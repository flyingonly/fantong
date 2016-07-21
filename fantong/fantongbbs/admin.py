from django.contrib import admin
from .models import User, Post, FollowUser, UserReportPost, UserLikePost, UserFollowPost

admin.site.register(User)
admin.site.register(Post)
admin.site.register(FollowUser)
admin.site.register(UserReportPost)
admin.site.register(UserLikePost)
admin.site.register(UserFollowPost)
# Register your models here.
