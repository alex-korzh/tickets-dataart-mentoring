from flask_mail import Message

from main import mail


def send_verification_email(email: str, code: str):
    msg = Message('Код для авторизации пользователя', sender='admin@mailtrap.io', recipients=[email])
    msg.body = code
    mail.send(msg)
