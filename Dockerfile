FROM ubuntu:20.04

WORKDIR ./workspace

COPY requirements.txt .
RUN apt-get update
RUN apt-get -y install vim
RUN apt-get -y install python3
RUN apt-get -y install pip
RUN apt-get -y install git
RUN pip3 install -r requirements.txt
RUN apt-get -y install jupyter

# ARG username=$user
# ARG password=$user
# RUN git clone https://username:password@github.com:Tishh95/tpForDocker.git
