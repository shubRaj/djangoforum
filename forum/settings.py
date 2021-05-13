"""
Django settings for forum project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os,socket,aiohttp,asyncio,facebook
import secrets
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secrets.token_hex(25)

# SECURITY WARNING: don't run with debug turned on in production!
is_production = socket.gethostname().endswith("com")

if is_production:
    DEBUG = False
    SECURE_SSL_REDIRECT = True
else:
    DEBUG = True

ALLOWED_HOSTS = ["localhost","ask.shubraj.com","127.0.0.1"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'askbuddie.apps.AskbuddieConfig',
    'django_user_agents',
    'django_summernote',
    'django.contrib.sitemaps',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'askbuddie.custom_middleware.UserLastOnlineMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
    
]

ROOT_URLCONF = 'forum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates",],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'askbuddie.processors.config',
            ],
            'builtins':[
                "askbuddie.templatetags.custom_filters",
            ],
        },
    },
]

WSGI_APPLICATION = 'forum.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
AUTHENTICATION_BACKENDS = ["askbuddie.models.EmailBackend"]
FILE_UPLOAD_HANDLERS= [
    'django.core.files.uploadhandler.MemoryFileUploadHandler',
    'django.core.files.uploadhandler.TemporaryFileUploadHandler',
]
FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
"""YOUR RECAPTCHA KEY FOR CAPTCHA BACKEND VERIFICATION"""
RECAPTCHA_SECRET_KEY = "6LeqhmIaAAAAAKT6x2y5l5lFYDviacE6WS3sN5-z"
STATICFILES_DIRS = [
        BASE_DIR/"staticfiles",
    ]
if DEBUG:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "test",
        "HOST":"db",
        "USER":"test",
        "PASSWORD":"test123",
    },}
    #static & media
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR/"assets"
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR/"media"
   
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }
    USER_AGENTS_CACHE = 'default'
    MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    DATABASES = {
    "default":{
        'ENGINE':'django.db.backends.mysql',
        'NAME': 'YOUR DB NAME' ,
        "HOST": 'localhost',
        "USER": 'YOUR DB USERNAME',
        "PASSWORD": 'YOUR DB PASSWORD',
        'OPTION': {'init_command':"SET sql_mode='STRICT_TRANS_TABLE',"},
    },}

    #static & media
    #know it is bad practice but have no option because of the css url
    STATIC_URL = "YOUR STATIC URL"
    STATIC_ROOT = BASE_DIR/"assets"
    MEDIA_URL = "YOUR MEDIA URL"
    MEDIA_ROOT = 'YOUR MEDIA ROOT'
    #FaceBook GraphAPI
    #FOR AUTOMATIC POST ON FACEBOOK POST
    USER_ACCESS_TOKEN = ""
    PAGE_ID = ""
    async def get_page_access_token(user_access_token,page_id):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://graph.facebook.com/v3.0/me?access_token={user_access_token}") as response:
                if response.status == 200:
                    response_json = await response.json()
                    user_id = response_json.get("id")
            if user_id:
                async with session.get(f"https://graph.facebook.com/v3.0/{user_id}/accounts?access_token={user_access_token}") as response:
                    if response.status == 200:
                        response_json = await response.json()
                        for page in response_json.get("data"):
                            if page.get("id") == page_id:
                                page_access_token = page.get("access_token")
                                return page_access_token
            return None
    class PostMyArticle:
        def __init__(self,user_access_token,page_id):
            self.page_id = page_id
            self.page_access_token = asyncio.run(get_page_access_token(user_access_token,page_id))
            self.graphql = facebook.GraphAPI(access_token=self.page_access_token,version="3.0")
        def post(self,message,**kwargs):
            return self.graphql.put_object(parent_object=self.page_id,connection_name=kwargs.get("type","feed"),message=message,link=kwargs.get("link","")).get("id")
        def delete(self,page_post_id):
            self.graphql.delete_object(id=page_post_id)
    FB = PostMyArticle(USER_ACCESS_TOKEN,PAGE_ID)
CKEDITOR_UPLOAD_PATH = "uploads/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
LOGIN_URL = "app_askbuddie:askbuddie_login"

#summernote
X_FRAME_OPTIONS = 'SAMEORIGIN'
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '480',

        # Toolbar customization
        # https://summernote.org/deep-dive/#custom-toolbar-popover
        'toolbar': [
            ['style', ['style','bold', 'italic', 'underline', 'clear']],
            ['font', ['strikethrough', 'superscript', 'subscript']],
            ['fontname', ['fontname']],
            ['color', ['color','forecolor','backcolor']],
            ['fontsize', ['fontsize']],
            ['para', ['ul', 'ol', 'paragraph',"hr"]],
            ['table', ['table']],
            ['insert', ['link','unlink','picture', 'video']],
            ['view', ['fullscreen','undo','redo']],
        ],
},
}