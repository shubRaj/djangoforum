from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from askbuddie.models import ForumThread,ThreadReply,Support
from django.contrib.auth.forms import UserCreationForm
from django_summernote.widgets import SummernoteWidget
import asyncio
import aiohttp
from django.conf import settings
async def verifyRecaptcha(token):
    payload = {"secret":settings.RECAPTCHA_SECRET_KEY,"response":token}
    async with aiohttp.ClientSession() as session:
        async with session.post("https://www.google.com/recaptcha/api/siteverify",data=payload) as response:
            output = await response.json()
            return output.get("success")
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={"required":True,}))
    terms = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email",
        "password1","password2","terms",]
    def clean_terms(self):
        value = self.cleaned_data.get("terms")
        if not value:
            self.add_error("terms","Agree to terms & conditions to Sign Up.")
        return value
class ForumThreadForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={"required":False,}))
    class Meta:
        model = ForumThread
        exclude = ("created_by","slug","closed",'views',)
        widgets = {
            "description":SummernoteWidget(),
        }
class ThreadReplyForm(forms.ModelForm):
    class Meta:
        model = ThreadReply
        fields = ("description",)
        widgets = {
            "description":SummernoteWidget(),
        }
class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        exclude = ("user",)