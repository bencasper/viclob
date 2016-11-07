# -*- coding: utf-8 -*-

from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


# A couple of abstract classes that contain commonly used fields

class LinkFields(models.Model):
    link_external = models.URLField("链接地址", blank=True)
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
        FieldPanel('telephone'),
        FieldPanel('email'),
        FieldPanel('wechat'),
        FieldPanel('address_1'),
        FieldPanel('city'),
        # FieldPanel('country'),
        FieldPanel('post_code'),
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


# Related links
class RelatedLink(LinkFields):
    title = models.CharField(verbose_name=u'标题', max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True
