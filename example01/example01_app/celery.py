from celery import Celery

BROKER_URL = 'amqp://admin:admin@localhost:5672/'

app = Celery('test_celery',
             broker=BROKER_URL,
             backend='rpc://',
             include=['example01_app.tasks'])
