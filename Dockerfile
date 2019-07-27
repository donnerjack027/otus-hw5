FROM ubuntu:16.04

WORKDIR /home/support/otus
RUN apt-get clean && apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y git
RUN git clone https://github.com/donnerjack027/otus-hw5.git
RUN apt-get -y install python3-pip
RUN pip3 install -r /home/support/otus/otus-hw5/requirements.txt
RUN export PYTHONPATH="$PYTHONPATH:/home/support/otus/otus-hw5"
