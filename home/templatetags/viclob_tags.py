# -*- coding: utf-8 -*-

from django import template
from django.conf import settings
from wagtail.wagtailcore.models import Page

from home.models import NavigationPage, HomePage, NewsIndexPage, ProviderIndexPage

register = template.Library()


# settings value
@register.assignment_tag
def get_google_maps_key():
    return getattr(settings, 'GOOGLE_MAPS_KEY', "")


@register.assignment_tag(takes_context=True)
def get_current_user(context):
    print context['request'].user
    return context['request'].user


@register.assignment_tag(takes_context=True)
def get_site_root(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


@register.assignment_tag(takes_context=True)
def get_home_page(context):
    # NB this returns a core.Page, not the implementation-specific model used
    # so object-comparison to self will return false as objects would differ
    return context['request'].site.root_page


def has_menu_children(page):
    return page.get_children().live().in_menu().exists()


@register.assignment_tag
def get_nav_items(homepage):
    navitems = []
    menuitems = homepage.get_children().live().in_menu()
    for menuitem in menuitems:
	print menuitem
        menuitem.show_dropdown = has_menu_children(menuitem)
        if menuitem.title == u'解决方案':
            menuitem.fa = 'fa-cloud'
            menuitem.icon = 'solution.png'
            menuitem.menu_priority = 10
            navitems.append(menuitem)
        elif menuitem.title == u'行业资讯':
            menuitem.fa = 'fa-paper-plane'
            menuitem.icon = 'news.png'
            menuitem.menu_priority = 9
            navitems.append(menuitem)
        elif menuitem.title == u'云服务商':
            menuitem.fa = 'fa-video-camera'
            navitems.append(menuitem)

    navitems.sort(key=lambda x: x.menu_priority, reverse=True)
    return navitems


@register.assignment_tag
def news_sub_navitems(calling_page=None):
    news_indexpage = NewsIndexPage.objects.first()
    navitems = news_indexpage.get_children().live().in_menu()
    for navitem in navitems:
        navitem.active = (calling_page.url.startswith(navitem.url) if calling_page else False)
        print calling_page.url
        print navitem.url
    print navitems
    return navitems


@register.assignment_tag
def provider_sub_navitems(calling_page=None):
    news_indexpage = ProviderIndexPage.objects.first()
    navitems = news_indexpage.get_children().live().in_menu()
    for navitem in navitems:
        navitem.active = (calling_page.url.startswith(navitem.url) if calling_page else False)
        print calling_page.url
        print navitem.url
    print navitems
    return navitems



# Retrieves the top menu items - the immediate children of the parent page
# The has_menu_children method is necessary because the bootstrap menu requires
# a dropdown class to be applied to a parent
@register.inclusion_tag('home/tags/top_menu.html', takes_context=True)
def top_menu(context, parent, calling_page=None):
    navitems = []
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.menu_priority = 0
        if menuitem.title == u'行业资讯':
            menuitem.menu_priority = 8
	    navitems.append(menuitem)
        elif menuitem.title == u'解决方案':
            menuitem.menu_priority = 10
	    navitems.append(menuitem)
        #elif menuitem.title == u'云服务商':
        #    menuitem.menu_priority = 8
        elif menuitem.title == u'合作案例':
            menuitem.menu_priority = 9
	    navitems.append(menuitem)
        elif menuitem.title == u'关于我们':
            menuitem.menu_priority = 0
	    navitems.append(menuitem)
        menuitem.show_dropdown = has_menu_children(menuitem)
        # We don't directly check if calling_page is None since the template
        # engine can pass an empty string to calling_page
        # if the variable passed as calling_page does not exist.
        menuitem.active = (calling_page.url.startswith(menuitem.url) if calling_page else False)

    navitems.sort(key=lambda x: x.menu_priority, reverse=True)
    return {
        'calling_page': calling_page,
        'menuitems': navitems,
        # required by the pageurl tag that we want to use within this template
        'request': context['request'],
    }


# Retrieves the children of the top menu items for the drop downs
@register.inclusion_tag('home/tags/top_menu_children.html', takes_context=True)
def top_menu_children(context, parent, calling_page=None):
    menuitems_children = parent.get_children()
    menuitems_children = menuitems_children.live().in_menu()
    for menuitem in menuitems_children:
        menuitem.active = (calling_page.url.startswith(menuitem.url) if calling_page else False)
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
