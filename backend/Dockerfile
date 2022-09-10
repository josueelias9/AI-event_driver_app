FROM python:3.8

# update y upgrade base image
RUN apt-get update && \
    apt-get upgrade -y

# this will be the path where we will be working
WORKDIR /usr/src/app

# create backend folder
RUN mkdir backend

# go in...
WORKDIR /usr/src/app/backend

# lets copy everything that is inside our backend folder  to our container (consider the files ignored in our Dockerfile)
COPY . .

# install venv, activate venv, and install requirements
RUN python3 -m venv venv && \
    /bin/bash -c 'source ./venv/bin/activate' && \
    pip3 install -r requirements.txt

# go to the project file
WORKDIR /usr/src/app/backend/project

# this is the port of the container (when created)
EXPOSE 8000

# run server
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000" ]