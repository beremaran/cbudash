FROM python:3.6
MAINTAINER Berke Arslan <berke@beremaran.com>

WORKDIR .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update
RUN apt-get -y install nodejs
RUN apt-get -y autoremove
RUN npm install
RUN npm run build

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - --reload app