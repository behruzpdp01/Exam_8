from django.core.mail import send_mail
from django.http import HttpResponse

from apps.models import User
from root.settings import EMAIL_HOST_USER


def send_emails(to_email: list):
    print(to_email)
    send_mail('Subject', 'msg', EMAIL_HOST_USER, to_email, False)
    return {"status": "success", "message": f"{'.'.join(to_email)} send email successfully"}



def send_email_task(req):
    return HttpResponse(send_emails('Xabar', 'Behruz', User.objects.filter('email')))