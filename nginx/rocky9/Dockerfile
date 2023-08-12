FROM rockylinux:9

MAINTAINER Bruce Lu <bruce.lu@luxiaoyou.com>

RUN dnf update -y \
    && dnf install nginx -y \
    && dnf clean all

COPY nginx/nginx.conf /etc/ngnix/nginx.conf
COPY nginx/conf.d /etc/nginx/conf.d
COPY nginx/default.d /etc/nginx/default.d

COPY html  /usr/share/nginx/html

EXPOSE 80
USER nginx

CMD ["nginx", "-g", "daemon off;"]