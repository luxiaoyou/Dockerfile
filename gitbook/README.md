# Dockerfile

#### 使用
```
mkdir book
cd book

初始化gitbook
docker run --rm -v $PWD:/var/gitbook_home gitbook:8-alpine gitbook init

mkdir book_html

构建gitbook
docker run --rm -v $PWD:/var/gitbook_home -v $PWD/book_html:/var/gitbook_src gitbook:8-alpine gitbook build . /var/gitbook_src

或者

端口映射访问(调试用)
docker run -d -p 4000:4000 -v $PWD:/var/gitbook_home gitbook:8-alpine gitbook serve
```
