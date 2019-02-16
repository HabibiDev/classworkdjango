from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# встановлюємо стандартні Django налаштування для celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coocking.settings')
app = Celery('coocking')

# Використвуємо строку для того, щоб воркер не приховав об'єкт при використанні Windows
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))