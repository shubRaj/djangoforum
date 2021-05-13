from django.contrib.sitemaps import Sitemap
from askbuddie.models import ForumThread,BasePage
from django.urls import reverse
class ForumThreadSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = "https"
    limit = 1000
    def items(self):
        return ForumThread.objects.all()

    def lastmod(self, obj):
        return obj.created_on
class PageSitemap(Sitemap):
    priority = 0.5
    changefreq="monthly"
    protocol = "https"
    def items(self):
        return BasePage.objects.all()
class StaticSitemap(Sitemap):
    priority = 0.5
    changefreq="monthly"
    protocol = "https"
    def items(self):
        return ["app_askbuddie:askbuddie_login","app_askbuddie:askbuddie_signup","app_askbuddie:askbuddie_forgot","app_askbuddie:askbuddie_support"]
    def location(self,item):
        return reverse(item)