# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.tests.testapp.models import LinkFields
from wagtail.wagtailcore.fields import RichTextField

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from home.Fields import *
from django.db import models
from wagtail.wagtailsearch import index

# A couple of static contants

TECHES = ((1, u'基础'), (2, u'直播'), (3, u'点播'))


class HomePage(Page):
    class Meta:
        verbose_name = u'首页'


HomePage.content_pannels = [
    MultiFieldPanel(SubjectItem.panels, u'咨询'),
    MultiFieldPanel(SubjectItem.panels, u'服务'),
    MultiFieldPanel(SubjectItem.panels, u'全网发型平台'),
    MultiFieldPanel(SubjectItem.panels, u'案例')

]


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.HomePage', related_name='carousel_items')


class HomePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.HomePage', related_name='related_links')


# Content page

class ContentPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.ContentPage', related_name='carousel_items')


class ContentPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.ContentPage', related_name='related_links')


class ContentPage(Page):
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]


ContentPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel('carousel_items', label="Carousel items"),
    FieldPanel('body', classname="full"),
    InlinePanel('related_links', label="Related links"),
]

ContentPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


class TechIntroPage(ContentPage):
    pass


class ProviderIntroPage(ContentPage):
    pass


class PracticeIntroPage(ContentPage):
    pass


class NewsIndexPage(Page):
    class Meta:
        verbose_name = u'咨询首页'

    pass


class FilmServiceIntroPage(ContentPage):
    class Meta:
        verbose_name = u'拍摄制作'


class DiyServiceIntroPage(ContentPage):
    class Meta:
        verbose_name = u'产品定制'


class PublishServiceIntroPage(ContentPage):
    class Meta:
        verbose_name = u'全网发行'


class ServiceIndexPage(Page):
    class Meta:
        verbose_name = u'服务首页'

    pass


class CaseIndexPage(ContentPage):
    class Meta:
        verbose_name = u'案例展示'


class VideoPlayPage(Page):
    class Meta:
        verbose_name = u'播放页'


class ImageShowPage(Page):
    class Meta:
        verbose_name = u'图片展示页'


# Index page


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
