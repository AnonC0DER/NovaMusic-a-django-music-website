from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task

@shared_task
def send_email_task(email):
    '''Send email to user after submitting a new comment'''
    send_mail(
        subject='Your comment successfully submitted !',
        message='It will be available after admin review.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )

    print(f'Email successfully sent to {email}')