FROM ubuntu:18.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install firefox sudo wget curl jq python-pip cron at vim apache2 libapache2-mod-php

RUN service apache2 restart

RUN useradd -m developer -u 1000

RUN    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer 

USER developer

ENV HOME /home/developer

# RUN pip install pyinotify

# COPY scriptToDocker.sh scriptToDocker.sh

# CMD ./scriptToDocker.sh

