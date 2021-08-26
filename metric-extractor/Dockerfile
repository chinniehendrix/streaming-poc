FROM python:3.9.5-alpine3.13
RUN apk add build-base

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["faust", "-A", "extractor", "worker"]