from django import template
from django.utils import timezone
from askbuddie.models import COLOR_CATEGORY
import random
register = template.Library()
# COLOR_CATEGORY = {
#     "Arts":"bg-f9bc64",
#     "Education":"bg-525252",
#     "Entertainment":"bg-36b7d7",
#     "Gaming":"bg-4f80b0",
#     "Hobbies":"bg-83253f",
#     "Pets":"bg-c6b38e",
#     "Photography":"bg-f26522",
#     "Politics":"bg-777da7",
#     "Random":"bg-5dd39e",
#     "Science":"bg-c49bbb",
#     "Social":"bg-348aa7",
#     "Tech":"bg-bce784",
#     "Travel":"bg-92278f",
#     "Video":"bg-4436f8",
#     "Nature":"bg-3ebafa"
# }
@register.filter
def div(numTo:int,numBy:int):
    result = round(int(numTo)/int(numBy),1)
    return result
@register.filter
def replace(value,args):
    replace,replace_to = args.split(",")
    return value.replace(replace,replace_to)
@register.filter
def split(value,sep):

    return value.split(sep)
@register.filter
def color(value):
    color = COLOR_CATEGORY.get(value.strip().lower())
    return color
@register.filter
def thread_reply_timesince(value):
    if not value:
        return None
    time_now = timezone.now()
    difference_time = time_now-value
    total_seconds = difference_time.total_seconds()
    days = round(total_seconds//86400)
    if not days:
        hours = round((total_seconds-days*86400)/(3600))
        if not hours:
            minutes = round((total_seconds-(days*86400+hours*3600))/60)
    if days:
        value=f"{days} days ago"
    elif hours:
        value=f"{hours} hours ago"
    else:
        value = f"{minutes} mins ago"
    return value
@register.filter
def user_last_online_timesince(value):
    time_now = timezone.now()
    difference_time = time_now-value
    total_seconds = difference_time.total_seconds()
    days = round(total_seconds//86400)
    if not days:
        hours = round((total_seconds-days*86400)/(3600))
        if not hours:
            minutes = round((total_seconds-(days*86400+hours*3600))/60)
    if days:
        value=f"{days} days ago"
    elif hours:
        value=f"{hours} hours ago"
    else:
        if minutes>5:
            value = f"{minutes} mins ago"
        else:
            value = "Online"
    return value
color_choices =[
    "bg-f9bc64",
    "bg-525252",
    "bg-36b7d7",
    "bg-4e80b0",
    "bg-83253f",
    "bg-c6b38e",
    "bg-f26522",
    "bg-777da7",
    "bg-5dd39e",
    "bg-c49bbb",
    "bg-348aa7",
    "bg-bce784",
    "bg-92278f",
    "bg-4436f8",
    "bg-3ebafa",
    "bg-877da7",
]
@register.filter
def random_color_generator(value):
    color = random.choice(color_choices)
    return color
@register.filter
def activity(value):
    latest = value.thread_reply.order_by("-created_on").first()
    if latest:
        total_seconds = (latest.created_on - value.created_on).total_seconds()
        days = round(total_seconds//86400)
        if not days:
            hours = round((total_seconds-days*86400)/(3600))
            if not hours:
                minutes = round((total_seconds-(days*86400+hours*3600))/60)
        if days:
            activity=f"{days}d"
        elif hours:
            activity=f"{hours}h"
        else:
            activity = f"{minutes}m"
    else:
        activity = "0m"
    return activity