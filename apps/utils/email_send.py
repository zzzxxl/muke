from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecode
from muke.settings import EMAIL_FROM


def send_register_email(email, send_type='register', len=16):
    email_record = EmailVerifyRecode()
    # 生成随机字符串
    code = random_str(len)

    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '注册激活链接'
        email_body = '点击链接激活:http://127.0.0.1:8000/active/{0}'.format(code)

        send_mail(email_title, email_body, EMAIL_FROM, [email])
        # send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # if send_status:
        #     pass
    elif send_type == 'forget':
        email_title = '密码重置链接'
        email_body = '点击重置密码:http://127.0.0.1:8000/reset/{0}'.format(code)
        send_mail(email_title, email_body, EMAIL_FROM, [email])

    elif send_type == 'update':
        email_title = '密码重置验证码'
        email_body = '密码重置验证码:{0}'.format(code)
        send_mail(email_title, email_body, EMAIL_FROM, [email])


def random_str(random_length=8):
    str = ''
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str