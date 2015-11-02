<!--Meta
category:系统开发
title:软件仓库及pools对应关系
DO NOT Delete Meta Above -->


# 2015/10/27 会议记录

> 计划还会添加一个`合并测试源`以减轻`pools`磁盘消耗，目前`合并测试源`与`内部测试源`除url地址不一样外，内容完全一致，所以并不会引起任何问题。

内部使用源列表
--------------------
* http://mirrors.corp.linuxdeepin.com/2015 内部测试源(unstable/experimental)
* http://pools.corp.linuxdeepin.com/deepin 合并测试源(unstable/experimental)
* http://pools.corp.linuxdeepin.com/debian debian同步源(unstable)
* http://pools.corp.linuxdeepin.com/experimental CodeMerge源(experimental)
* http://pools.corp.linuxdeepin.com/maintain Tag发布源(unstable)
* http://pools.corp.linuxdeepin.com/universe 系统组维护源(unstable)
* http://pools.corp.linuxdeepin.com/ppa/* 项目特殊源

> 1. 目前`内部测试源`与`合并测试源`一致，未来`内部测试源`会使用一个更合理的地址，并与`合并测试源`进行分离，一般可以认为`合并测试源`通过测试后会向`内部测试源`进行同步更新
> 2. 其他软件源应具体需求进行添加，无需全部添加
> 3. `pools.corp.linuxdeepin.com`软件源大部分工作流程都是作为附加源，依附在内部测试源进行工作。一般应用/体验，直接使用内部测试源即可，无需添加任何`pools.corp.linuxdeepin.com`的软件源

Code Review 流程
---------------------
1. **开发**提交cr至[Code Review](https://cr.deepin.io)平台
2. **CI(jenkins/lxc-builder)**负责自动打包，build +1/-1
3. **测试**下载对应软件包安装测试 测试 +1/-1
4. **开发**代码合并到对应代码仓库

__软件源__
```
deb http://mirrors.corp.linuxdeepin.com/2015 unstable main contrib non-free
deb http://pools.corp.linuxdeepin.com/experimental experimental main
```

>期间测试过程大部分问题，主要由开发与测试之间沟通解决，系统组协助。CI配置问题导致打包失败等问题由系统组负责

Commit Merge 工作流程
------------------------
1. **开发** 将代码合并到对应代码仓库
2. **系统** [BuildBot](http://10.0.0.8:9998)自动拉取最新代码打包并推入__expermintal__仓库
3. **测试/开发** 进行升级测试

__软件源__
```
deb http://mirrors.corp.linuxdeepin.com/2015 unstable main contrib non-free
deb http://pools.corp.linuxdeepin.com/experimental experimental main
```
> 期间测试过程大部分问题，主要由开发组与测试组之间沟通解决。BuildBot由于配置问题导致打包失败等问题由系统组负责。

Tag Source 工作流程
--------------------------
1. **开发/产品** 对稳定代码进行tag
2. **系统** [BuildBot](http://10.0.0.8:9998)获取对应Tag代码进行生成、编译、推送到__maintain__仓库
3. **开发/测试/系统**进行升级测试
4. 测试若出现问题，可有以下解决方案：
   - 系统组对代码进行patch，debian/patch依旧产生对应commit会在下一个tag发布版集成
   - 开发组升级tag版本，重新通过cr,merge流程提交新tag

__软件源__
```
deb http://mirrors.corp.linuxdeepin.com/2015 unstable main contrib non-free
deb http://pools.corp.linuxdeepin.com/maintain unstable main
```

> 期间测试过程出现问题，测试组只需与系统组进行沟通解决。实质为代码问题由系统组与开发组共同解决，编译问题由系统组解决。

ISO自动测试(openQA)流程
----------------
该流程主要目的为测试官方更新与Deepin维护软件仓库的兼容性、稳定性。
1. **测试** OpenQA平台使用某ISO使用对应软件源进行测试，并将测试结果反馈于 **系统** [*目前通过邮件sysdev@linuxdeepin.com通知*]
2. **系统**对测试结果进行评估修正，并反馈工作状态
3. 当天**系统**若修正完成，通知**测试**进行新一轮测试。若无法修正完成，则直接等待下一次自动测试结果重新评估修正

__软件源__
```
deb http://pools.corp.linuxdeepin.com/debian unstable main contrib non-free
deb http://pools.corp.linuxdeepin.com/maintain unstable main contrib non-free
deb http://pools.corp.linuxdeepin.com/universe unstable main contrib non-free
```

仓库更新测试/仓库推送
---------------------
该流程主要目的为对不适合使用自动测试流程进行的任务进行人工干预。包括软件细节不一致/字体差异等问题。系统组推送外网更新特别依赖与测试提供测试报告。

1. ISO自动测试成功后，**系统**根据各个维护源，按需生成[合并测试源](http://pools.corp.linuxdeepin.com/deepin)
2. **测试** http://pools.corp.linuxdeepin.com/maintain unstable main使用[合并测试源](http://pools.corp.linuxdeepin.com/deepin)进行测试
3. **测试**将测试结果通知**系统**,测试成功,**系统**更新内部测试源，不成功便放弃更新
4. **测试**对内部测试源进行验证，验证成功** 系统**产生对应release存档,推送外网更新
5. **系统** 就更新内容发送邮件至涉及到**开发/测试/产品/系统**等

需要按顺序测试软件源
```
deb http://pools.corp.linuxdeepin.com/deepin unstable main contrib non-free
```
```
deb http://mirrors.corp.linuxdeepin.com/2015 unstable main contrib non-free
```

特殊软件集成测试
---------------------------
特殊项目会通过建立ppa方式进行测试，比如目前的dstore项目。只需要测试使用项目对应ppa进行更新测试，测试环境源配置`需且只需`如下形式
```
deb http://mirrors.corp.linuxdeepin.com/2015 unstable main contrib non-free
deb http://pools.corp.linuxdeepin/ppa/${Name} ${Dist} main
```

神威/龙芯移植
-----------------------
目前还是按移植部门工作流程
待deepin 2015代码稳定tag后，不再使用 `experimental`仓库代码，而使用如下地址获取`unstable`对应源代码中进行移植
```
http://pools.corp.linuxdeepin.com/deepin
```

DDE-NEXT安装体验
----------------------------
如有安装体验DDE-NEXT环境等需求，按如下软件源配置并安装`dde-next`即可
```
deb http://mirrors.corp.linuxdeepin.com/2015 unstable main contrib non-free
deb http://mirrors.corp.linuxdeepin.com/2015 experimental main contrib non-free
```

特殊软件集成测试
---------------------------
特殊项目会通过建立ppa方式进行测试，比如目前的dstore项目。只需要测试使用项目对应ppa进行更新测试，测试环境源配置`需且只需`如下形式
```
deb http://mirrors.corp.linuxdeepin.com/2015 unstable main contrib non-free
deb http://pools.corp.linuxdeepin/ppa/${Name} ${Dist} main
```
执行命令`apt-get update;apt-get dist-upgrade; apt-get install dde-next`


每日构建ISO测试
------------------------------
**测试** 通过PXE测试2015每日构建的ISO，具体工作内容由测试补全。5. **系统** 就更新内容发送邮件至涉及到**开发/测试/产品/系统**等

__使用软件源__
```
deb http://mirrors.corp.linuxdeepin.com/2015 unstable main contrib non-free
```
