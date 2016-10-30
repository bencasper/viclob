# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from home.Fields import *
from django.db import models
from wagtail.wagtailsearch import index


class HomePage(Page):
    class Meta:
        verbose_name = u'首页'


# Contact page

class ContactPage(Page, ContactFields):
    body = RichTextField(verbose_name='简介', blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    class Meta:
        verbose_name = u'联系我们'


ContactPage.content_panels = [
    # FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
    MultiFieldPanel(ContactFields.panels, u"联系方式"),
]

ContactPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]
