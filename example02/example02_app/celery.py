"""The Celery worker module
"""
import os
from celery import Celery

BROKER_HOST = os.environ.get('BROKER_HOST', 'localhost')
BROKER_URL = 'amqp://admin:admin@{host}:5672/'.format(host=BROKER_HOST)

app = Celery('test_celery',
             broker=BROKER_URL,
             backend='rpc://',
             include=['example02_app.tasks'])
