# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from django.db.models import Q
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import InlinePanel
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailforms.models import AbstractFormField, AbstractForm
from wagtail.wagtailsearch import index

from home.Fields import *


# A couple of static contants


# entry page
class HomePage(Page):
    @property
    def get_nav_page(self):
        print NavigationPage.objects.all()[0]
        return NavigationPage.objects.all()[0]

    class Meta:
        verbose_name = u'入口页面'


HomePage.content_panels = [
    # index
    InlinePanel('home_index_items', label=u'视频全媒体分发服务商'),

]


class HomePageSubjectItems(Orderable, IndexItem):
    page = ParentalKey('home.HomePage', related_name='home_index_items')


# navigation page
class NavigationPage(Page):
    class Meta:
        verbose_name = u'目录导航页面'


# class FirstPage(Page):
#     class Meta:
#         verbose_name = u'首页'
#
#
# # home page
# FirstPage.content_panels = [
#     FieldPanel('title', classname="full title"),
#     InlinePanel('business_carousel', label=u'业务内容展示图'),
#     InlinePanel('cloud_items', label=u'视频云资讯'),
#     InlinePanel('service_items', label=u'视频云服务'),
#     InlinePanel('case_carousel', label="作品展示图"),
#     InlinePanel('partner_carousel', label="合作伙伴展示图"),
#
# ]
#
#
# class FirstPageBusinessCarousel(Orderable, CarouselItem):
#     page = ParentalKey('home.FirstPage', related_name='business_carousel')
#
#
# class FirstPageCloudItems(Orderable, TopicItem):
#     page = ParentalKey('home.FirstPage', related_name='cloud_items')
#
#
# class FirstPageServiceItems(Orderable, TopicItem):
#     page = ParentalKey('home.FirstPage', related_name='service_items')
#
#
# class FirstPageCaseCarousel(Orderable, CarouselItem):
#     page = ParentalKey('home.FirstPage', related_name='case_carousel')
#
#
# class FirstPagePartnerCarouse(Orderable, CarouselItem):
#     page = ParentalKey('home.FirstPage', related_name='partner_carousel')

# service page
class ServiceIndexPage(Page):
    template = 'test_platform_page.html'

    class Meta:
        verbose_name = u'服务首页'


# 统一测试平台
class TestPlatformPage(Page):
    class Meta:
        verbose_name = u'统一测试平台页面'


# 视频制作
class VideoProduction(Page):
    class Meta:
        verbose_name = u'拍摄制作页面'


VideoProduction.content_panels = [
    FieldPanel('title', classname="full title"),
    InlinePanel('introduce_items', label=u'项目'),
    InlinePanel('video_items', label=u'作品')
]


class VideoProductionIntroduceItem(Orderable, TopicItem):
    page = ParentalKey('home.VideoProduction', related_name='introduce_items')


class VideoProductionIntroduceItem(Orderable, VideoItem):
    page = ParentalKey('home.VideoProduction', related_name='video_items')


# # 视频云代理
# class CloudPage(Page):
#     class Meta:
#         verbose_name = u'视频云代理'
#
#
# CloudPage.content_panels = [
#     FieldPanel('title', classname="full title"),
#     InlinePanel('introduce_items', label=u'业务介绍'),
# ]
#
#
# class CloudPageNewsItem(Orderable, TopicItem):
#     page = ParentalKey('home.CloudPage', related_name='introduce_items')


TECH_TYPES = (
    (0, '请选择技术新闻类型'), (1, u'点播'), (2, u'直播'), (3, u'播放器'), (4, u'CDN'), (5, u'编解码'), (6, u'存储'), (7, u'加密'), (8, u'安全'))
PROVIDER_TYPES = ((0, '请选择服务商新闻类型'), (1, u'阿里云'), (2, u'腾讯云'), (3, u'金山云'), (4, u'乐视云'), (5, u'七牛'))
SECTOR_TYPES = ((0, '请选择行业新闻类型'), (1, u'政策'), (2, u'资本'), (3, u'会议'))
CASE_TYPES = ((0, '请选择应用新闻类型'), (1, u'秀场'), (2, u'游戏'), (3, u'在线教育'), (4, u'新媒体'), (5, u'视频会议'), (6, u'监控'))
PRACTITIONER_TYPES = (
    (0, '请选择从业者新闻类型'), (1, u'营销'), (2, u'市场'), (3, u'产品'), (4, u'运营'), (5, u'测试'), (6, u'开发'), (7, u'技术支持'))


