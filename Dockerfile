FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask flask-mysqldb python-dotenv mysqlclient

ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8081

CMD ["python", "app/main.py"]