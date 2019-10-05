FROM node:8-alpine

LABEL Bruce Lu "luxiaoyou.com@gmail.com"

ENV WORKPLACE_DIR=/var/gitbook_home
ENV SRC=/var/gitbook_src

VOLUME $SRC
WORKDIR $WORKPLACE_DIR

RUN npm install -g gitbook-cli

EXPOSE 4000