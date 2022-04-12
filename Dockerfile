# /server/Dockerfile
FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /server
ADD . /server

WORKDIR /server

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN python3 manage.py migrate --settings=soul_prj.settings.deploy
RUN python3 manage.py collectstatic --settings=soul_prj.settings.deploy

EXPOSE 8000
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "soul_prj.wsgi.deploy:application"]