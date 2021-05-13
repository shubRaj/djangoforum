from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    profile = models.ImageField(upload_to="profile",null=True,default="profile/default.png")
    send_newsletter = models.BooleanField(default=False)
    socialHandle = models.URLField(max_length=283,null=True,blank=True)
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(Q(username=username)|Q(email=username))
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None