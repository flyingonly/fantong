from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import BBSUser, BBSPost, FollowUser, UserReportPost, UserLikePost, UserFollowPost
from django.contrib.auth.models import User


class BBSUserInline(admin.StackedInline):
    model = BBSUser
    can_delete = False
    verbose_name_plural = 'BBSUser'


class UserAdmin(BaseUserAdmin):
    inlines = (BBSUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(BBSPost)
admin.site.register(FollowUser)
admin.site.register(UserReportPost)
admin.site.register(UserLikePost)
admin.site.register(UserFollowPost)
# Register your models here.
