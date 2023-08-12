构建镜像

```bash
docker build -t nginx:rockylinux9 .
```

```bash
docker build -t <username>/nginx:rockylinux9 .
```

启动容器

```bash
docker run -d -p 80:80 nginx:rockylinux9
```

测试

```bash
> curl http://localhost
hello
```

