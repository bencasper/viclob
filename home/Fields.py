# -*- coding: utf-8 -*-

from django.db import models
from django import forms
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, \
    PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.blocks import StreamBlock, CharBlock, RichTextBlock, StructBlock, TextBlock, FieldBlock, \
    RawHTMLBlock
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


# A couple of abstract classes that contain commonly used fields


class LinkFields(models.Model):
    link_external = models.URLField(u'链接地址', blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        elif self.link_document:
            return self.link_document.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
    ]

    class Meta:
        abstract = True


class ContactFields(models.Model):
    telephone = models.CharField(verbose_name=u'电话', max_length=20, blank=True)
    email = models.EmailField(blank=True)
    wechat = models.CharField(verbose_name=u'微信', max_length=255, blank=True)
    address_1 = models.CharField(verbose_name=u'地址', max_length=255, blank=True)
    city = models.CharField(verbose_name=u'城市', max_length=255, blank=True)
    # country = models.CharField(max_length=255, blank=True)
    post_code = models.CharField(verbose_name=u'邮编', max_length=10, blank=True)

    panels = [
        FieldPanel('city'),
        FieldPanel('address_1'),
        FieldPanel('telephone'),
        FieldPanel('email'),
        FieldPanel('wechat'),

        # FieldPanel('country'),
        # FieldPanel('post_code'),
    ]

    class Meta:
        abstract = True


# Carousel items
class CarouselItem(LinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField(u'链接URL', blank=True)
    caption = models.CharField(verbose_name=u'标题', max_length=255, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('embed_url'),
        FieldPanel('caption'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


# case
class CaseItem(LinkFields):
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    intro = models.CharField(verbose_name=u'简介', max_length=255, blank=True);
    title = models.CharField(verbose_name=u'名称', max_length=255, blank=True)

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('logo'),
        FieldPanel('intro'),
    ]

    class Meta:
        abstract = True


# # video items
# class VideoItem(LinkFields):
#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#     embed_url = models.URLField(u'链接URL', blank=True)
#     caption = models.CharField(verbose_name=u'标题', max_length=255, blank=True)
#
#     panels = [
#         ImageChooserPanel('image'),
#         FieldPanel('embed_url'),
#         FieldPanel('caption'),
#         MultiFieldPanel(LinkFields.panels, "Link"),
#     ]
#
#     class Meta:
#         abstract = True


# provider items
class ProviderItem(models.Model):
    title = models.CharField(verbose_name=u'供应商', max_length=255)
    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    embed_url = models.URLField(u'链接URL', blank=True)
    products = RichTextField(verbose_name=u'主要产品')
    customers = RichTextField(verbose_name=u'客户方向')
    panels = [
        FieldPanel('title'),
        ImageChooserPanel('logo'),
        FieldPanel('embed_url'),
        FieldPanel('products'),
        FieldPanel('customers'),
    ]

    class Meta:
        abstract = True


# Global Streamfield definition


class PullQuoteBlock(StructBlock):
    quote = TextBlock(label=u'引用正文')
    attribution = CharBlock(label=u'引用自')

    class Meta:
        icon = "openquote"


class ImageFormatChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('left', u'居左'), ('right', u'居右'), ('mid', u'居中'), ('full', u'全尺寸'),
    ))


class HTMLAlignmentChoiceBlock(FieldBlock):
    field = forms.ChoiceField(choices=(
        ('normal', u'普通'), ('full', u'全尺寸'),
    ))


class ImageBlock(StructBlock):
    image = ImageChooserBlock(label=u'请选择图片')
    caption = RichTextBlock()
    alignment = ImageFormatChoiceBlock()


class AlignedHTMLBlock(StructBlock):
    html = RawHTMLBlock()
    alignment = HTMLAlignmentChoiceBlock()

    class Meta:
        icon = "code"


class ContentStreamBlock(StreamBlock):
    h2 = CharBlock(icon="title", classname="title")
    h3 = CharBlock(icon="title", classname="title")
    h4 = CharBlock(icon="title", classname="title")
    intro = RichTextBlock(icon="pilcrow", label=u'简介')
    paragraph = RichTextBlock(icon="pilcrow", label=u'段落')
    aligned_image = ImageBlock(label=u'图片', icon="image")
    pullquote = PullQuoteBlock(label=u'引言')
    aligned_html = AlignedHTMLBlock(icon="code", label=u'HTML 代码')
    document = DocumentChooserBlock(icon="doc-full-inverse", label=u'请选择文本')


# Global Streamfield definition end

class IndexItem(models.Model):
    title = models.CharField(verbose_name=u'主题', max_length=255)

    panels = [
        FieldPanel('title'),

    ]

    class Meta:
        abstract = True


class TopicItem(models.Model):
    title = models.CharField(verbose_name=u'主题', max_length=255)
    desc = RichTextField(verbose_name=u'简介', blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('desc', classname='full'),
        ImageChooserPanel('image'),

    ]

    class Meta:
        abstract = True


class VideoItem(models.Model):
    title = models.CharField(verbose_name=u'视频名称', max_length=255)
    code = RichTextField(verbose_name=u'视频代码', max_length=255)

    code = StreamField([
        ('code', blocks.RawHTMLBlock()),
    ])

    panels = [
        FieldPanel('title'),
        StreamFieldPanel('code'),

    ]

    class Meta:
        abstract = True


class CareerShowItem(models.Model):
    name = models.CharField(verbose_name=u'从业者名称', max_length=255)
    title = models.CharField(verbose_name=u'从业者title', max_length=255)
    content = RichTextField(verbose_name=u'简介', blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('title'),
        FieldPanel('content', classname='full'),
        ImageChooserPanel('image'),

    ]

    class Meta:
        abstract = True


#
# class VideoItem(models.Model):
#     video = models.ForeignKey(
#         'wagtail_embed_videos.EmbedVideo',
#         verbose_name="Video",
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#     panels = [EmbedVideoChooserPanel('video')]
#

# Related links
class RelatedLink(LinkFields):
    title = models.CharField(verbose_name=u'标题', max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True
