构建镜像

```bash
docker build -t memcached:rockylinux8 .
```



启动镜像

```bash
docker run -d -p 11211:11211 memcached:rockylinux8
```

```bash
docker run -d -p 11211:11211 --name "memcached" memcached:rockylinux8
```

