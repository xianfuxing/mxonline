from functools import wraps
from django.core.mail import send_mail
from users.models import EmailVerifyRecord
from utils.email_send import random_str


def require_send_type(send_type):
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(email, *args, **kwargs):
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

                send_status = func(email, email_title, email_body, 'xianfuxing@126.com')
                if send_status:
                    pass
            elif send_type == 'forget':
                email_title = '慕学在线密码重置链接'
                email_body = '请点击以下链接重置密码: http://127.0.0.1:8000/users/reset/{0}'.format(code)

            send_status = func(email, email_title, email_body, 'xianfuxing@126.com')

            return send_status
        return return_wrapper
    return func_wrapper


@require_send_type('forget')
def im_send_mail(email, *args):
    send_mail(*args, [email])