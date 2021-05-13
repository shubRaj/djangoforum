from askbuddie.models import (
    CATEGORY_CHOICES,
    COLOR_CATEGORY,
    BaseTag,
    BaseConfig,
    BasePage,
    SocialMedia,
    )
category_choices = [(COLOR_CATEGORY.get(category[0]),category[1]) for category in CATEGORY_CHOICES]
def config(request):
    context = {
        "socials":SocialMedia.objects.all(),
        "tags":BaseTag.objects.all(),
        "config":BaseConfig.objects.first(),
        "pages":BasePage.objects.all(),
        "category_choices":category_choices,
        
    }
    return context