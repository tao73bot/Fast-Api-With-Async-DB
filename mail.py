from fastapi_mail import FastMail, ConnectionConfig, MessageSchema, MessageType
from config import settings
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

mail_config = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    # TEMPLATE_FOLDER=Path(BASE_DIR, "templates"),
)

mail = FastMail(mail_config)

def create_message(recipient: list[str],subject:str,body:str):
    message = MessageSchema(
        subject=subject,
        recipients=recipient,
        body=body,
        subtype="html"
    )
    return message