from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
class BaseConfig(models.Model):
    title = models.CharField(max_length=30,help_text="Only One Instance Is Allowed")
    logo = models.ImageField(upload_to="logo",null=True,blank=True)
    favicon = models.ImageField(upload_to="favicon",null=True,blank=True)
    header = models.CharField(max_length=15)
    author = models.OneToOneField(User,on_delete=models.CASCADE,related_name="base_author",default=1)
    analytics = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    def save(self,*args,**kwargs):
        self.id=1
        return super().save(*args,**kwargs)
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = "BaseConfig"
class SocialMedia(models.Model):
    baseConfig = models.ForeignKey(BaseConfig,on_delete=models.CASCADE,related_name="base_social")
    platform = models.CharField(max_length=12,help_text="Example: Facebook,Instagram",unique=True)
    url = models.URLField(max_length=283,help_text="Example: https://www.facebook.com/Shuvraj.lama7")
    css_class = models.CharField(max_length=30,null=True,blank=True,help_text="FontAwesome. Example: facebook-square")
    def __str__(self)-> str:
        return self.platform
    class Meta:
        verbose_name_plural = "SocialMedias"
class BasePage(models.Model):
    baseConfig = models.ForeignKey(BaseConfig,on_delete=models.CASCADE,related_name="base_page")
    title = models.CharField(max_length=20,unique=True)
    description = models.TextField(blank=True,null=True)
    slug = models.SlugField(null=True,blank=True)
    class Meta:
        verbose_name_plural = "BasePages"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("app_askbuddie:askbuddie_page", kwargs={"slug": self.slug})
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args,**kwargs)
class BaseTag(models.Model):
    baseConfig = models.ForeignKey(BaseConfig,on_delete=models.CASCADE,related_name="base_tag")
    name = models.CharField(max_length=20)
    class Meta:
        verbose_name_plural = "BaseTags"
    def __str__(self):
        return self.name