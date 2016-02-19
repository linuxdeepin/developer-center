FROM alpine-python-golang

RUN pip install mkdocs

RUN mkdir -p /root/golang
ENV GOPATH=/root/golang
ADD server/_vendor /root/golang
ADD . /var/www/docs.deepin.io

WORKDIR /var/www/docs.deepin.io

RUN go get github.com/iceyer/gom
RUN make
RUN make update-cache

CMD ["./docs.deepin.io"]
