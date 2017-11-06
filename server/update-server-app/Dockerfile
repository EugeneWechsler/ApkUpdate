FROM python:2.7-alpine3.6
MAINTAINER Eugene Wechsler "<eugenewechsler@gmail.com>

ENV SUPERVISOR_VERSION=3.3.1
ENV PYTHONPATH=$PYTHONPATH:/update-server/

ENV APK_PACKAGES=/packages
ENV LOGS=/var/log
ENV SUPERVISOR_PROCESSES=4
ENV SUPERVISOR_START_PORT=13000

RUN apk update && apk add gcc python-dev libzip-dev jpeg-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl

ADD supervisor/supervisord.conf /etc/supervisord.conf
ADD src/update-server.py /update-server/update-server.py
RUN chmod 755 /update-server/update-server.py
ADD ./requirements.txt /update-server/
ADD ./Docker_entry.sh /Docker_entry.sh

WORKDIR /update-server

RUN pip install -r requirements.txt

RUN pip install supervisor==$SUPERVISOR_VERSION

#ENTRYPOINT ["python", "update-server.py"]
ENTRYPOINT ["sh", "/Docker_entry.sh"]
