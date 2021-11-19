# Create your tasks here
from celery import shared_task
from time import sleep

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




