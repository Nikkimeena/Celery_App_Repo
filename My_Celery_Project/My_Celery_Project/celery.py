from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import timedelta
import My_Celery_App.tasks
from decouple import config
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_Celery_Project.settings')

app = Celery('My_Celery_Project')



app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')