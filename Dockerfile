FROM python:3.11

RUN mkdir /app
COPY ./src /app
COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

CMD ["unicorn", "main:app", "--host", "0.0.0.0", "--port", "$PORT"]