FROM python:3.7-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["gunicorn"]
CMD ["-w", "2", "-b", "0.0.0.0:8000", "blog:create_app()"]