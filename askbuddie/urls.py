from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf import settings
app_name = "app_askbuddie"
urlpatterns = [
    path("thread/<slug:slug>/",views.DetailThread.as_view(),name="askbuddie_thread"),
    path("search/",views.SearchForumView.as_view(),name="askbuddie_search"),
    path("create-topic/",views.CreateTopic.as_view(),name="askbuddie_create"),
    path("mostliked/",views.MostLikedView.as_view(),name="askbuddie_mostliked"),
    path("unread/",views.UnreadView.as_view(),name="askbuddie_unread"),
    path("signup/",views.SignupView.as_view(),name="askbuddie_signup"),
    path("login/",views.MyLoginView.as_view(),name="askbuddie_login"),
    path("logout/",views.MyLogoutView.as_view(),name="askbuddie_logout"),
    path("support/",views.SupportView.as_view(),name="askbuddie_support"),
    path("forgot-password/",views.ForgotPassword.as_view(),name="askbuddie_forgot"),
    path("tag/<str:tag>/",views.TagForumView.as_view(),name="askbuddie_tag"),
    path("category/<str:category>/",views.CategoryForumView.as_view(),name="askbuddie_category"),
    path("<slug:slug>/",views.SinglePage.as_view(),name="askbuddie_page"),
    path("",views.IndexThread.as_view(),name="askbuddie_home"),
]