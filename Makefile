.PHONY : test

CURDIR=$(shell pwd)
VENDOR=$(CURDIR)/_vendor
GOPATH=$(VENDOR)
GOBIN=$(VENDOR)/bin
GOM=$(GOBIN)/gom

build:
	env GOPATH=$(VENDOR) $(GOM) build -v

po:
	cd $(CURDIR); xgettext --package-name=deepinid-oauth --package-version=0.1.0 -d oauth -s `find  rest view  -name "*.go" -o -name "*.tpl"` -o lang/oauth.pot -L c++ -i --keyword=gettext --keyword=Gettext
	[ -d $(CURDIR)/lang/zh/LC_MESSAGES ] || mkdir -p $(CURDIR)/lang/zh/LC_MESSAGES
	if [ -e $(CURDIR)/lang/zh/LC_MESSAGES/oauth.po ]; then\
		cd $(CURDIR)/lang; msgmerge --lang=zh zh/LC_MESSAGES/oauth.po oauth.pot -o zh/LC_MESSAGES/oauth.po;\
	else\
		cd $(CURDIR)/lang; msginit --l zh -o zh/LC_MESSAGES/oauth.po -i oauth.pot;\
	fi

mo:
	cd $(CURDIR)/lang/zh/LC_MESSAGES; msgfmt -c -v -o oauth.mo oauth.po

clean:
	rm -rf _vendor/pkg/

update:
	env GOPATH=$(VENDOR) GOBIN=$(VENDOR)/bin go get github.com/Iceyer/gom
	env PATH=$(GOBIN):$(PATH) $(GOM) install -v

