from flask import render_template
from flask_mail import Message

from app import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg: Message = Message(
        subject=subject,
        sender=sender,
        recipients=recipients
    )
    msg.body = text_body
    msg.html = html_body
    print(mail.state.server)
    mail.send(msg)


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Flask app] Reset Your Password',
               sender='flask-blog@administrator.com',
               recipients=[user.email],
               text_body=render_template('email/pwd_reset.txt', user=user, token=token),
               html_body=render_template('email/pwd_reset_msg.jinja2', user=user, token=token))
