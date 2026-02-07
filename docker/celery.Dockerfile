FROM python:3.13

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app

CMD ["celery", "-A", "app.workers.celery_app.celery_app", "worker", "-Q", "default", "--loglevel=info"]
