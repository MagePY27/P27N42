# Devops


## 第一章 环境准备

#### 安装pyenv并创建虚拟环境
    brew update
    brew install pyenv
    #安装python环境，根据自己需要安装对应版本
    pyenv install 3.6.10
    #安装 virtualenv 虚拟环境
    brew install pyenv-virtualenv
    #利用pyenv的虚拟环境，创建python虚拟环境
    pyenv virtualenv 3.6.10 devops-3610
    #进入项目目录后可指定项目使用的虚拟环境
    cd $projet && pyenv local devops-3610
  

2. #### Django初识

        #创建Django项目 版本2.2
        cd $projet && pip install Django==2.2.0
        django-admin startproject devops
         #查看目录层级
        tree ./devops
        ./
        ├── devops
        │   ├── __init__.py
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        └── manage.py
  
   
   

   ## 第二章 第一个Hello World Django


1. #### 数据库配置修改

   ```shell
   #修改访问权限，全部地址可以访问
   ALLOWED_HOSTS = ["*"] 
   #编辑settings.py 修改数据库信息
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',#使用的数据库
           'NAME': 'devops',#数据库名
           'HOST': '127.0.0.1',#数据库地址
           'POST': '3306',#数据库端口
           'USER': 'django',#数据库用户名
           'PASSWORD': '123456',#数据库密码
   
       }
   }
   #修改Django项目语言
   LANGUAGE_CODE = 'zh-hans'
   #修改Django项目时区
   TIME_ZONE = 'Asia/Shanghai'
   ```

2. #### 第一个helloword

   - 创建hello App

     ```shell
     #创建hello APP
     cd $projet && python manage,py startapp hello
     tree ./hello
     ├── hello
     │   ├── __init__.py
     │   ├── admin.py
     │   ├── apps.py
     │   ├── migrations
     │   │   ├── __init__.py
     │   │   └── __pycache__
     │   │       └── __init__.cpython-36.pyc
     │   ├── models.py
     │   ├── tests.py
     │   ├── urls.py
     │   └── views.py
     ```

   - 注册hello App

     ```shell
     #注册app
     vim $projet/devops/settings.py
     
     INSTALLED_APPS = [
         'django.contrib.admin',
         'django.contrib.auth',
         'django.contrib.contenttypes',
         'django.contrib.sessions',
         'django.contrib.messages',
         'django.contrib.staticfiles',
         'hello.apps.HelloConfig', #注册 hello APP
     ]
     ```

   

   - 创建主路由到app

     ```python
     vim $projet/devops/urls.py
     
     from django.contrib import admin
     from django.urls import path, include
     
     
     urlpatterns = [
         path('admin/', admin.site.urls),
         path('hello/', include('hello.urls')),#添加hello，路由到helloApp下的urls
     ]
     ```

   - 创建hello App路由规则

     ```python
     vim $projet/devops/hello/urls.py
     
     from django.urls import path
     
     from . import views
     
     urlpatterns = {
        # path('hello/', views.index, name='index'),#访问模式ip/hello/hello多子路由
       	path('', views.index, name='index') #访问模式ip/hello 子路由直接访问
     }
     
  ```
   
- 创建视图views 方法
   
     ```python
     vim $projet/devops/hello/views.py
     
     from django.shortcuts import render
     from django.http import HttpResponse
     
     def index(request):
         return HttpResponse("<p>Hello World Django!!!</p>")#访问hello接口返回字符串
  ```
   
- 启动并测试访问
   
     ```shell
     cd $projet/ && python manage.py runserver 0.0.0.0:8080
     #启动项目后浏览器访问本地ip接口
  ```
