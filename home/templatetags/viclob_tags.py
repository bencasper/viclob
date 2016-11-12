# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from wagtail.wagtailcore.models import Page

from home.models import TechNewsIndexPage, NavigationPage, NewsIndexPage, NewsContentPage, ServiceIndexPage

register = template.Library()


# settings value
@register.assignment_tag
def get_google_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")


@register.assignment_tag
def get_news_types():
    news_types = NewsIndexPage.objects.all()[0].get_children()
    for news_type in news_types:
        if news_type.title == u'技术':
            news_type.fa = 'fa-list'
        elif news_type.title == u'服务商':
            news_type.fa = 'fa-cloud'
        elif news_type.title == u'行业':
            news_type.fa = 'fa-film'
        elif news_type.title == u'应用':
            news_type.fa = 'fa-video-camera'
        elif news_type.title == u'从业者':
            news_type.fa = 'fa-user'

    return news_types

@register.assignment_tag
def get_service_types():
    service_types = ServiceIndexPage.objects.all()[0].get_children()

    for service_type in service_types:
        if service_type.title == u'统一测试平台':
            service_type.fa = 'fa-try'
        elif service_type.title == u'拍摄制作':
            service_type.fa = 'fa-film'

    return service_types



@register.assignment_tag
def get_vod_news():
    return NewsContentPage.objects.filter(techType=u'点播')


@register.assignment_tag
def get_tech_news():
    return NewsContentPage.objects.filter(techType=u'直播')


@register.assignment_tag
def get_player_news():
    return NewsContentPage.objects.filter(techType=u'播放器')


@register.assignment_tag
def get_cdn_news():
    return NewsContentPage.objects.filter(techType=u'CDN')


@register.assignment_tag
def get_code_news():
    return NewsContentPage.objects.filter(techType=u'编解码')


@register.assignment_tag
def get_store_news():
    return NewsContentPage.objects.filter(techType=u'存储')


@register.assignment_tag
def get_md5_news():
    return NewsContentPage.objects.filter(techType=u'加密')


@register.assignment_tag
def get_security_news():
    return NewsContentPage.objects.filter(techType=u'安全')


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page.get_children()[0]


@register.assignment_tag(takes_context=True)
def get_home_page(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


@register.assignment_tag(takes_context=True)
def get_nav_page():
    return Page.objects.get(title="")


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('home/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        if menuitem.title == u'导航':
            menuitem.fa = 'fa-paper-plane'
        if menuitem.title == u'资讯':
            menuitem.fa = 'fa-newspaper-o'
        elif menuitem.title == u'服务':
            menuitem.fa = 'fa-video-camera'
        elif menuitem.title == u'联系我们':
            menuitem.fa = 'fa-phone'
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url)
                           if calling_page else False)
    return {
        'calling_page': calling_page,
        'menuitems': menuitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.assignment_tag
def get_top_menu():
    menuitems = NavigationPage.objects.all().first().get_children().live().in_menu()
    for menuitem in menuitems:
        if menuitem.title == u'导航':
            menuitem.fa = 'fa-paper-plane'
        if menuitem.title == u'资讯':
            menuitem.fa = 'fa-newspaper-o'
        elif menuitem.title == u'服务':
            menuitem.fa = 'fa-video-camera'
        elif menuitem.title == u'联系我们':
            menuitem.fa = 'fa-phone'
        menuitem.show_dropdown = has_menu_children(menuitem)
    return menuitems


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('home/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    return {
        'parent': parent,
        'menuitems_children': menuitems_children,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


@register.inclusion_tag('home/tags/breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    self = context.get('self')
    if self is None or self.depth <= 2:
        # When on the home page, displaying breadcrumbs is irrelevant.
        ancestors = ()
    else:
        ancestors = Page.objects.ancestor_of(
            self, inclusive=True).filter(depth__gt=2)
    return {
        'ancestors': ancestors,
        'request': context['request'],
    }
