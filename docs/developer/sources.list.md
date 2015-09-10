<!--Meta
category:系统开发
title:源列表测试说明
DO NOT Delete Meta Above -->

## 源列表说明
文档所述`软件源`和`软件仓库`并无实质区别，具体表现都是通过`deb ${url} ${dist} ${sections}`体现

软件源文件存放于 `/etc/apt/sources.list` 及 `/etc/apt/sources.list.d/`下

#### 2015 默认源列表
```
deb http://cache.mirrors.deepin.org unstable main contrib non-free
```
`cache.mirrors.deepin.org`实现工作机制这里不作阐述，在公司内部使用与使用`packages.corp.linuxdeepin.com`并无区别，简而言之， 类似与`deb http://cache.mirrors.deepin.org unstable main`与`deb http://packages.corp.linuxdeepin.com/deepin-2015 unstable main` 结果上是一模一样的

* debian ci merge 测试项目请添加` deb http://pools.corp.linuxdeepin.com/experimental experimental main `进行测试
> `experimental`由于开发组未使用tag标记软件发布版本，所以需要添加这个软件源来安装deepin软件，可预见的未来这个dist作为测试使用，发布版本（release）不使用该dist

* debian tag 测试请添加` deb http://packages.corp.linuxdeepin.com/deepin-2015 unstable main contrib non-free `进行测试

* 软件源` deb http://packages.corp.linuxdeepin.com/deepin-2015 stable main contrib non-free ` 目前无软件，故无需测试

#####目前2015使用源列表
```
deb http://cache.mirrors.deepin.org unstable main contrib non-free
```

注意：目前下列软件列表不再默认使用
```
deb http://cache.mirrors.deepin.org experimental main 
```
 

**请注意，除测试或者追新等特定需求外，这两个源不要一起使用，因为`experimental`软件版本会比`unstable`更新，导致使用的是`experimental`仓库软件包**

#### cdn 软件软件源列表

```
deb http://cdn.packages.linuxdeepin.com/packages-debian unstable main contrib non-free
```

下列软件源默认不使用
```
deb http://cdn.packages.linuxdeepin.com/packages-debian experimental main 
```

#### 2014.3 默认源列表

```
deb http://mirrors.corp.linuxdeepin.com/ubuntu trusty main universe multiverse restricted
deb http://mirrors.corp.linuxdeepin.com/deepin trusty main universe non-free
```

不通过ci 测试请添加 ` deb http://packages.corp.linuxdeepin.com/deepin trusty main universe non-free`进行测试 (dra-chromium)

~~2014.3 ci merge 测试项目请添加` deb http://pools.corp.linuxdeepin.com/testing/2014 trusty main `进行测试~~

请注意，通过`/etc/hosts`将`packages.linuxdeepin.com`指向`10.0.0.6`的效果和使用`mirrors.corp.linuxdeepin.com`效果一致


## 各个仓库同步关系
* `pools.corp.linuxdeepin.com/*`软件仓库简称为`pools`仓库
* `packages.corp.linuxdeepin.com/*`软件仓库简称为`release`仓库

####具体同步过程
1. 系统组维护多个`pools.corp.linuxdeepin.com/*`软件仓库，该仓库是原始仓库，性质类似与ubuntu中的ppa
2. 每个`release`仓库由`pools.corp.linuxdeepin.com`中几个合并而成，该操作定期由脚本或者手动等方式进行
3. `release`仓库通过定时任务向`packages.linuxdeepin.com`服务器进行同步
4. 目前`cdn`服务器由360定期从`packages.linuxdeepin.com`进行同步

通过上述流程描述:
各个仓库软件更新时间及版本存在一定差异，这是由于各个仓库职能范围及机制所限制

####开发/测试组注意:
1. `pools`仓库软件最快得到更新，针对某个软件测试大部分情况使用特定`pools`仓库
2. `release`仓库本身为完整仓库，针对系统完整性或者仓库完整性测试使用`release`仓库
3. 外网测试使用`packages.linuxdeepin.com`软件源
4. `cdn`软件源为360维护，除非特定测试`cdn`任务，一般来说测试无需使用`cdn`仓库
5. 各个软件仓库请尽量不要混用，尤其是`pools`仓库

## 软件branch推送说明

`pkg_debian`项目通过分支实现将生成二进制软件包推送至不同仓库

* 分支 `debian` 推送至软件源 ` deb http://pools.corp.linuxdeepin.com/experimental experimental main `
* 分支 `2014` 推送至软件源 ` deb http://pools.corp.linuxdeepin.com/testing/2014 trusty main `

>*TODO: `pkg_debian`项目下`branch.json`里面有`repo`值，该值未来会作为仓库地址使用*

