"""tasks module
"""
from example01_app.celery import app


@app.task
def add(x, y):
    print('task: add {} + {}'.format(x, y))
    return x + y
