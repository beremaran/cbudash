FROM python:3.6
MAINTAINER Berke Arslan <berke@beremaran.com>

ENV INSTALL_PATH /code/
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY requirements.txt $INSTALL_PATH
RUN pip install -r requirements.txt
COPY . $INSTALL_PATH

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get update
RUN apt-get -y install nodejs
RUN apt-get -y autoremove
RUN npm run build

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - --reload app