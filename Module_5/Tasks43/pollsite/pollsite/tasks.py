from time import sleep
from pollsite.celery import app


@app.task
def hello_world():
    sleep(5)  # поставим тут задержку в 10 сек для демонстрации ассинхрности
    print('Hello World')
