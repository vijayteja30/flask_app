From python:3.8-slim-buster

RUN mkdir -p /home/flask_app

WORKDIR /home/flask_app

COPY requirements.txt requirements.txt

COPY ./flask_app /home/flask_app

RUN pip3 install -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
