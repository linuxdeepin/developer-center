系统设计
========

TODO [\#A] WebHooks
-------------------

TODO 通用API规范
----------------

组件间的API目前包含 仓库(repository api) 和 商店API(appstore
API)。两者均遵守以下说明:
-   Logger
-   数据返回格式
-   Locales处理
-   权限验证

appstore-api (<http://appstore.api.deepin.test>)
------------------------------------------------

核心接口为两组

1.  橱窗(shopwindow)与商品(goods, e.g. applications,topics)
2.  排行榜(ratings)

### Applications

-   GET /applications

获取所有app的信息 注意:
1.  没有 `/applications/:id` 接口
2.  此接口返回的内容不包含app版本号,描述等信息。元数据请访问
    [repository](#repository)的[metadatas](#metadatas)接口

``` {.example}
[
{
    "id": "arduino",
    "package_id": "arduino",
    "banner": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/06/25/16-11-04-09ae4cca.jpeg",
    "slogan": " Let your Arduino circuit board “run”.",
    "locales": {
        "en_US": {
            "slogan": " Let your Arduino circuit board “run”."
        },
        "zh_CN": {
            "slogan": "让你的Arduino电路板“跑”起来。"
        }
    },
    "category": "development",
    "related_applications": [
        "gnome-sudoku",
        "arduino",
        "lyx",
        "planner"
    ],
    "last_modify_date": 0
},
...
]
```

### Topics

-   GET /topics
    -   topic作为个体存在时有其id、name和banner；
    -   topic作为容器存在时有其包含的apps以及背景相关的一些值;

``` {.example}
[
{
"id": 54,
"name": "Internet essential",
"description": "上网必备",
"background": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/01/10-32-09-c03197cc.tar.gz",
"background_color": "#000000",
"goods_name_color": "#ffffff",
"goods_category_color": "#787878",
"banner": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/01/10-30-30-4e1bd2bf.tar.gz",
"apps": [
    "ghex",
    "codeblocks",
    "abiword",
    "bluefish",
    "eclipse-platform",
    "arduino",
    "eric",
    "monodevelop",
    "codelite",
    "d-feet",
    "glade"
],
"locales": {
    "zh_CN": {
        "background": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/01/10-32-09-c03197cc.tar.gz",
        "background_color": "#000000",
        "goods_category_color": "#787878",
        "goods_name_color": "#ffffff",
        "name": "上网必备"
    }
}
},
...
]
```

### Shopwindows

-   GET /shopwindows

每一个shopwindow(橱窗)包含以下概念
-   type: slider、column、topic
    　通过type决定橱窗的外观样式，默认3种样式分别对应目前3种区域的概念.
-   name
-   goods: apps、topics 货品可以为app或者 **topic**

其中Goods本身抽象为
1.  cover:
    根据期望值设置不同的展示图。即使两个Goods有相同的type和id，其cover也不一定一样。　如Shopwindow为slider时，Goods的cover一般为横幅图，其他类型时则一般是小的banner图.
2.  type: 目前值可为application、topic
3.  id: 通过type和id可以找到此Goods对应的真实对象

``` {.example}
[
{
"id": "1",
"type": "slider",
"name": "默认slider",
"goods": [
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/22/09-48-53-2fbca471.tar.gz",
       "type": "application",
       "id": "aisleriot"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/23/17-11-26-a630d3e7.tar.gz",
       "type": "application",
       "id": "abiword"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/23/17-13-13-2b9516c1.tar.gz",
       "type": "application",
       "id": "anjuta"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/23/17-14-13-7533a481.tar.gz",
       "type": "application",
       "id": "arduino"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/23/17-14-29-77406a25.tar.gz",
       "type": "application",
       "id": "bluefish"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/07/24/20-15-04-66ceb6c5.tar.gz",
       "type": "application",
       "id": "codeblocks"
    }
],
},
{
"id": "1",
"type": "column",
"name": "Popular recommendation",
"goods": [
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/06/25/16-30-01-a942dbc1.jpeg",
       "type": "application",
       "id": "glade"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/06/25/16-47-15-0997b1c0.jpeg",
       "type": "application",
       "id": "scite"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/06/25/17-03-24-64c57587.jpeg",
       "type": "application",
       "id": "leafpad"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/06/25/16-58-13-8fa94c33.jpeg",
       "type": "application",
       "id": "gnote"
    },
    {
       "cover": "http://deepin-bucket.b0.upaiyun.com/public/report/2015/06/25/17-07-51-837a593b.jpeg",
       "type": "application",
       "id": "qpdfview"
    }
],
"locales": {
    "zh_CN": {
        "name": "热门推荐"
    }
}
},
...
]
```

### TODO Rating API

-   GET /rankings/downloaded
-   GET /rankings/score
-   Updating

<span id="repository"></span>

repository-api (<http://repository.api.deepin.test>)
----------------------------------------------------

### Mirrors Manager

#### TODO GET /mirrors (需调整完善此结构，并从数据库中移走)

此仓库支持的镜像源列表

``` {.example}
[
{
    "id": "Offical Stable(Chinese mainland)",
    "name": "Offical Stable(Chinese mainland)",
    "url": "http://packages.linuxdeepin.com/deepin",
    "location": "CN"
},
{
    "id": "华中镜像",
    "name": "华中镜像",
    "url": "http://www.deepin.org/",
    "location": "en_US"
},...
]
```

#### TODO GET /iso3166 (移动到更合适的地方去)

[国家码信息](https://en.wikipedia.org/wiki/ISO_3166)
用来枚举合法的地区码。供编辑mirror时使用。

### DSC query

描述信息查询接口，此接口和deb包中的dsc信息保持一致。对外目的有
1.  便于管理员搜索查找package id
2.  供管理员创建/编辑metadata时参考使用。
3.  版本号、包大小、包Id等信息与管理员编辑的包名、描述、截图等信息一起组合成最终用户看到的数据供appstore查询使用。

接口解释
-   [X] Query GET *dsc*:searchString

/searchString/　为任意字符串，仅匹配package id

``` {.example}
[
    {
        "package": "deepin-ui",
        "name": "deepin-ui",
        "description": "LinuxDeepin UI libs",
        "has_metadata": false
    },...
]
```

has~metadata表示此package~ id是否有对应的metadata。
只有管理员显示的创建了metadata后此值才会为true

-   [ ] Modify POST /dsc

修改dsc信息，此接口仅供debian仓库的hook自动调用，管理员无法直接或间接操作此接口。

#### TODO 实现从仓库更新dsc数据到server的cache数据中

SCHEDULED: \<2015-08-05 Wed\> CLOCK: [2015-08-05 Wed 09:52]--[2015-08-05
Wed 11:50] =\> 1:58 CLOCK: [2015-07-30 Thu 21:23]--[2015-07-30 Thu
22:53] =\> 1:30

-   [ ] 创建metadatas/:id时，若无对应metadatas应先检测dsc/:id是否存在
-   [ ] 内部需要自动获得版本、大小等信息。
-   [ ] 版本、大小等固有信息若改变，需要通过webhook进行通知。

### Metadatas Manager

<span id="metadatas"></span>

#### 查询接口

-   GET /metadatas

返回所有元数据的概要信息

-   GET *metadatas*:id

返回对应package的详细信息

#### 编辑接口

编辑接口为过渡性接口，最终所有metadatas信息因有开发者进行维护，并在通过管理员审核后方可进入deepin仓库

-   POST *metadatas*:id

创建或修改对应package的信息 目前支持的字段
1.  name (\*)
2.  icons
3.  screenshots (\*)
4.  category
5.  summary (\*)
6.  description (\*)

其中带\*的字段表示支持国际化，若要修改必须传递lang字段，同时这类字段编时仅是编辑的对应语言，其对应的默认值并不会进行修改。

注意:
icons和screenshots在编辑时，需要传递对应的position信息。目前做法是，字段对应值使用
\$prefix\$p1,\$prefix\$p2, 这类形式进行传递。 如 "s0,s2"
则表示修改第0张和第2张图片，其内容分别在名为"s0"和"s2"的formdata中。

-   DELETE *metadatas*:id

删除某字段

注意:
1.  删除支持国际化字段时，仅删除其对应的翻译信息。
2.  删除icons或screenshots时，需要传递field为positon的字段(值为纯数字)，表示对应的张数.

### Category

分类信息根据不同领域访问不同接口 目前仅支持 `GET /category/application`

``` {.example}
[
{
"id": "internet",
"name": "Internet",
    "locales": {
        "zh_CN": {
        "name": "网络应用"
        }
    }
},...
]
```

最终会支持 /category/icon~theme~　等其他领域的分类信息。
一个package的category和type(深度商店中package都是app类型)信息共同组成“分类”。

### TODO Download

接口描述
-   GET *download*:id

    参数:
    -   from
        客户端传递过来的下载来源信息，通常为商店所在区域。用来统计下载量信息
    -   mirror
        用户期望的镜像源。但在错误情况下会服务器会fallback到官方镜像源，保证仓库的一致性。
-   GET *download~info~*:id

    获得对应package的下载量信息。

TODO webapp-server
------------------

TODO webapp
-----------

TODO Client
-----------

### TODO [\#A] Client Backend

DEADLINE: \<2015-08-09 Sun\>

-   [ ] Download
-   [ ] Install
-   [ ] Remove

#### DONE 临时使用PackageKit的dbus服务生成proxy代码

CLOSED: [2015-08-05 Wed 09:23] SCHEDULED: \<2015-08-02 Sun\>

### TODO dbus-generator

TODO CMS
--------

TODO Comment-CMS
----------------

数据对象与其生命周期
====================

dsc 信息
--------

packgemeta 信息
---------------

appmeta　信息
-------------

翻译信息
--------

系统分层
========

TODO 外网、内网、阿里云、又拍云等
---------------------------------

TODO 文案、软件包准备
=====================

repository goods
----------------

-   [ ] APK
-   [ ] webapp (crosswalk)
    1.  download failed.
    2.  icon field doesn't work.
    3.  Need specify flash plugin path (using google-chrome's plugin)
    4.  Need replace libffmpeg library
-   [ ] eding metadatas

-   [ ] build deb

-   [ ] test deb

TODO 深度商店测试
=================

功能测试
--------

数据有效性
----------

错误日志记录
------------

服务器崩溃测试
--------------

第二阶段
========

metadata
--------

system layout
-------------

### framework多版本共存的处理

想法
====

软件包的metadata包含其所在仓库的信息。
--------------------------------------

结合dpkg的本地缓存动态构建这些信息。用户不需要配置任何/etc/apt/sources.list。

只允许添加经过验证的PPA源.
--------------------------

参考文档
========

[PackageKit backend and AppStream integration for Software
Center](http://swarm.cs.pub.ro/~alexef/gsoc/proposal.pdf)
