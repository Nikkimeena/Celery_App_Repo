# path/to/your/proj/cfehome/__init__.py
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app  # noqa
# from __future__ import absolute_import, unicode_literals

__all__ = ('celery_app',)