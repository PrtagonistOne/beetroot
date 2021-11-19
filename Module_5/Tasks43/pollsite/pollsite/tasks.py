# Create your tasks here
from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def add(x, y):
    sleep(2)
    print(x + y)


@shared_task
def mul(x, y):
    sleep(4)
    print(x * y)


@shared_task
def xsum(numbers):
    sleep(6)
    print(sum(numbers))


@shared_task
def send_email_task():
    sleep(10)
    send_mail('Celery Task Worked!',
              'This is proof the task worked!',
              'playerdna4@gmail.com',
              ['nojamaw857@keagenan.com'])

    return None
