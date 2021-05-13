"""forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views
from django.contrib.sitemaps.views import sitemap
from askbuddie.sitemap import ForumThreadSitemap,PageSitemap,StaticSitemap
from askbuddie.models import BaseConfig
# admin.site.site_header = BaseConfig.objects.first().header
# admin.site.index_title = f"{admin.site.site_header} Admin Dashboard"
# admin.site.site_title = f"{admin.site.site_header} Admin"
# admin.AdminSite.login_template = 'askbuddie/login.html'
sitemaps = {
    "threads":ForumThreadSitemap,
    "pages":PageSitemap,
    "static":StaticSitemap,
}
urlpatterns = [
    path('logmein/', admin.site.urls),
    path("",include("askbuddie.urls",namespace="askbuddie")),
    path('editor/', include('django_summernote.urls')),
    path("map.xml",views.index,{"sitemaps":sitemaps},name="django.contrib.sitemaps.views.sitemap"),
    path('map-<section>.xml', views.sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
else:
    handler404 = "forum.handlers.page_not_found"
    handler500 = "forum.handlers.server_error"