FROM python:3.13

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app
COPY alembic alembic
COPY alembic.ini alembic.ini
COPY start.sh /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]
