from celery_worker import celery_app

@celery_app.task(name = "apps.tasks.send_email")
def send_email(subject:str, recipient:str, body:str):
    print("\n[Email Task]")
    print(f"To: {recipient}")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}\n")
    return "Email sent (simulated)"
    

celery_app.conf.update(
    task_routes={
        'apps.tasks.send_email': {'queue': 'email'},
    }
)