# 资讯内容页
class NewsContentPage(Page):
    body = RichTextField(blank=True)
    techType = models.IntegerField(choices=TECH_TYPES,
                                   default=0)
    providerType = models.IntegerField(choices=PROVIDER_TYPES,
                                       default=0)
    sectorType = models.IntegerField(choices=SECTOR_TYPES,
                                     default=0)
    caseType = models.IntegerField(choices=CASE_TYPES,
                                   default=0)
    practitionerType = models.IntegerField(choices=PRACTITIONER_TYPES,
                                           default=0)

    class Meta:
        verbose_name = u'资讯内容页'


NewsContentPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('techType'),
    FieldPanel('providerType'),
    FieldPanel('sectorType'),
    FieldPanel('caseType'),
    FieldPanel('practitionerType'),

    FieldPanel('body', classname="full"),
]


# 资讯首页
class NewsIndexPage(Page):
    # def route(self, request, path_components):
    #     return RouteResult(TechNewsIndexPage.objects.all()[0], kwargs={'path_components': path_components})
    @property
    def subNewsTypes(self):
        return TECH_TYPES

    @property
    def contentList(self):
        return NewsContentPage.objects.filter(~Q(techType=0)).order_by('latest_revision_created_at')[:10]

    template = 'home/tech_news_index_page.html'

    class Meta:
        verbose_name = u'资讯首页'


class TechNewsIndexPage(Page):
    @property
    def subNewsTypes(self):
        return TECH_TYPES

    @property
    def contentList(self):
        return NewsContentPage.objects.filter(~Q(techType=0)).order_by('latest_revision_created_at')[:10]

    class Meta:
        verbose_name = u'技术资讯首页'


class ProviderNewsIndexPage(Page):
    # PROVIDER_TYPES = ((0, '请选择服务商新闻类型'), (1, u'阿里云'), (2, u'腾讯云'), (3, u'金山云'), (4, u'乐视云'), (5, u'七牛'))

    @property
    def subNewsTypes(self):
        return PROVIDER_TYPES

    @property
    def contentList(self):
        return NewsContentPage.objects.filter(~Q(providerType=0)).order_by('latest_revision_created_at')[:10]

    template = 'home/tech_news_index_page.html'

    class Meta:
        verbose_name = u'服务商首页'


class SectorNewsIndexPage(Page):
    # SECTOR_TYPES = ((0, '请选择行业新闻类型'), (1, u'政策'), (2, u'资本'), (3, u'会议'))

    @property
    def subNewsTypes(self):
        return SECTOR_TYPES

    @property
    def contentList(self):
        return NewsContentPage.objects.filter(~Q(sectorType=0)).order_by('latest_revision_created_at')[:10]

    template = 'home/tech_news_index_page.html'

    class Meta:
        verbose_name = u'行业首页'


class CaseNewsIndexPage(Page):
    # CASE_TYPES = ((0, '请选择应用新闻类型'), (1, u'秀场'), (2, u'游戏'), (3, u'在线教育'), (4, u'新媒体'), (5, u'视频会议'), (6, u'监控'))

    @property
    def subNewsTypes(self):
        return CASE_TYPES

    @property
    def contentList(self):
        return NewsContentPage.objects.filter(~Q(caseType=0)).order_by('latest_revision_created_at')[:10]

    template = 'home/tech_news_index_page.html'

    class Meta:
        verbose_name = u'应用首页'


class PractitionerIndexPage(Page):
    # PRACTITIONER_TYPES = ((0, '请选择从业者新闻类型'), (1, u'营销'), (2, u'市场'), (3, u'产品'), (4, u'运营'), (5, u'测试'), (6, u'开发'), (7, u'技术支持'))

    @property
    def subNewsTypes(self):
        return PRACTITIONER_TYPES

    @property
    def contentList(self):
        return NewsContentPage.objects.filter(~Q(practitionerType=0)).order_by('latest_revision_created_at')[:10]

    template = 'home/tech_news_index_page.html'

    class Meta:
        verbose_name = u'从业者首页'


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
]



class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='form_fields')


class FormPage(AbstractForm):
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


