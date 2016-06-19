import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for pywebes project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$((3lau#qw29s82urpn#&#dj2bx11*oi22z2#@glw$@5#p5!h$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition





ROOT_URLCONF = 'pywebes.urls'




# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'pywebes', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'pywebes', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',

                'aldryn_boilerplates.context_processors.boilerplate',
                'cms_bs3_theme.context_processors.settings',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE_CLASSES = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    # Initial DjangoCMS dependencies
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',
    'pywebes',

    # Extra dependencies
    'cms_bs3_theme',
    'djangocms_highlightjs',
    'bootstrap3',
    'aldryn_bootstrap3',


    # Aldryn Newsblog dependencied
    'aldryn_apphooks_config',
    'aldryn_boilerplates',
    'aldryn_categories',
    'aldryn_common',
    'aldryn_newsblog',
    'aldryn_people',
    'aldryn_reversion',
    'aldryn_translation_tools',
    'easy_thumbnails',
    'filer',
    'parler',
    'sortedm2m',
    'taggit',


]

LANGUAGES = (
    ## Customize this
    ('es', gettext('es')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'code': 'es',
            'public': True,
            'hide_untranslated': False,
            'redirect_on_fallback': True,
            'name': gettext('es'),
        },
    ],
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
}


# CMS_TEMPLATES = (
#     ## Customize this
#     ('fullwidth.html', 'Fullwidth'),
#     ('sidebar_left.html', 'Sidebar Left'),
#     ('sidebar_right.html', 'Sidebar Right')
# )

CMS_TEMPLATES = (
    # ('cms_bs3_theme/page.html', 'BS3 Page'),
    ('cms_bs3_theme/fullwidth.html', 'BS3 Fullwidth'),
    ('cms_bs3_theme/sidebar_right.html', 'BS3 Sidebar Right'),
    ('cms_bs3_theme/sidebar_left.html', 'BS3 Sidebar Left'),
    ('cms_bs3_theme/feature.html', 'BS3 Feature'),
    ('cms_bs3_theme/landscape.html', 'BS3 Landscape'),
    ('pywebes/home.html', 'BS3 Home'),
    ('sidebar_right.html', 'NekTheme Sidebar right'),
)

ALDRYN_BOILERPLATE_NAME = 'bootstrap3'

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)


BOOTSTRAP3_THEME = 'pywebes'
BOOTSTRAP3_COLS = 12
BOOTSTRAP3_SIDEBAR_COLS = 4
BOOTSTRAP3_MENU_TEMPLATE = 'cms_bs3_theme/menus/fluid-static-top-default.html'

CMS_STYLE_NAMES = (
    ('info', gettext("info")),
    ('new', gettext("new")),
    ('hint', gettext("hint")),
    ('primary-background', gettext('Primary background')),
    ('secondary-background', gettext('Secondary background')),
    ('container', gettext('Container')),
)

ACCOUNT_ACTIVATION_DAYS = 7