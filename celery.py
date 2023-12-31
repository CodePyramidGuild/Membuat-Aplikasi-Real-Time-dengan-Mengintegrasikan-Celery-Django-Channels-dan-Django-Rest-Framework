from celery import Celery
from django.conf import settings

app = Celery('my_realtime_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
