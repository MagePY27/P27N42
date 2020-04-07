"""devops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path,re_path
from . import views,views1
from . import views2
import re
app_name='hello'
#普通参数
urlpatterns = [
    path('', views.index, name='index'),
    path('list/',views.list,name='list'),
    path('userlist1/',views.userlist,name='userlist1'),
#位置传参
# urlpatterns = [
#     re_path('([0-9]{4})/([0-9]{2})/', views.index, name='index'),
# ]

# #关键字传参
# urlpatterns = [
#      re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index, name='index'),
#  ]
    #简易用户管理系统
path('useradd/',views1.useradd,name='useradd'),
path('userlist/',views1.userlist,name='userlist'),
re_path('usermod/(?P<pk>[0-9]+)?/',views1.usermod,name='usermod'),
re_path('userdel/(?P<pk>[0-9]+)?/',views1.userdel,name='userdel'),

    #CBV 实现增删改查
#path('index/',views2.index, name='index1')
    #view
path('index/',views2.IndexView.as_view()),
path('user/temp/',views2.Tempview.as_view(),name="Tempview"),
path('user/userlist/',views2.UserListView.as_view(),name="listview"),
path('user/useradd/',views2.UserCreateView.as_view(),name="createview"),
re_path('user/detail/(?P<pk>[0-9]+)?/',views2.UserDetailView.as_view(),name="detailview"),
re_path('user/usermod/(?P<pk>[0-9]+)?/',views2.UserUpateView.as_view(),name="updateview"),
re_path('user/userdel/(?P<pk>[0-9]+)?/',views2.UserDelView.as_view(),name="delview"),
]
