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
    InlinePanel('home_distribute_items', label=u'视频全媒体分发'),
    InlinePanel('home_cloud_items', label=u'视频云'),
    InlinePanel('home_film_items', label=u'视频拍摄制作'),
    InlinePanel('carousel_case_items', label="案例展示图"),
    InlinePanel('carousel_partner_items', label="合作伙伴展示图"),

]


class FirstPageDistributeItems(Orderable, TopicItem):
    page = ParentalKey('home.FirstPage', related_name='home_distribute_items')


class FirstPageCloudItems(Orderable, TopicItem):
    page = ParentalKey('home.FirstPage', related_name='home_cloud_items')


class FirstPageFilmItems(Orderable, TopicItem):
    page = ParentalKey('home.FirstPage', related_name='home_film_items')


class FirstPageCaseItem(Orderable, CarouselItem):
    page = ParentalKey('home.FirstPage', related_name='carousel_case_items')


class FirstPagePartnerItems(Orderable, CarouselItem):
    page = ParentalKey('home.FirstPage', related_name='carousel_partner_items')


class ServiceIndexPage(Page):
    class Meta:
        verbose_name = u'服务首页'


# 视频全媒体发布
class DistributePage(Page):
    class Meta:
        verbose_name = u'视频全媒体发布'


DistributePage.content_panels = [
    InlinePanel('oneClick_item', label=u'一键接入'),
    InlinePanel('distribute_item', label=u'全媒体分发'),
    InlinePanel('bigData_item', label=u'数据分析系统'),
    InlinePanel('selfMedia_item', label=u'自频道运营推广'),
]


class DistributePageOneclickItem(Orderable, TopicItem):
    page = ParentalKey('home.DistributePage', related_name='oneClick_item')


class DistributePageDistributeItem(Orderable, TopicItem):
    page = ParentalKey('home.DistributePage', related_name='distribute_item')


class DistributePageBigDataItem(Orderable, TopicItem):
    page = ParentalKey('home.DistributePage', related_name='bigData_item')


class DistributePageSelfMediaItem(Orderable, TopicItem):
    page = ParentalKey('home.DistributePage', related_name='selfMedia_item')


# 视频云
class CloudPage(Page):
    class Meta:
        verbose_name = u'视频云服务'


CloudPage.content_panels = [
    InlinePanel('news_item', label=u'视频云咨询'),
    InlinePanel('ask_item', label=u'视频云询价'),
]


class CloudPageNewsItem(Orderable, TopicItem):
    page = ParentalKey('home.CloudPage', related_name='news_item')


class CloudPageAskItem(Orderable, TopicItem):
    page = ParentalKey('home.CloudPage', related_name='ask_item')


# 拍摄制作
class FilmPage(Page):
    class Meta:
        verbose_name = u'视频拍摄制作'


FilmPage.content_panels = [
    InlinePanel('film_item', label=u'视频拍摄制作'),
    InlinePanel('loan_item', label=u'视频设备租赁'),
    InlinePanel('partner_item', label=u'合作客户及作品列表'),

]


class FilmPageNewsItem(Orderable, TopicItem):
    page = ParentalKey('home.FilmPage', related_name='film_item')


class FilmLoanAskItem(Orderable, TopicItem):
    page = ParentalKey('home.FilmPage', related_name='loan_item')


class FilmPageAskItem(Orderable, TopicItem):
    page = ParentalKey('home.FilmPage', related_name='partner_item')


# 咨询首页
class NewsIndexPage(Page):
    class Meta:
        verbose_name = u'咨询首页'


class TechNewsIndexPage(Page):
    class Meta:
        verbose_name = u'技术咨询首页'


class TechNewsPage(Page):
    body = RichTextField(blank=True)
    type = models.IntegerField(choices=NEWS_TYPES,
                               default=1)

    class Meta:
        verbose_name = u'咨询内容页'


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
        verbose_name = u'案例首页'


class CaseContentPage(Page):
    body = RichTextField(blank=True)
    type = models.IntegerField(choices=CASE_SHOW_TYPES,
                               default=1)

    class Meta:
        verbose_name = u'案例展示内容页'


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
        verbose_name = u'联系我们'


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
