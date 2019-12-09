"""
author: buppter
datetime: 2019/12/9 15:59
"""
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed

from .models import Post


class ExtendedRssFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRssFeed, self).add_item_elements(handler, item)
        handler.addQuickElement("content:html", item['content_html'])


class LatestPostFeed(Feed):
    feed_type = Rss201rev2Feed
    title = 'Typeidea Blog System'
    link = '/rss/'
    description = "typeidea is a blog system based on Django"

    def items(self):
        return Post.objects.filter(status=Post.STATUS_NORMAL)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.desc

    def item_link(self, item):
        return reverse('post_detail', args=[item.pk])

    def item_extra_kwargs(self, item):
        return {"content_html": self.item_content_html(item)}

    @staticmethod
    def item_content_html(item):
        return item.content_html
