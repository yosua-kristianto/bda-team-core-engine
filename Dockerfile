FROM python:3.11.6-bookworm

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["PYTHONDONTWRITEBYTECODE=1", "python", "ml_instance_service/src/main/main.py", "--spark=no"]