from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.bbs_list, name='index'),
    url(r'^personal/', views.get_user),
    url(r'^accounts/profile/$', views.update_time),
    url(r'changepassword/(.+)/$', views.change_password),
    url(r'^bbs_post_detail/(\d+)/$', views.bbs_post_detail, name='bbs_post_detail')
]
