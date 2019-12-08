"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from base.custom_site import custom_site
from blog.views import PostDetailView, IndexView, TagView, CategoryView
from config.views import links

urlpatterns = [
    url(r'^super_admin/', admin.site.urls, name="super_admin"),
    url(r'^admin/', custom_site.urls, name="admin"),

    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name="post_detail"),
    url(r'^links/$', links, name="links"),
    url(r"^$", IndexView.as_view(), name="index"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag_list"),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name="category_list"),

    # function based view 时的各 URL 配置
    # url(r"^$", post_list, name="index"),
    # url(r'^post/(?P<post_id>\d+).html$', post_detail, name="post_detail"),
    # url(r'^tag/(?P<tag_id>\d+)/$', post_list, name="tag_list"),
    # url(r'^category/(?P<category_id>\d+)/$', post_list, name="category_list"),

]
