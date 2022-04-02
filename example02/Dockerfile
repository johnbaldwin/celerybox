
# -- Define our base image
#
# https://pythonspeed.com/articles/base-image-python-docker-images/
# For performance, recommends using Ubunto 20.04 image, although may be some
# more hassle getting set up
FROM python:3.9-buster

# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
# If this is set to a non-empty string it is equivalent to specifying the -u option.
# Send output to the console
ENV PYTHONBUFFERED=1

# https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE
ENV PYTHONDONTWRITEBYTECODE=1

# Copy specified host contents into the docker image
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY ./example02_app /app/example02_app

WORKDIR /app

ENTRYPOINT celery -A example02_app worker -l INFO
