# pull official base image
FROM python:3.9.10-slim-buster

# install system dependencies
RUN apt-get update && apt-get -y install curl && apt-get clean

# set working directory
WORKDIR /usr/src/app

# add api source code to working directory
COPY . /usr/src/app

# install python dependencies
RUN pip install -r requirements.txt

RUN chmod +x startup.sh
# run startup script
CMD ['./startup.sh']
