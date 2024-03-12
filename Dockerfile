### First stage
FROM python:3

RUN mkdir /app
WORKDIR /app
ADD . /app/

RUN pip install flask flask_sqlalchemy
#RUN python3 -m venv venv

EXPOSE 5000
CMD [ "python", "./bookmanager.py" ]
