from django.dispatch import receiver
from django.db.models.signals import post_save,pre_delete
from django.contrib.auth.models import User
from askbuddie.models import UserProfile,ForumThread
from django.conf import settings
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
@receiver(pre_delete,sender=ForumThread)
def delete_fb_post(sender,instance,**kwargs):
    if not settings.DEBUG and instance.fb_post_id:
        settings.FB.delete(instance.fb_post_id)