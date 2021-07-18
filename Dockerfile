FROM python:3.8.3-alpine
WORKDIR /home/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /home/app
RUN pip install -r requirements.txt
COPY ./testapp /home/app

EXPOSE 8080

CMD ["python", "manage.py","runserver","0.0.0.0:8080"]
