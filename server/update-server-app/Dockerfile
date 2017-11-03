FROM python:2.7-alpine3.6
MAINTAINER Eugene Wechsler "<eugenewechsler@gmail.com>

RUN apk update && apk add gcc python-dev libzip-dev jpeg-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl

ADD src/update-server.py /update-server/update-server.py
ADD ./requirements.txt /update-server/

WORKDIR /update-server

RUN pip install -r requirements.txt

ENV PYTHONPATH=$PYTHONPATH:/update-server/

ENV TORNADO_PORT=8888
ENV APK_PACKAGES=./packages

ENTRYPOINT ["python", "update-server.py"]
