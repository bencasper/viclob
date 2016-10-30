# -*- coding: utf-8 -*-

from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, MultiFieldPanel, \
    InlinePanel, PageChooserPanel, StreamFieldPanel


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
