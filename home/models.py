# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

from random import randint

from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.template.response import TemplateResponse
from hitcount.models import HitCount
from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.wagtailadmin.edit_handlers import InlinePanel, StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.url_routing import RouteResult
from wagtail.wagtailforms.models import AbstractFormField, AbstractForm
from wagtail.wagtailsearch import index

from home.Fields import *


# A couple of static contants


class MenuPage(Page):
    menu_priority = models.SmallIntegerField(verbose_name=u'目录权重',
                                             default=10,
                                             blank=True)

    class Meta:
        abstract = True


MenuPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('menu_priority')
]


# entry page
class HomePage(MenuPage):
    # @property
    # def get_nav_page(self):
    #     if NavigationPage.objects.all():
    #         return NavigationPage.objects.all()[0]
    #     else:
    #         return self

    template = 'home/navigation_page.html'

    class Meta:
        verbose_name = u'入口页面'


# navigation page
class NavigationPage(MenuPage):
    class Meta:
        verbose_name = u'目录导航页面'


# solution page
class SolutionPage(MenuPage):
    class Meta:
        verbose_name = u'解决方案页面'


# case page
class CasePageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.CasePage', related_name='carousel_items')


class CasePageVideoItem(Orderable, VideoItem):
    page = ParentalKey('home.CasePage', related_name='video_items')


class CasePage(MenuPage):
    class Meta:
        verbose_name = u'案例页面'


CasePage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('menu_priority'),
    InlinePanel('carousel_items', label=u"合作客户"),
    InlinePanel('video_items', label=u"视频"),
]

INDEX_TYPES = ((0, u'请选择首页类型'),)
CONTENT_TYPES = ((0, u'请选择内容类型'),)


# Base page
class BasicPage(Page):
    """
            HitCountMixin provides an easy way to add a `hit_count` property to your
            model that will return the related HitCount object.
            """
    type = models.IntegerField(choices=CONTENT_TYPES,
                               default=0)

    @property
    def hit_count(self):
        ctype = ContentType.objects.get_for_model(self.__class__)
        hit_count, created = HitCount.objects.get_or_create(
            content_type=ctype, object_pk=self.pk)
        if hit_count.hits < 100:
            init_num = randint(100, 1000)
            # for i in range(init_num):
            #     hit_count.increase()
            hit_count.hits = init_num
            hit_count.save()
        return hit_count

    @property
    def like_count(self):
        ctype = ContentType.objects.get_for_model(self.__class__)
        like_count, created = HitCount.objects.get_or_create(
            content_type=ctype, object_pk=self.pk)
        if like_count.hits < 100:
            init_num = randint(50, 200)

            like_count.hits = init_num
            like_count.save()
        return like_count

    def serve(self, request):
        if "like" in request.GET:
            self.like_count.increase()
            response = HttpResponse(
                self.like_count,
                content_type='application/json',
            )
            return response
        else:
            self.hit_count.increase()
            return super(BasicPage, self).serve(request)

    class Meta:
        abstract = True


# abstract index page

class IndexPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.IndexPage', related_name='related_links')


# 行业资讯 indexPage
class IndexPage(MenuPage):
    intro = RichTextField(blank=True)
    type = models.IntegerField(choices=INDEX_TYPES,
                               default=0)
    search_fields = Page.search_fields + [
        index.SearchField('intro'),
    ]

    @property
    def contents(self):
        # Get list of live blog pages that are descendants of this page
        contents = ContentPage.objects.live().descendant_of(self)

        # Order by most recent date first
        contents = contents.order_by('-date')

        return contents

    def get_context(self, request):

        print 'get context'
        # Get blogs
        contents = self.contents
        page_count = contents.count()


        # Filter by tag
        tag = request.GET.get('tag')
        author = request.GET.get('author')
        print tag
        order_by = request.GET.get('orderBy')
        if tag:
            contents = contents.filter(tags__name=tag)
        elif author:
            print 'author------------' , author
            contents = contents.filter(author=author)
        elif order_by:
            if order_by == 'hit':
                contents = contents.order_by('-order_by')
        print contents.count()
        # Pagination
        page = request.GET.get('page')
        if not page:
            page = 1
        paginator = Paginator(contents, 5)  # Show 5 contents per page
        try:
            contents = paginator.page(page)
        except PageNotAnInteger:
            contents = paginator.page(1)
        except EmptyPage:
            contents = paginator.page(paginator.num_pages)

        # Update template context
        context = super(IndexPage, self).get_context(request)

        for content in contents:
            print 'a'
            print content

        context['contents'] = contents
        context['pagecount'] = page_count
        if page > 1:
            context['pre'] = int(page) - 1

        print page, page_count
        print int(page) * 5 < page_count
        if int(page) * 5 < page_count:
            print '----next----'
            context['next'] = int(page) + 1
        if tag:
            context['tag'] = tag
        return context

    def serve(self, request, *args, **kwargs):
        request.is_preview = getattr(request, 'is_preview', False)
        print 'serve'


        context = self.get_context(request, *args, **kwargs)
        for content in context['contents']:
            print 'debug'
            print content

        return TemplateResponse(
            request,
            self.get_template(request, *args, **kwargs),
            context
        )


IndexPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('menu_priority'),
    FieldPanel('intro', classname="full"),
    InlinePanel('related_links', label="Related links"),
]

IndexPage.promote_panels = Page.promote_panels


# Content page
class ContentPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.ContentPage', related_name='carousel_items')


class ContentPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.ContentPage', related_name='related_links')


class ContentPageTag(TaggedItemBase):
    content_object = ParentalKey('home.ContentPage', related_name='tagged_items')


class ContentPage(BasicPage):
    body = StreamField(ContentStreamBlock())
    tags = ClusterTaggableManager(through=ContentPageTag, blank=True)
    author = models.CharField(verbose_name=u"发布人", max_length=20, blank=True)
    date = models.DateField(u"发布时间")
    thumbnail = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

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

    @property
    def index(self):
        # Find closest ancestor which is a blog index
        return self.get_ancestors().type(IndexPage).last()

    class Meta:
        verbose_name = u'通用内容页'


ContentPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('author'),
    FieldPanel('date'),
    FieldPanel('type'),
    ImageChooserPanel('thumbnail'),
    StreamFieldPanel('body'),
    InlinePanel('carousel_items', label="Carousel items"),
    InlinePanel('related_links', label="Related links"),
]

ContentPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
    FieldPanel('tags'),
]


# 咨询
class NewsIndexPage(IndexPage):
    def serve(self, request, *args, **kwargs):
        page = EventIndexPage.objects.first()
        return EventIndexPage.serve(page, request)

    class Meta:
        verbose_name = u'资讯首页'


class EventIndexPage(IndexPage):
    template = 'home/index_base.html'

    class Meta:
        verbose_name = u'动态'


class TechIndexPage(IndexPage):
    template = 'home/index_base.html'

    class Meta:
        verbose_name = u'技术List'


class ColumnIndexPage(IndexPage):
    template = 'home/index_base.html'

    class Meta:
        verbose_name = u'专栏List'


class CareerIndexPage(IndexPage):
    template = 'home/index_base.html'

    class Meta:
        verbose_name = u'圈子List'


# 服务商
# Standard page

class StandardPageCarouselItem(Orderable, CarouselItem):
    page = ParentalKey('home.StandardPage', related_name='carousel_items')


class StandardPageRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('home.StandardPage', related_name='related_links')


class StandardPage(MenuPage):
    # intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        # index.SearchField('intro'),
        index.SearchField('body'),
    ]

    class Meta:
        verbose_name = u'服务商内容页'


StandardPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('menu_priority'),
    # FieldPanel('intro', classname="full"),
    InlinePanel('carousel_items', label="logos"),
    FieldPanel('body', classname="full"),
    InlinePanel('related_links', label="Related links"),
]

StandardPage.promote_panels = Page.promote_panels + [
    ImageChooserPanel('feed_image'),
]


class VODIndexPage(IndexPage):
    class Meta:
        verbose_name = u'点直播List'


class CNDIndexPage(IndexPage):
    class Meta:
        verbose_name = u'流媒体加速List'


class VCIndexPage(IndexPage):
    class Meta:
        verbose_name = u'视频会议List'


class MonitorIndexPage(IndexPage):
    class Meta:
        verbose_name = u'远程监控List'


class IOTIndexPage(IndexPage):
    class Meta:
        verbose_name = u'物联网List'


class ProviderIndexPage(VODIndexPage):
    class Meta:
        verbose_name = u'服务商首页'


# 从业者


class ViewIndexPage(IndexPage):
    class Meta:
        verbose_name = u'观点List'


class FAQIndexPage(IndexPage):
    class Meta:
        verbose_name = u'FAQ List'


# Contact page

class ContactPage(MenuPage):
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
        verbose_name = u'联系首页'


ContactPage.content_panels = [
    FieldPanel('title', classname="full title"),
    FieldPanel('menu_priority'),
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
