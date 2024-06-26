from celery import Celery

app = Celery("breamer_tasks", broker="redis://127.0.0.1:6379/0")
