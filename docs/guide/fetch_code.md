<!--Meta
category: 开发环境
title: 获取"国际化"的代码
DO NOT Delete Meta Above -->

"国际化"代替"明敢词"

代码拉取过程中经常遇到“国际化”问题，导致在不使用VPN的时候无法获取到代码。

对于偶尔使用的同学可以设置以下参数，能够解决大部分“国际化”问题。
但请注意这里的方式只适合少量开发类的网站.

~/.zshrc || ~/.bashrc 中增加
```
export http_proxy=http://hx.gy:1080
```

~/.gitconfig 中增加
```
[http]
    proxy = http://hx.gy:1080
```

~/.hgrc 中增加
```
[http_proxy]
host = http://hx.gy:1080
```

~/.subversion/servers　中增加
```
[global]
http-proxy-host = hx.gy
http-proxy-port = 1080
http-proxy-compression = no
```

此代理是由[hx](http://honx.in/i/Unzt3YKo13ewFpvO)提供的开发人员专用的免费动态线路
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
这里面的域名会通过代理线路，其他域名会使用正常速度的服务器。
