from __future__ import absolute_import, unicode_literals

import registration
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from formdemo import views as form_views
from django.contrib.auth import views as auth_views

from login.models import RegistrationForm
from login.views import RegistrationView
from search import views as search_views

urlpatterns = [

    # url(r'^$', django.contrib.auth.views.login),

    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    url(r'^captcha/', include('captcha.urls')),

    url(r'^comments/', include('django_comments.urls')),

    url(r'^testform/demo/$', form_views.demo, name='form'),
    url(r'^testform/thanks/$', form_views.thanks, name='form'),


    # url(r'^accounts/login/$', auth_views.login, {'template_name': 'login/login.html'}, name='login'),
    # url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'login/logged_out.html'}, name='logout'),
    url(r'^viclob/register/$', RegistrationView.as_view(form_class=RegistrationForm), name='viclob'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    # should put wagtail_urls last
    url(r'', include(wagtail_urls)),

]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
