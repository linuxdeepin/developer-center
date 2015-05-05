.PHONY : test

TARGET=docs.deepin.io
CURDIR=$(shell pwd)
FIXGOPATH=$(CURDIR):$(GOPATH)
BIN_PATH=$(CURDIR)

SERVICE_SRC=$(CURDIR)/server

ifndef USE_GCCGO
    GOBUILD = go build
else
    LDFLAGS = $(shell pkg-config --libs gio-2.0)
    GOBUILD = go build -compiler gccgo -gccgoflags "${LDFLAGS}"
endif

build:
	cd $(SERVICE_SRC)  && GOPATH=$(FIXGOPATH) ${GOBUILD} -o $(BIN_PATH)/$(TARGET)
