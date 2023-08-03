from celery import shared_task
import time

@shared_task
def long_running_task(task_name):
    time.sleep(5)
    return f'{task_name} completed successfully.'
