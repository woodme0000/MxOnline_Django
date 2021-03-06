"""imooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
# from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve #处理静态文件

# from django.views.static import serve #处理静态文件
from imooc.settings import MEDIA_ROOT

import xadmin

# from users.views import user_login
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # 验证码
    url(r'^captcha/', include('captcha.urls')),

    #配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # TemplateView 只返回静态模板，不用在 views 里写逻辑
    # url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),

    # 基于函数 的 View 映射 URL 方法
    # url(r'^login/$', user_login, name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),

    # 验证用户注册后，在邮件里点击注册链接
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name='user_active'),

    # 注册页面
    url(r'^register/$', RegisterView.as_view(), name='register'),
    # 忘记密码
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),

    #用户在邮件里点击重置密码链接
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),

    # 重置密码表单 POST 请求
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),


    #课程机构相关 URL
    url(r'^org/', include('organization.urls', namespace='org')),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^__debug__/', include(debug_toolbar.urls)))