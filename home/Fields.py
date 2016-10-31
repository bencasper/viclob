# -*- coding: utf-8 -*-

from django.db import models
from wagtail.tests.testapp.models import LinkFields

from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel
from wagtail.wagtailcore.blocks import RichTextBlock
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


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


class SubjectItem(models.Model):
    title = models.CharField(verbose_name=u'主题', max_length=255)
    desc = RichTextBlock(verbose_name=u'简介', icon="pilcrow")
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('desc'),
        ImageChooserPanel('image')

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
