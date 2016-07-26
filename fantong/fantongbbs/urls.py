from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.bbs_list, name='index'),
    url(r'^personal/(\w+)/$', views.get_user),
    url(r'^accounts/profile/$', views.update_time),
    url(r'^accounts/profile/$', views.update_time),
    url(r'changepassword/(.+)/$', views.change_password),
    url(r'^bbs_post_detail/(\d+)/$', views.bbs_post_detail, name='postDetail'),
    url(r'changeimage/(.+)/$', views.change_image),
    url(r'^follow_deal/$', views.follow_deal),
    url(r'^ajax_deal/$', views.ajax_deal),
    url(r'^ajax_append_image/$', views.ajax_append_image),
    url(r'^ajax_append_files/$', views.ajax_append_files),
    url(r'^search/post/(\w+)/$', views.search_postbycontent),
    url(r'^search/user/(\w+)/$', views.search_userbyusername),
]

