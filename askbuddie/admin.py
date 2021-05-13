from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin 
from django.contrib.auth.models import User
from .models import (
    ForumThread,
    ThreadReply,
    BaseConfig,
    SocialMedia,
    BasePage,
    BaseTag,
    UserProfile,
    ThreadTag,
    Support,
    )
class AdminForumThread(SummernoteModelAdmin):
    fields = (
        "topic",
        "category",
        "description",
        'fb_post_id',
        "created_by",
        "views",
        "closed",
        "slug",
        )
    search_fields = (
        "topic",
        "category",
        "description",
        "created_by__username",
        "created_on",
        )
    list_display = (
        "topic",
        "category",
        'fb_post_id',
        "created_by",
        "created_on",
        "views",
        "closed",
        )
    summernote_fields = ("description",)
class AdminThreadReply(SummernoteModelAdmin):
    fields = (
        "forumThread",
        "description",
        "upvotes",
        "downvotes",
        "hearts",
        "created_by",
        )
    search_fields = (
        "forumThread__topic",
        "created_by__username",
        "created_on",
        )
    list_display = (
        "forumThread",
        "upvotes",
        "downvotes",
        "hearts",
        "created_by",
        "created_on",
        "hidden",
        )
class AdminBaseConfig(admin.ModelAdmin):
    list_display = (
        "title",
        "header",
        'analytics',
    )
class AdminBaseSocialMedia(admin.ModelAdmin):
    list_display = (
        "platform",
        "url",
        "css_class",
    )
class AdminBasePage(SummernoteModelAdmin):
    fields = (
        "baseConfig",
        "title",
        "description",
    )
    list_display = (
        "title",
    )
class AdminBaseProfile(admin.ModelAdmin):
    list_display = (
        "name",
    )
class UserProfileRule(admin.StackedInline):
    model = UserProfile
class AdminUserProfile(admin.ModelAdmin):
    inlines = [UserProfileRule,]
admin.site.register([BaseTag,ThreadTag,Support])
admin.site.unregister(User)
admin.site.register(User,AdminUserProfile)
admin.site.register(BasePage,AdminBasePage)
admin.site.register(SocialMedia,AdminBaseSocialMedia)
admin.site.register(BaseConfig,AdminBaseConfig)
admin.site.register(ForumThread,AdminForumThread)
admin.site.register(ThreadReply,AdminThreadReply)