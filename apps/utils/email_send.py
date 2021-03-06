__author__ = 'xianfuxing'
__date__ = '2017/11/19 21:41'

import random
from functools import wraps
from django.core.mail import send_mail
from django.conf import settings

from users.models import EmailVerifyRecord
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(48)
    # code = random_exp_str(48)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type == 'register':
        email_title = '慕学在线注册激活链接'
        email_body = '请点击以下链接激活您的账号: http://127.0.0.1:8000/users/register/activate/{0}'.format(code)

        send_status = send_mail(email_title, email_body, 'xianfuxing@126.com', [email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '慕学在线密码重置链接'
        email_body = '请点击以下链接重置密码: http://127.0.0.1:8000/users/reset/{0}'.format(code)

        send_status = send_mail(email_title, email_body, 'xianfuxing@126.com', [email])


def random_str(length=16):
    s = ''
    chars = 'AaBbCcDdEdFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_'
    index = len(chars) - 1
    for i in range(length):
        s += chars[random.randint(0, index)]
    return s


def random_exp_str(length=16):
    secret_key = settings.SECRET_KEY
    s = Serializer(secret_key, expires_in=300)
    return s