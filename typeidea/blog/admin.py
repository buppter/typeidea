from abc import ABC

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', "create_time")
    fields = ('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(CategoryAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(TagAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


class CategoryOwnerFiler(admin.SimpleListFilter):
    """自定义过滤器只展示当前用户类"""
    title = "分类过滤器"
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'create_time', 'owner', 'operator']
    list_display_links = []

    list_filter = [CategoryOwnerFiler]
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = False

    # 编辑页面
    save_on_top = True

    exclude = ('owner',)
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )

    fieldsets = (
        ("基础配置", {
            "description": "基础配置描述",
            "fields": (
                ("title", "category"),
                "status",
            )
        }),
        ("内容", {
            "fields": (
                "desc",
                "content",
            )
        }),
        ("额外信息", {
            "classes": ("collapse",),
            "fields": ("tag",),
        })
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = "操作"

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    # 对 queryset 进行过滤
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)

    # 对外键下拉框进行过滤
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.filter(owner=request.user)
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # 对多选多字段进行过滤渲染
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "tag":
            kwargs["queryset"] = Tag.objects.filter(owner=request.user)
        return super(PostAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

    # class Media:
    #     css = {
    #         'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
    #     }
    #     js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)
