""" Generic mail sending functions """

from flask_mail import Message
from app import mail, app
from flask import render_template
from config import ADMINS
from .decorators import async


def follower_notification(followed, follower):
    follow_sub = "[microblog] %s is now following you!" % follower.nickname
    send_email(follow_sub, ADMINS[0],
               [followed.email],
               render_template('follower_email.txt',
                               user=followed, follower=follower),
               render_template('follower_email.html',
                               user=followed, follower=follower))


@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html_body = html_body
    send_async_email(app, msg)


