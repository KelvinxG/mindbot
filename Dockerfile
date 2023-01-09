FROM python:3.8-alpine
WORKDIR /MINDBOT
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask","run"]
