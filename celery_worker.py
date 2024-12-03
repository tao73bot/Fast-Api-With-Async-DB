from celery import Celery

celery_app = Celery(
    "apps",
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    broker_connection_retry_on_startup=True,
)

@celery_app.task()
def send_email(subject:str, recipient:str, body:str):
    print("\n[Email Task]")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}\n")
    return "Email sent (simulated)"

celery_app.register_task(send_email)