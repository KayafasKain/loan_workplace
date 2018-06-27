import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loan_workplace.settings')

app = Celery('mail_celery')
app.config_from_object('django.conf:settings')


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'publisher.tasks.send_view_count_report',
        'schedule': crontab(hour=12, minute=30, day_of_month='24'),
    },
}