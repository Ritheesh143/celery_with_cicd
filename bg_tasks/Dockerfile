FROM python:3.10

copy ./requirements.txt /bg_tasks/

copy ./tasks.py /bg_tasks/

workdir /bg_tasks

run pip install -r requirements.txt

cmd celery -A tasks worker --pool=solo --loglevel=INFO