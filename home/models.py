# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailforms.models import AbstractFormField, AbstractEmailForm
from wagtail.wagtailsearch import index

from home.Fields import *

# A couple of static contants

TECHES = ((1, u'基础'), (2, u'直播'), (3, u'点播'))


class HomePage(Page):
    class Meta:
        verbose_name = u'首页'


HomePage.content_panels = [
    InlinePanel('home_subject_items', label=u'页面板块内容简介'),
    InlinePanel('home_carousel_items', label=u"Carousel items"),
    InlinePanel('home_related_links', label=u"友情链接"),

]


class HomePageSubjectItems(Orderable, TopicItem):
    page = ParentalKey('home.HomePage', related_name='home_subject_items')


class HomePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.HomePage', related_name='home_carousel_items')


class HomePageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.HomePage', related_name='home_related_links')


# Content page

class ContentPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.ContentPage', related_name='content_carousel_items')


class ContentPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.ContentPage', related_name='content_related_links')


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
    FieldPanel('body', classname="full"),
    InlinePanel('content_carousel_items', label="Carousel items"),
    InlinePanel('content_related_links', label=u"友情链接"),
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
    desc = RichTextField(verbose_name=u'简介', blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    video_code = models.URLField(verbose_name=u'', max_length=255, blank=False)

    search_fields = Page.search_fields + [
        index.SearchField('title')
    ]

    class Meta:
        verbose_name = u'播放页'


VideoPlayPage.content_panels = [
    FieldPanel('title', classname='full title'),
    FieldPanel('desc', classname='full'),
    ImageChooserPanel('image'),
    FieldPanel('video_code', classname='full')
]


class ImageShowPageCarouseItem(Orderable, CarouselItem):
    page = ParentalKey('home.ImageShowPage', related_name='image_carousel_items')


class ImageShowPage(ContentPage):
    InlinePanel('image_carousel_items', label="Carousel items"),

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


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractEmailForm):
    intro = RichTextField(verbose_name=u'简介', blank=True)
    thank_you_text = RichTextField(verbose_name=u'表单提交后提示语', blank=True)


FormPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('intro', classname="full"),
    InlinePanel('form_fields', label="表单字段"),
    FieldPanel('thank_you_text', classname="full"),
    # MultiFieldPanel([
    #     FieldRowPanel([
    #         FieldPanel('from_address', classname="col6"),
    #         FieldPanel('to_address', classname="col6"),
    #     ]),
    #     FieldPanel('subject'),
    # ], "Email"),
]
