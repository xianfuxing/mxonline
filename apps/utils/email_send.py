__author__ = 'xianfuxing'
__date__ = '2017/11/19 21:41'

import random
import itsdangerous
from django.core.mail import send_mail

from users.models import EmailVerifyRecord


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code = random_str(32)
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


def random_str(length=16):
    s = ''
    chars = 'AaBbCcDdEdFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789_'
    index = len(chars) - 1
    for i in range(length):
        s += chars[random.randint(0, index)]
    return s

