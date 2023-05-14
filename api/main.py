from fastapi import FastAPI

from pydantic import BaseModel
from typing import List, Optional
from celery import Celery

class TaskID(BaseModel):
    id: str
    game: Optional[str]

app = FastAPI()

simple_worker = Celery('simple_worker',backend='redis://redis:6379/', broker='redis://redis:6379/')



@app.get('/')
def home():
    return {"message":"home"}

@app.get('/triggerwelcome')
def triggerwelcome():
    result = simple_worker.send_task('tasks.welcome')
    return result.id

@app.post('/taskstatus')
def taskstatus(taskid:TaskID):
    print(taskid.id)
    result = simple_worker.AsyncResult(taskid.id)
    print(result.ready())
    return {"status":result.status,"value":result.result if result.ready() else None}