from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommnerAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'create_time')
