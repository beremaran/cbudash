FROM python:3.6
MAINTAINER Berke Arslan <berke@beremaran.com>
ENV INSTALL_PATH /code/
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY requirements.txt $INSTALL_PATH
RUN pip install -r requirements.txt
COPY . $INSTALL_PATH
CMD gunicorn -b 0.0.0.0:8000 --access-logfile - --reload app