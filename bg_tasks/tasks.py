from celery import Celery
import time


celery_app = Celery('tasks',backend='redis://redis:6379/', broker='redis://redis:6379/')

@celery_app.task
def welcome():
    print("welcome by celery")
    time.sleep(3)
    return "hello" 