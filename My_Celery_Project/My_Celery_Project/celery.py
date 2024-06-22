from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'My_Celery_Project.settings')

app = Celery('My_Celery_Project')



app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


import My_Celery_App.tasks

app.autodiscover_tasks(['My_Celery_App.tasks'])
# We used CELERY_BROKER_URL in settings.py instead of:
# app.conf.broker_url = ''

# We used CELERY_BEAT_SCHEDULER in settings.py instead of:
# app.conf.beat_scheduler = ''django_celery_beat.schedulers.DatabaseScheduler'

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')