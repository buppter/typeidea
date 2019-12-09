from django.views.generic import ListView

from blog.views import CommonViewMixin
from .models import Link, Status


class LinkView(CommonViewMixin, ListView):
    queryset = Link.objects.filter(status=Status.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = "link_list"

