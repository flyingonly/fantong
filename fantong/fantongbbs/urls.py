from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.bbs_list, name='index'),
    url(r'^personal/', views.get_user),
    url(r'changepassword/(.+)/$', views.change_password),
]
