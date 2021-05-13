from django.db import models
from multiselectfield import MultiSelectField
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.text import slugify
import random
from django.urls import reverse
# from django.conf import settings
CATEGORY_CHOICES= (
    ('arts','Arts'),
    ('education','Education'),
    ('entertainment','Entertainment'),
    ('gaming','Gaming'),
    ('hobbies','Hobbies'),
    ("maths","Maths"),
    ('pets','Pets'),
    ('photography','Photography'),
    ('programming',"Programming"),
    ('politics','Politics'),
    ('random','Random'),
    ('science','Science'),
    ('social','Social'), 
    ('tech','Tech'), 
    ('travel','Travel'), 
    ('video','Video'),
    ("nature","Nature"),)
COLOR_CATEGORY = {
    "arts":"bg-f9bc64",
    "education":"bg-525252",
    "entertainment":"bg-36b7d7",
    "gaming":"bg-8781bd",
    "hobbies":"bg-83253f",
    "pets":"bg-c6b38e",
    "photography":"bg-f26522",
    "politics":"bg-777da7",
    "random":"bg-5dd39e",
    "science":"bg-c49bbb",
    "social":"bg-348aa7",
    "tech":"bg-bce784",
    "travel":"bg-92278f",
    "video":"bg-4436f8",
    "nature":"bg-3ebafa",
    'maths':'bg-218380',
    'programming':'bg-00bd9d',
}
class BaseModel(models.Model):
    description = models.TextField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,editable=False)
    class Meta:
        abstract=True
class ForumThread(BaseModel):
    topic = models.CharField(max_length=512,unique=True)
    category = MultiSelectField(choices=CATEGORY_CHOICES,max_length=34,max_choices=3,null=True)
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="user_thread")
    fb_post_id = models.CharField(max_length=35,null=True,blank=True)
    slug = models.SlugField(blank=True,null=True,max_length=512)
    closed = models.BooleanField(default=False)
    views = models.IntegerField(default=0)
    def save(self,*args,**kwargs):
        if self.topic and not self.slug:
            self.slug = slugify(self.topic)
        save_status = super().save(*args,**kwargs)
        # settings.FB.post(f"{self.topic}\n https://{settings.ALLOWED_HOSTS[-1]}{self.get_absolute_url()}")
        return save_status
    def __str__(self) -> str:
        return self.topic
    def __repr__(self) -> str:
        return self.__str__()
    class Meta:
        ordering = ["-created_on",]
        verbose_name_plural = "ForumThreads"
    def get_absolute_url(self):
        return reverse("app_askbuddie:askbuddie_thread", kwargs={"slug": self.slug})
    
class ThreadReply(BaseModel):
    forumThread = models.ForeignKey(ForumThread,on_delete=models.CASCADE,related_name="thread_reply",related_query_name="withThreadReply")
    upvotes,downvotes,hearts= [models.IntegerField(default=0) for _ in range(3)]
    created_by = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="user_reply")
    hidden = models.BooleanField(default=False)
    class Meta:
        ordering = (
            "-upvotes",
            "-hearts",
            "-created_on",
            )
        verbose_name_plural = "ThreadReplies"
class ThreadTag(models.Model):
    forumThread = models.ManyToManyField(ForumThread,related_name="forum_tag",related_query_name="withTag")
    tag = models.CharField(max_length=70,unique=True)
    def __str__(self):
        return self.tag
    class Meta:
        verbose_name_plural = "Tags"
    def save(self,*args,**kwargs):
        return super().save(*args,**kwargs)
class Support(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_support",null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    regarding = models.CharField(max_length=512)
    description = models.TextField()
    def __str__(self):
        return self.regarding
    def get_absolute_url(self):
        return reverse("app_askbuddie:askbuddie_support")
    