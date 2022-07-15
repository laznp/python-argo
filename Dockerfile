FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app
COPY . .
EXPOSE 5000
CMD ["python","app.py"]
