<!--Meta
category:系统开发
title:branchs.json文件结构
DO NOT Delete Meta Above -->

### 文件示例
#### branchs.json示例

```
{
    "repo": "http://packages.corp.linuxdeepin.com/deepin-2015",
    "default":"develop",
    "base_version": "15.06",
    "dist": "unstable",
    "packages":[
    {
        "pkg": "dae",
        "git": "https://cr.deepin.io/dae",
        "branch": "develop"
    },
    {
        "pkg": "dde-workspace",
        "packagename": "deepin-desktop-environment",
        "git": "https://cr.deepin.io/dde-workspace",
        "branch": "master",
        "base_version": "2.1"
    }
    ]
}
```

#### builder.conf示例

```
[build]
upstreamer_basedir = *
debian_basedir = *
notify = 0
json_config = branchs.json

[repo]
host = *

[source]
method = *
dest = *
```

### branchs.json 各个字段分析
branchs.json 为json格式文件

#### 主要字段

该字段为仓库维护者修改，单个package请修改或者添加对应packages字段

 - repo: 代表对应仓库的url链接，为仓库维护者填写字段，编译机器并未使用该值
 - default: 默认打包分支
 - base_version: 默认软件版本号
 - dist: 打包软件发行版本代号

#### packages字段

软件开发请至少添加一下内容

 - pkg: 对应软件名称
 - packagename: 对应软件debian目录下名称，参考dde-workspace
 - git: 获取代码地址

支持自定义字段
 - branch: 覆盖主要字段对应默认branch
 - base_version: 覆盖主要字段对应base_version

### builder.conf 各个字段分析
builder.conf 为ini格式文件,如需修改请通知系统开发人员
文档会在编译服务中说明

### 修订历史
* 第一次提交 @ 2015年06月08日14:44:45 leaeasy:
 - branchs.json 文件示例
 - builder.conf 文件示例
