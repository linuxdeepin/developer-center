<!--Meta
category:文档服务
title:gerrit使用
DO NOT Delete Meta Above -->

#gerrit使用流程

##基本信息
开发者围绕git+gerrit这套系统进行代码合作开发与质量审核。使用jenkins作为continuous integration工具辅助监督整个项目的质量。 

### gerrit服务器信息
[https://cr.deepin.io](https://cr.deepin.io)

cr = code review

### jenkins服务器信息
[https://ci.deepin.io](https://ci.deepin.io)

ci = continuous integration


## gerrit注册
目前cr使用[github](https://github.com)账号进行认证。使用前请先配置好github的基本信息,包括

   * 邮箱地址
   * ssh-publickey

完成github基本信息配置后(可以正常从github push/pull自己的任意项目)。进入配置[导入](https://cr.deepin.io/plugins/github-plugin-2.10-SNAPSHOT/static/account.html)页面，点击*Next*按钮将github的配置信息导入到cr里。(成功后进入一个空白页面，不会有任何提示)



## gerrit使用
* 工具安装
  apt-get install git-review 安装review工具
* 基本配置
  创建~/.config/git-review/git-review.conf这个文件，并写入以下内容
```
[gerrit]
defaultremote = origin
```
* 本地仓库克隆
  进入[项目列表](https://cr.deepin.io/#/admin/projects/)页面，查找需要的项目.
  点击复制拷贝命令后在终端下拉取代码 ![](docs/guide/git-clone.png)

* 详细的使用文档请阅读[官方文档](https://cr.deepin.io/Documentation/index.html)



git-review工具目前有bug导致非英文locale的系统无法使用。出现这类问题请使用
LANGUAGE=en_US.UTF-8 git review 进行替换，或者手动修改/usr/bin/git-review的代码,修改方式谁来补充 :)
