构建镜像

```bash
docker build -t nginx:rockylinux8 .
```

```bash
docker build -t <username>/nginx:rockylinux8 .
```

启动容器

```bash
docker run -d -p 80:80 nginx:rockylinux8
```

测试

```bash
> curl http://localhost
hello
```

