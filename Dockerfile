FROM python:3.9-alpine3.13
LABEL maintainer="gradly.com"

ENV PYTHONUNBUFFERED 1

COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk update && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev jpeg-dev zlib-dev musl-dev linux-headers && \
    /py/bin/pip install -r /app/requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app && \
    mkdir -p /vol/web/static && \
    mkdir -p /vol/web/media && \
    chown -R app:app /vol && \
    chmod -R 755 /vol && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER app

CMD ["run.sh"]