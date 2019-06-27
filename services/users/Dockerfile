# base image
#FROM python:3.7.2-alpine
FROM python:3.7.2-stretch

RUN apt-get update && apt-get install netcat-openbsd

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./requirements-dev.txt /usr/src/app/requirements-dev.txt
RUN pip install -r requirements-dev.txt

# new
# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . /usr/src/app

# run server
CMD ["/usr/src/app/entrypoint.sh"]