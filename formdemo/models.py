from __future__ import unicode_literals

from captcha.fields import CaptchaField
from django import forms


class DemoForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

    captcha = CaptchaField()
