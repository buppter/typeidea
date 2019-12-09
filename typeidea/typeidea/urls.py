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
import debug_toolbar
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views

from base.custom_site import custom_site
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap
from blog.views import PostDetailView, IndexView, TagView, CategoryView, SearchView, AuthorView
from comment.views import CommentView
from config.views import LinkView
from typeidea.settings import dev

urlpatterns = [
    url(r'^super_admin/', admin.site.urls, name="super_admin"),
    url(r'^admin/', custom_site.urls, name="admin"),

    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name="post_detail"),
    url(r'^links/$', LinkView.as_view(), name="links"),
    url(r"^$", IndexView.as_view(), name="index"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag_list"),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name="category_list"),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name="author"),
    url(r'^comment/$', CommentView.as_view(), name="comment"),
    url(r'^rss|feed/', LatestPostFeed(), name="rss"),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {"posts": PostSitemap}}),

    # function based view 时的各 URL 配置
    # url(r"^$", post_list, name="index"),
    # url(r'^post/(?P<post_id>\d+).html$', post_detail, name="post_detail"),
    # url(r'^tag/(?P<tag_id>\d+)/$', post_list, name="tag_list"),
    # url(r'^category/(?P<category_id>\d+)/$', post_list, name="category_list"),
    # url(r'^links/$', links, name="links"),

]
if dev.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      # path('__debug__/', include(debug_toolbar.urls)),

                      # For django versions before 2.0:
                      url(r'^__debug__/', include(debug_toolbar.urls)),

                  ] + urlpatterns
