FROM python:3.12-alpine

WORKDIR /app

COPY docker_test.py /app

ENTRYPOINT ["python", "docker_test.py"]
