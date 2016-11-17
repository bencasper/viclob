# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import AbstractUser, User
from django.db import models

from captcha.fields import CaptchaField
from django import forms


# Create your models here.

# class User(AbstractUser):
#     phone = models.IntegerField(u'手机号码', max_length=11 , blank=True)
#     # REQUIRED_FIELDS = ['email']


class RegistrationForm(forms.Form):
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=False, max_length=30)),
                                label=u"用户名", error_messages={
            'invalid': u"用户名只能含有数字、字母和 _"})
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=u"电子邮件")
    phone = forms.IntegerField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=u"手机号码")
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=u"密码")
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)),
        label=u"再次输入密码")
    # valid_code = forms.IntegerField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=u"手机验证码")

    captcha = CaptchaField(label=u'验证码')

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(u"此用户名已存在.")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(u"两次输入的密码不一致.")

        return self.cleaned_data

