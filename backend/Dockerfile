FROM python:3.11.0

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
        libatlas-base-dev nginx supervisor

RUN pip3 install uwsgi

COPY ./requirements.txt /project/requirements.txt

RUN pip3 install -r /project/requirements.txt

RUN useradd --no-create-home nginx

RUN rm /etc/nginx/sites-enabled/default
RUN rm -r /root/.cache

COPY webserver-config/nginx.conf /etc/nginx/
COPY webserver-config/flask-site-nginx.conf /etc/nginx/conf.d/
COPY webserver-config/uwsgi.ini /etc/uwsgi/
COPY webserver-config/supervisord.conf /etc/

COPY . /project

WORKDIR /project

CMD ["/usr/bin/supervisord"]
