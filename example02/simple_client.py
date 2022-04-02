"""First example app calling a Celery task

To read more about results, see here:

* [celery.result](https://docs.celeryproject.org/en/stable/reference/celery.result.html)
"""
from example02_app.tasks import add


def simple_run():
    print('calling "add" task')
    result = add.delay(4, 5)
    print('waiting up to 10 seconds for the result...')
    result.wait(10)
    if result.successful():
        print('Success! result = {}'.format(result.result))
    else:
        print('Hmm, not successful. Status: {}'.format(result.status))


if __name__ == '__main__':
    simple_run()
