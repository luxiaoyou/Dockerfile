FROM rockylinux:8

MAINTAINER Bruce Lu <bruce.lu@luxiaoyou.com>

RUN dnf update -y \
    && dnf install memcached -y \
    && dnf clean all

EXPOSE 11211

CMD ["memcached", "-u", "daemon"]