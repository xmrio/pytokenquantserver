from django.contrib.admin.forms import (
    AdminAuthenticationForm as _AdminAuthenticationForm
)

from captcha.fields import CaptchaField


class AdminAuthenticationForm(_AdminAuthenticationForm):
    captcha = CaptchaField()
