# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from modelcluster.fields import ParentalKey
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.url_routing import RouteResult
from wagtail.wagtailforms.models import AbstractFormField, AbstractEmailForm
from wagtail.wagtailsearch import index

from home.Fields import *

# A couple of static contants

NEWS_TYPES = ((1, u'点播'), (2, u'直播'), (3, u'播放器'), (4, u'CDN'), (5, u'编解码'), (6, u'存储'), (7, u'加密'), (8, u'安全'))
PROVIDER_TYPES = ((1, u'阿里云'), (2, u'腾讯云'), (3, u'金山云'), (4, u'乐视云'), (5, u'七牛'))
CASE_NEW_TYPES = ((1, u'泛娱乐'), (2, u'电商'), (1, u'教育'), (1, u'新媒体'), (1, u'政府'))

CASE_SHOW_TYPES = ((1, u'合作客户'), (2, u'作品展示'))


# entry page
class HomePage(Page):
    class Meta:
        verbose_name = u'入口页面'


HomePage.content_panels = [
    # index
    InlinePanel('home_index_items', label=u'视频全媒体分发服务商'),

]


class HomePageSubjectItems(Orderable, IndexItem):
    page = ParentalKey('home.HomePage', related_name='home_index_items')


class FirstPage(Page):
    class Meta:
        verbose_name = u'首页'


# home page
FirstPage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel('business_carousel', label=u'业务内容展示图'),
    InlinePanel('cloud_items', label=u'视频云资讯'),
    InlinePanel('service_items', label=u'视频云服务'),
    InlinePanel('case_carousel', label="作品展示图"),
    InlinePanel('partner_carousel', label="合作伙伴展示图"),

]


class FirstPageBusinessCarousel(Orderable, CarouselItem):
    page = ParentalKey('home.FirstPage', related_name='business_carousel')


class FirstPageCloudItems(Orderable, TopicItem):
    page = ParentalKey('home.FirstPage', related_name='cloud_items')


class FirstPageServiceItems(Orderable, TopicItem):
    page = ParentalKey('home.FirstPage', related_name='service_items')


class FirstPageCaseCarousel(Orderable, CarouselItem):
    page = ParentalKey('home.FirstPage', related_name='case_carousel')


class FirstPagePartnerCarouse(Orderable, CarouselItem):
    page = ParentalKey('home.FirstPage', related_name='partner_carousel')


class ServiceIndexPage(Page):
    class Meta:
        verbose_name = u'服务首页'


# 视频制作
class VideoProduction(Page):
    class Meta:
        verbose_name = u'视频制作'


VideoProduction.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel('introduce_items', label=u'业务介绍'),
]


class VideoProductionIntroduceItem(Orderable, TopicItem):
    page = ParentalKey('home.VideoProduction', related_name='introduce_items')


# 视频云代理
class CloudPage(Page):
    class Meta:
        verbose_name = u'视频云代理'


CloudPage.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel('introduce_items', label=u'业务介绍'),
]


class CloudPageNewsItem(Orderable, TopicItem):
    page = ParentalKey('home.CloudPage', related_name='introduce_items')


# 资讯首页
class NewsIndexPage(Page):
    class Meta:
        verbose_name = u'资讯首页'


class TechNewsIndexPage(Page):
    class Meta:
        verbose_name = u'技术资讯首页'


class TechNewsPage(Page):
    body = RichTextField(blank=True)
    type = models.IntegerField(choices=NEWS_TYPES,
                               default=1)

    class Meta:
        verbose_name = u'资讯内容页'


TechNewsPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('type'),
    FieldPanel('body', classname="full"),
]


class ProviderNewsIndexPage(Page):
    class Meta:
        verbose_name = u'服务商首页'


class ProviderNewsPage(Page):
    body = RichTextField(blank=True)
    type = models.IntegerField(choices=PROVIDER_TYPES,
                               default=1)

    class Meta:
        verbose_name = u'服务商内容页'


ProviderNewsPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('type'),
    FieldPanel('body', classname="full"),
]


#

class CaseNewsIndexPage(Page):
    class Meta:
        verbose_name = u'行业应用首页'


class CaseNewsPage(Page):
    body = RichTextField(blank=True)
    type = models.IntegerField(choices=CASE_NEW_TYPES,
                               default=1)

    class Meta:
        verbose_name = u'行业应用内容页'


CaseNewsPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('type'),
    FieldPanel('body', classname="full"),
]


class CaseIndexPage(Page):
    class Meta:
        verbose_name = u'从业者首页'


class CaseContentPage(Page):
    body = RichTextField(blank=True)
    type = models.IntegerField(choices=CASE_SHOW_TYPES,
                               default=1)

    class Meta:
        verbose_name = u'从业者资讯内容页'


CaseContentPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('type'),
    FieldPanel('body', classname="full"),
]


# Index page


# Contact page

class ContactPage(Page):
    body = RichTextField(verbose_name='简介', blank=True)
    telephone = models.CharField(verbose_name=u'电话', max_length=20, blank=True)
    email = models.EmailField(blank=True)
    wechat = models.CharField(verbose_name=u'微信', max_length=255, blank=True)
    address = models.CharField(verbose_name=u'地址', max_length=255, blank=True)

    wechat_qrcode = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    self_media_qrcode = models.ForeignKey(
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
        verbose_name = u'关于我们'


ContactPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('body', classname="full"),
    FieldPanel('telephone', classname='full'),
    FieldPanel('email', classname='full'),
    FieldPanel('wechat', classname='full'),
    FieldPanel('address', classname='full'),
    ImageChooserPanel('wechat_qrcode'),
    ImageChooserPanel('self_media_qrcode'),
]



# class FormField(AbstractFormField):
#     page = ParentalKey('FormPage', related_name='form_fields')
#
#
# class FormPage(AbstractEmailForm):
#     intro = RichTextField(verbose_name=u'简介', blank=True)
#     thank_you_text = RichTextField(verbose_name=u'表单提交后提示语', blank=True)
#
#
# FormPage.content_panels = [
#     FieldPanel('title', classname="full title"),
#     FieldPanel('intro', classname="full"),
#     InlinePanel('form_fields', label="表单字段"),
#     FieldPanel('thank_you_text', classname="full"),
#     # MultiFieldPanel([
#     #     FieldRowPanel([
#     #         FieldPanel('from_address', classname="col6"),
#     #         FieldPanel('to_address', classname="col6"),
#     #     ]),
#     #     FieldPanel('subject'),
#     # ], "Email"),
# ]
