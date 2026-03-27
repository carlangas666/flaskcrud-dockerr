FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask flask-mysqldb python-dotenv mysqlclient

ENV FLASK_APP=app/main.py

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]