FROM ubuntu:16.04

WORKDIR /home/support/otus
RUN apt-get clean && apt-get update
RUN apt-get upgrade -y && \
    apt-get install -y git

# Install OpenJDK-8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y ant && \
    apt-get clean;

# Fix certificate issues
RUN apt-get update && \
    apt-get install ca-certificates-java && \
    apt-get clean && \
    update-ca-certificates -f;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

RUN git clone https://github.com/donnerjack027/otus-hw5.git
RUN apt-get -y install python3-pip
RUN pip3 install -r /home/support/otus/otus-hw5/requirements.txt

RUN chmod -R +x /allure-2.6.2/bin

ENV PATH="/allure-2.6.2/bin:${PATH}"
RUN export PYTHONPATH="$PYTHONPATH:/home/support/otus/otus-hw5"
