from celery import Celery

celery_app = Celery(
    'apps',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
)

celery_app.conf.update(
    task_routes={
        'apps.tasks.send_email': {'queue': 'email'},
    }
)