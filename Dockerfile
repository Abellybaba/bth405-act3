FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install mysql-connector-python

#Expose the application port
#EXPOSE 8010

CMD ["python", "api/server.py"]
