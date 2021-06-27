FROM python:3.8.10

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD [ "python", "manage.py", "runserver" ]
