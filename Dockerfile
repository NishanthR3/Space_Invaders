FROM debian:jessie-slim

WORKDIR /usr/src/app/

COPY . .

RUN apt-get update && apt-get install -y python3 build-essential python3-pip python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev \
libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion \
libportmidi-dev libfreetype6-dev libavformat-dev libswscale-dev mercurial && pip3 install hg+http://bitbucket.org/pygame/pygame