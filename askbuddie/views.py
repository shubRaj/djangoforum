from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.conf import settings
from django.contrib.messages.views import SuccessMessageMixin
from .forms import (
    UserRegistrationForm,
    verifyRecaptcha,
    ForumThreadForm,
    ThreadReplyForm,
    SupportForm,
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView
)
from django.views.generic import (
    ListView,
    DetailView,
    View,
    CreateView,
    FormView
)
from askbuddie.models import (
    ForumThread,
    BasePage,
    ThreadTag,
)
from django.db.models import (
    Sum,
    Count
)
from django.urls import (
    reverse_lazy,
    reverse
)
from django.contrib.auth.mixins import (
    UserPassesTestMixin,
    LoginRequiredMixin,
)

from django.http import (
    HttpResponseNotModified,
    HttpResponseRedirect,
)
import asyncio,random
from urllib.parse import unquote_plus
from django.http import HttpResponse
class IndexThread(ListView):
    model = ForumThread
    template_name = "askbuddie/home.html"
    context_object_name = "threads"
    paginate_by = 20
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = "Latest"
        return context
    def get_queryset(self):
        return self.model.objects.all().select_related("created_by")
    
class DetailThread(DetailView):
    model = ForumThread
    template_name = "askbuddie/detail.html"
    context_object_name = "thread"
    def post(self,request,*args,**kwargs):
        reply = ThreadReplyForm(request.POST,request.FILES) 
        if reply.is_valid():
            reply = reply.save(commit=False)
            reply.created_by = request.user
            reply.forumThread = self.get_object()
            reply.save()
        return super().get(request,*args,**kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views +=1
        self.object.save(update_fields=["views",])
        context["form"] = ThreadReplyForm()
        context["thread_likes"]=self.object.thread_reply.aggregate(upvotes=Sum("upvotes")).get("upvotes")
        context["thread_users"] = self.object.thread_reply.aggregate(users=Count("created_by")).get("users")
        return context
class SearchForumView(ListView):
    model = ForumThread
    template_name = "askbuddie/home.html"
    context_object_name = "threads"
    paginate_by = 20
    def get(self,request,*args,**kwargs):
        if not request.GET.get("thread"):
            return HttpResponseNotModified()
        return super().get(request,*args,**kwargs)
    def get_queryset(self):
        query = self.request.GET.get("thread")
        threads = ForumThread.objects.filter(topic__icontains=query)|ForumThread.objects.filter(withTag__tag__icontains=query)
        return threads
class CategoryForumView(ListView):
    model = ForumThread
    template_name = "askbuddie/home.html"
    context_object_name = "threads"
    paginate_by = 20
    def get_queryset(self):
        threads = self.model.objects.filter(category__icontains=self.kwargs.get("category"))
        return threads
class TagForumView(CategoryForumView):
    def get_queryset(self):
        threads = self.model.objects.filter(withTag__tag__icontains=unquote_plus(self.kwargs.get("tag")))
        return threads
class MostLikedView(CategoryForumView):
    def get_queryset(self):
        threads = self.model.objects.annotate(upvotes=Sum("withThreadReply__upvotes")).order_by("-upvotes")
        return threads
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = "Most Liked"
        return context
class UnreadView(CategoryForumView):
    def get_queryset(self):
        threads = self.model.objects.filter(views=0)
        return threads
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = "Unread"
        return context
class MyLoginView(UserPassesTestMixin,SuccessMessageMixin,LoginView):
    template_name = "askbuddie/login.html"
    success_login_messages=["Welcome back! %s .This place hasn't been the same without you",
    "So Glad You're Back,%s","Welcome back! %s .There will be forcefull resistance if you ever try to leave again",]
    def get_success_url(self):
        return reverse("app_askbuddie:askbuddie_home")
    def get_success_message(self,cleaned_data):
        self.success_message = random.choice(self.success_login_messages)% self.request.user.first_name
        return super().get_success_message(cleaned_data)
    def form_valid(self,form):
        recaptcha_token = self.request.POST.get("g-recaptcha-response")
        if asyncio.run(verifyRecaptcha(recaptcha_token)):
            return super().form_valid(form)
        form.add_error(None,"Human Verification Failed.Try Again")
        return super().form_invalid(form)
    def test_func(self):
        return self.request.user.is_anonymous
    def handle_no_permission(self):
        return HttpResponseRedirect(reverse("app_askbuddie:askbuddie_home"))
class MyLogoutView(LoginRequiredMixin,LogoutView):
    pass
class SinglePage(DetailView):
    model = BasePage
    template_name = "askbuddie/singlepage.html"
    context_object_name = "page"

class ForgotPassword(View):
    template_name = "askbuddie/forgot.html"
    def get(self,request):
        return render(request,self.template_name)
class SignupView(UserPassesTestMixin,SuccessMessageMixin,CreateView):
    form_class = UserRegistrationForm
    template_name = "askbuddie/signup.html"
    success_message = "Welcome Nerds"
    def get_success_url(self):
        return reverse("app_askbuddie:askbuddie_login")
    def get_success_message(self,cleaned_data):
        self.success_message = "You're Welcome! Nerd"
        return super().get_success_message(cleaned_data)
    def form_valid(self,form):
        recaptcha_token = self.request.POST.get("g-recaptcha-response")
        if asyncio.run(verifyRecaptcha(recaptcha_token)):
            form_response = super().form_valid(form)
            user = authenticate(username = form.cleaned_data.get("username"),password=form.cleaned_data.get("password1"))
            if self.request.POST.get("send_newsletter"):
                user.user_profile.send_newsletter=True
                user.user_profile.save()
            login(self.request,user)
            return form_response
        form.add_error(None,"Human Verification Failed.Try Again")
        return super().form_invalid(form)
    def test_func(self):
        return self.request.user.is_anonymous
    def handle_no_permission(self):
        return redirect("app_askbuddie:askbuddie_home")
class CreateTopic(LoginRequiredMixin,CreateView):
    form_class = ForumThreadForm
    template_name = "askbuddie/create-topic.html"
    def form_valid(self,form):
        form.instance.created_by = self.request.user
        formResponse = super().form_valid(form)
        tags = form.cleaned_data.get("tags","").split(",")
        # tags.remove("")
        #use if tag to check if the tag is empty string or not
        for tag in tags:
            if tag and form.instance.forum_tag.count()<7:
                threadtag,created=ThreadTag.objects.get_or_create(tag=tag)
                threadtag.forumThread.add(form.instance)
        if not settings.DEBUG:
            fb_post_id = settings.FB.post(form.instance.topic,link=f"{self.request.get_host()}{form.instance.get_absolute_url()}")
            form.instance.fb_post_id = fb_post_id
            form.instance.save()
        return formResponse
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["threads"] = random.choices(ForumThread.objects.all(),k=10)
        return context
    
class SupportView(SuccessMessageMixin,CreateView):
    form_class = SupportForm
    template_name = "askbuddie/support.html"
    success_message = "Submitted Successfully"
    def form_valid(self,form):
        recaptcha_token = self.request.POST.get("g-recaptcha-response")
        if asyncio.run(verifyRecaptcha(recaptcha_token)):
            if self.request.user.is_authenticated:
                form.instance.user = self.request.user
                form.instance.email = self.request.user.email
            else:
                if not form.cleaned_data.get("email"):
                    form.add_error("email","Please provide an email")
                    return super().form_invalid(form)
            return super().form_valid(form)
        form.add_error(None,"Human Verification Failed.Try Again")
        return super().form_invalid(form)