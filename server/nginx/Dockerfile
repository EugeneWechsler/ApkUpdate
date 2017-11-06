FROM nginx:alpine
MAINTAINER Eugene Wechsler "<eugenewechsler@gmail.com>"

RUN apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ADD nginx.conf.tmpl /etc/nginx/nginx.conf.tmpl
ADD Docker_entry.sh /Docker_entry.sh
ENTRYPOINT ["sh", "/Docker_entry.sh"]

CMD ["nginx", "-g", "daemon off;"]



