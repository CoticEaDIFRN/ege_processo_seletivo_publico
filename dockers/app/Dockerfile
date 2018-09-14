FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && \
    apk add postgresql-libs && \
    apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev && \
    pip install psycopg2-binary && \
    apk --purge del .build-deps gcc python3-dev musl-dev postgresql-dev

RUN addgroup -g 1000 app && adduser -D -H -s none -u 1000 -G app app

ADD startup.sh . 

ADD requirements-build.txt . 
RUN pip install -r requirements-build.txt

WORKDIR /apps/app

CMD /startup.sh

