FROM python:3.8.5

WORKDIR /app

RUN pip3 install requests

COPY . .

CMD [ "python3", "asignacion7.py" ]
