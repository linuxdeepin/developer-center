<!--Meta
category: 开发环境
title: 获取"国际化"的代码
DO NOT Delete Meta Above -->

"国际化"代替"明敢词"
代码拉取过程中经常遇到“国际化”问题，导致在不使用VPN的时候无法获取到代码。

请大家补充*方便*、*稳定*的方式


#hx.gy (http_proxy)
此代理是由[hx](http://honx.in/i/Unzt3YKo13ewFpvO)提供的开发人员专用免费线路，

对于偶尔使用的同学可以设置以下参数，能够解决大部分“国际化”问题。

##设置方式

###常见工具
大部分命令行工具支持http_proxy命令 使用的时候在命令行前加上http_proxy的
环境变量即可。
```
http_proxy=http://hx.gy:1080 wget/curl

or

export http_proxy=http://hx.gy:1080
wget balabala
curl balabala
```

###git
~/.gitconfig 中增加
```
[http]
    proxy = http://hx.gy:1080
```

###hg
~/.hgrc 中增加
```
[http_proxy]
host = http://hx.gy:1080
```

###svn
~/.subversion/servers　中增加
```
[global]
http-proxy-host = hx.gy
http-proxy-port = 1080
http-proxy-compression = no
```

##支持的域名##
http_proxy方式无法做到动态切换，*所以不用的时要将上面哪些配置注释掉，避免影响正常使用*。

公益性免费代理,仅支持[以下域名](http://blog.honx.in/dev-only/)。
```
android.com
bitbucket.org
bintray.com
chromium.org
clojars.org
registry.cordova.io
dartlang.org
download.eclipse.org
github.com
githubusercontent.com
golang.org
googlesource.com
storage.googleapis.com
code.google.com
googlecode.com
dl.google.com
dl-ssl.google.com
getcomposer.org
gradle.org
gopkg.in
ionicframework.com
plugins.jetbrains.com
macports.org
maven.org
melpa.org
mendeley.com
www.nuget.org
npmjs.com
npmjs.org
pypi.python.org
packagist.org
packagecontrol.io
rubygems.org
repo.typesafe.com
```


#GoAgent

#Deepin内网VPN服务
