<!--Meta
category: 项目文档
title: 深度商店(开发记录)
DO NOT Delete Meta Above-->

# 系统设计

## TODO WebHooks

## TODO 通用API规范


组件间的API目前包含 仓库(repository api) 和 商店API(appstore API)。两者均遵守以下说明:
-   Logger
-   数据返回格式
-   Locales处理
-   权限验证

## appstore-api (<http://appstore.api.deepin.test>)

核心接口为两组

1.  橱窗(shopwindow)与商品(goods, e.g. applications,topics)
2.  排行榜(ratings)

### Applications

-   GET /applications

获取所有app的信息
注意:
1.  没有 `/applications/:id` 接口
2.  此接口返回的内容不包含app版本号,描述等信息。元数据请访问 repository的metadatas接口

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

### Topics

-   GET /topics
    -   topic作为个体存在时有其id、name和banner；
    -   topic作为容器存在时有其包含的apps以及背景相关的一些值;

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

### Shopwindows

-   GET /shopwindows

每一个shopwindow(橱窗)包含以下概念
-   type: slider、column、topic
    　通过type决定橱窗的外观样式，默认3种样式分别对应目前3种区域的概念.
-   name
-   goods: apps、topics
    货品可以为app或者 **topic**

其中Goods本身抽象为
1.  cover: 根据期望值设置不同的展示图。即使两个Goods有相同的type和id，其cover也不一定一样。　如Shopwindow为slider时，Goods的cover一般为横幅图，其他类型时则一般是小的banner图.
2.  type: 目前值可为application、topic
3.  id: 通过type和id可以找到此Goods对应的真实对象

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

### TODO Rating API


-   GET /rankings/downloaded
-   GET /rankings/score
-   Updating

<a id="repository" name="repository"></a>

## repository-api (<http://repository.api.deepin.test>)

### Mirrors Manager

1.  TODO GET /mirrors  (需调整完善此结构，并从数据库中移走)

    
    此仓库支持的镜像源列表
    
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

2.  TODO GET /iso3166 (移动到更合适的地方去)

    
    [国家码信息](https://en.wikipedia.org/wiki/ISO_3166) 用来枚举合法的地区码。供编辑mirror时使用。

### DSC query

描述信息查询接口，此接口和deb包中的dsc信息保持一致。对外目的有
1.  便于管理员搜索查找package id
2.  供管理员创建/编辑metadata时参考使用。
3.  版本号、包大小、包Id等信息与管理员编辑的包名、描述、截图等信息一起组合成最终用户看到的数据供appstore查询使用。

接口解释
-   [X] Query
    GET *dsc*:searchString

/searchString/　为任意字符串，仅匹配package id

    [
        {
            "package": "deepin-ui",
            "name": "deepin-ui",
            "description": "LinuxDeepin UI libs",
            "has_metadata": false
        },...
    ]

has\_metadata表示此package id是否有对应的metadata。
只有管理员显示的创建了metadata后此值才会为true

-   [ ] Modify
    POST /dsc

修改dsc信息，此接口仅供debian仓库的hook自动调用，管理员无法直接或间接操作此接口。

1.  TODO 实现从仓库更新dsc数据到server的cache数据中

    
    -   [ ] 创建metadatas/:id时，若无对应metadatas应先检测dsc/:id是否存在
    -   [ ] 内部需要自动获得版本、大小等信息。
    -   [ ] 版本、大小等固有信息若改变，需要通过webhook进行通知。

### Metadatas Manager

<a id="metadatas" name="metadatas"></a>

1.  查询接口

    -   GET /metadatas
    
    返回所有元数据的概要信息
    
    -   GET *metadatas*:id
    
    返回对应package的详细信息

2.  编辑接口

    编辑接口为过渡性接口，最终所有metadatas信息因有开发者进行维护，并在通过管理员审核后方可进入deepin仓库
    
    -   POST *metadatas*:id
    
    创建或修改对应package的信息
    目前支持的字段
    1.  name (\*)
    2.  icons
    3.  screenshots (\*)
    4.  category
    5.  summary (\*)
    6.  description (\*)
    
    其中带\*的字段表示支持国际化，若要修改必须传递lang字段，同时这类字段编时仅是编辑的对应语言，其对应的默认值并不会进行修改。
    
    注意: 
      icons和screenshots在编辑时，需要传递对应的position信息。目前做法是，字段对应值使用 $prefix$p1,$prefix$p2, 这类形式进行传递。
      如 "s0,s2" 则表示修改第0张和第2张图片，其内容分别在名为"s0"和"s2"的formdata中。
    
    -   DELETE *metadatas*:id
    
    删除某字段
    
    注意:
    1.  删除支持国际化字段时，仅删除其对应的翻译信息。
    2.  删除icons或screenshots时，需要传递field为positon的字段(值为纯数字)，表示对应的张数.

### Category

分类信息根据不同领域访问不同接口
目前仅支持
`GET /category/application`

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

最终会支持 /category/icon\_theme　等其他领域的分类信息。
一个package的category和type(深度商店中package都是app类型)信息共同组成“分类”。

### TODO Download


接口描述
-   GET *download*:id
    
    参数: 
    
    -   from   客户端传递过来的下载来源信息，通常为商店所在区域。用来统计下载量信息
    -   mirror 用户期望的镜像源。但在错误情况下会服务器会fallback到官方镜像源，保证仓库的一致性。

-   GET *download\_info*:id
    
    获得对应package的下载量信息。

## TODO webapp-server

## TODO webapp

## TODO Client



### TODO Client Backend


-   [ ] Download
-   [ ] Install
-   [ ] Remove

1.  DONE 临时使用PackageKit的dbus服务生成proxy代码

### TODO dbus-generator

## TODO CMS

## TODO Comment-CMS

# 数据对象与其生命周期

## dsc 信息

## packgemeta 信息

## appmeta　信息

## 翻译信息

# 系统分层

## TODO 外网、内网、阿里云、又拍云等

# TODO 文案、软件包准备



## repository goods

-   [ ] APK
-   [ ] webapp (crosswalk)
    1.  download failed.
    2.  icon field doesn't work.
    3.  Need specify flash plugin path (using google-chrome's plugin)
    4.  Need replace libffmpeg library

-   [ ] eding metadatas

-   [ ] build deb

-   [ ] test deb

# TODO 深度商店测试



## 功能测试

## 数据有效性

## 错误日志记录

## 服务器崩溃测试

# DONE repository API: upload/delte screenshots & icon     :@work:

# 第二阶段

## metadata

## system layout

### framework多版本共存的处理

# 想法

## 软件包的metadata包含其所在仓库的信息。

结合dpkg的本地缓存动态构建这些信息。用户不需要配置任何/etc/apt/sources.list。

## 只允许添加经过验证的PPA源.

# 参考文档

[PackageKit backend and AppStream integration for Software Center](http://swarm.cs.pub.ro/~alexef/gsoc/proposal.pdf)

# 进度会议

## DONE 第32周任务安排


1.  完成所有android和web应用的deb生成。 预先完成deb生成，细节调整，优化之后进行。
2.  所有精品应用的deb测试由陈科云负责，同时此支线任务的进度由陈科云负责。黄志然、龙宇、王珈、马福鸿等人配合。
3.  客户端支持安装删除软件。 陈新楷负责。夏彬配合完成
4.  商店页面实现。 陈新楷负责安排范文杰的任务，王珈验收协调

# 规范用词     :@夏彬:@补充:

所有相关人员有遵守以下规范的责任
1.  看到不规范用语请制止。
2.  发现不合理地方及时指出
3.  本文档未更新前不要擅自使用“更好”的用词
4.  规范变更时，有责任传达到小组人员
5.  此规范影响，设计图用词，图片命名用词，代码命名用词，数据库表命名用词

目的
1.  准确交流,避免歧义
2.  方便测试用例编写
3.  代码名称和设计思维的一致

## 深度商店 (deepin store, dstore)

项目总名称为"深度商店", 不是"软件商店","应用商店"等

## 仓库与商店

### 仓库 (repository)

1.  软件(softwares)

    1.  应用(application)
    2.  驱动(driver)
    3.  开发框架(framework)
    4.  各类主题(theme)

2.  软件原始信息(dsc)

    原始信息包含，版本信息(version)，软件的id(package id), 支持的架构(architecture), 作者(author), 主页(home page)等信息.

3.  软件描述数据(metadatas)

    dsc+管理员编辑后合成为metadatas

4.  仓库源地址 (repository source url)

5.  镜像源列表 (mirror list)

### 商店 (store)

1.  专题(topics)

2.  橱窗 (shopwindow)

    -   栏目橱窗(column shopwindows)
    -   专题橱窗(topic shopwindows)
    -   商品展示窗口 (泛指) (goods)
    -   应用商品展示窗口 (特指应用) (application goods)
    -   专题商品展示窗口 (特指专题) (topic goods)
    -   商品宣传图区域 (banner of goods)
        1.  文字区域 (此区域的内容,slogan of goods)
        2.  图片 (banner of goods)
    -   商品宣传文字区域
    -   轮播橱窗 (顶部轮播，特指当前版本的顶部的轮播橱窗区) (slider shopwindows)

3.  应用(applications)

    -   如"精品应用"，"推荐应用". 不要使用"软件"一词

## 几大组件

### 商店页面 (dstore site)

1.  首页 (home page)

2.  排行榜页面 (rakings page) (不是下载排行榜页面)

    1.  载量排行榜　(downloaded raking)
    2.  评分排行榜 (score raking　)

3.  专题页面 (topic page)

    1.  背景图 (topic background iamge, 简称topic background)
    2.  背景颜色 (topic background color)

4.  应用详情页面　(不是"软件详情"页面) (application detail page)

    1.  相关推荐 (relative apps)
    
    2.  描述 (description)
    
    3.  简介 (summary) 注意和宣传语(slogan)的区别
    
        -   目前深度商店并没有summary这个概念

5.  搜索结果页面 (search result page)

6.  分类展示页面 (cateogry page)

7.  侧边导航栏 (side navigation?)

### 商店客户端 (dstore client, 简称dstore)

### 商店客户端后端 (lastore)

### 商店CMS (dstore cms)

# 开发完成度记录

## 数据相关

### 信息变更通知

1.  应用信息     :@夏彬:

    -   版本号
    -   商店数据

2.  排行榜如何更新?     :@新楷:@夏彬:@补充:

3.  下载量、评分数更新如何通知     :@新楷:@补充:

4.  应用上下架     :@新楷:@全超:@补充:

### deb生成

1.  应用测试源的处理     :@补充:

2.  应用软件deb的生成     :@龙宇:

3.  应用软件deb的测试     :@陈科云:

4.  apk/webapp

    1.  deb生成
    
    2.  deb结构调整成适当的布局

### 翻译

1.  国际化

    1.  登陆界面似乎没有根据主页面的locale的切换而切换     :@夏彬:@确认:
    
    2.  整理各页面出现的ID并替换为英文     :@文杰:@补充:
    
    3.  整理哪些地方需要做国际化     :@王珈:@补充:
    
        -   详情页面: 应用名称、描述、截图
        -   客户端以及网页项目本身所有显示的文字

2.  本地化

    1.  项目的transifex配置     :@新楷:@夏彬:
    
    2.  非固定po方式的数据整合     :@夏彬:@补充:
    
        1.  CMS中直接编辑
        
        2.  分类信息
    
    3.  文案信息没有使用中文     :@夏彬:@补充:

### 评分数据真实化     :@夏彬:@补充:

### 下载数据真实化     :@夏彬:@补充:

### 调整缓存机制，使资源可以在短时间内过期 + 压缩请求数（需要服务端合并请求结果）     :@新楷:

## 工具相关

### 批量导入数据

1.  确定数据格式     :@夏彬:@补充:

### 压力测试工具     :@陈科云:

-   智能仓库压力测试
-   网站压力测试

## CMS

### CMS界面

1.  位置信息、链接ID等宽度过长     :@全超:

2.  补充需要明显调整的地方(是否改进再讨论)     :@王珈:@补充:

### bucket API无法正常使用     :@全超:@李鹤:@确认:

### /metadatas?query=q 搜索功能     :@夏彬:

### metadatas新增接口     :@夏彬:@补充:

### 新创建时候提供默认数据     :@全超:

### 数据用例图绘制     :@夏彬:@补充:

### 镜像管理     :@夏彬:@补充:

### 编辑下载量

1.  提供接口走正常流程刷数据     :@夏彬:

### 下架功能(测试)     :@陈科云:

### 发布按钮功能无法使用     :@全超:

## 评论API

### 接口确定?

### API返回结构调整 (可能需要重写)     :@全超:

### 是否移动CMS

## 测试

### 深度商店页面测试用例完善

### 保证appstore.deepin.test和cms.deepin.test已有功能正常     :@陈科云:

1.  考虑是否可以部分自动测试

## 登陆窗口

### 登录窗口的遮罩效果     :@文杰:

### 登陆窗口出现后，页面后方行为不一致(有部分事件被遮盖)     :@李鹤:@文杰:@确认:

### 登陆界面无法点击“记住密码"     :@李鹤:@确认:

### "注册"|"忘记密码" 不要下划线效果     :@李鹤:

### Mac下出现了滚动条     :@舒乐:@文杰:@确认:

### 测试效果(功能已完成)     :@陈科云:

### 目前的右上角如何处理     :@夏彬:@文杰:@王珈:@舒乐:@补充:

### 相关设计图补充     :@舒乐:@文杰:

## 页面&客户端

### 首页

1.  确认首页slide点击行为     :@王珈:@确认:

### 搜索

1.  搜索补全列表样式细节调整     :@界面:@文杰:

2.  页面搜索框与主内容间的细节调整     :@文杰:

    1.  增加padding

3.  搜索行为

    1.  容回车后，下拉菜单没有消失     :@文杰:
    
    2.  页面切换后，搜索框内容不消失     :@王珈:@确认:

4.  搜索页面 细节     :@文杰:

    1.  搜索栏到主内容间的搜索提示细节     :@舒乐:@补充:

### 专题

1.  背景图与背景主体渐变     :@文杰:

2.  背景图位置调整     :@文杰:

    -专题页面背景图只显示了一部分图片

### 详细页

1.  "相关应用"按钮的布局     :@文杰:

2.  详细页面没有任何评论时，不显示"所有版本"     :@文杰:

3.  截图位置尽量处于居中状态     :@文杰:

    -   页面宽度宽时，目前截图没有居中.

4.  截图点击后位置改变     :@舒乐:@确认:@补充:

    1.  讨论是否目前做这个功能

5.  截图下方的"相关应用"、"评论"的细节

    1.  没有切换效果     :@文杰:
    
    2.  按钮本身文字没有居中     :@文杰:

6.  截图区域图片外加阴影     :@舒乐:@确认:

7.  评论功能

    1.  评论分页功能     :@文杰:
    
    2.  评论失败处理和样式     :@文杰:
    
        1.  补全相关设计图     :@舒乐:@补充:
    
    3.  评论字数限制？     :@文杰:
    
        1.  明确需求     :@王珈:@补充:

8.  安装按钮状态切换

    1.  安装状态检测     :@新楷:@夏彬:@补充:
    
    2.  功能实现     :@新楷:
    
        -   可先模拟
    
    3.  界面实现     :@文杰:
    
    4.  不支持当前架构时的提示     :@夏彬:@补充:@王珈:@舒乐:

9.  文案布局细节

    1.  描述收起     :@文杰:
    
    2.  对齐     :@文杰:

10. 最后更新时间

    1.  API提供此字段     :@夏彬:
    
    2.  计算真实数据     :@夏彬:

11. 截图无法显示

    1.  查找原因,图挂了     :@新楷:
    
    2.  如何避免     :@新楷:@全超:

12. 评分功能

    1.  历史评论接口需要只返回特定应用的数据     :@全超:
    
    2.  评论发出后需要即使更新     :@全超:@确认:
    
        1.  若无法做到，给出原因，统一态度

13. 截图区域的预加载图     :@文杰:

14. 应用页面时高亮对应的分类(需求商讨中)     :@补充:@王珈:

### 应用商品展示窗口

1.  首页、下载排行中的应用下方的短描述是否应该有　     :@陈祥帮:@确认:@王珈:

2.  应用封面处于hover状态时，底下圆角细节不对     :@文杰:

3.  文字与图标的布局调整     :@文杰:

### 侧边栏导航

1.  字体设置     :@确认:@舒乐:

2.  文字间距不对     :@补充:@舒乐:

3.  图标和文字没有对齐     :@文杰:

4.  激活状态文字颜色未响应     :@文杰:

### 下载排行榜页面     :@文杰:

-   编号
-   角标

### 其他

1.  小分辨率时候界面布局的处理     :@文杰:@确认:@舒乐:

    -   支持到什么程度,　最大最小

2.  tooltip提示功能     :@新楷:@文杰:

3.  统一右的键菜单(确定要做什么)     :@新楷:@王珈:

4.  各种出错页面样式     :@文杰:

    -   网络错误 无网络
    -   页面未找到 404
    -   内部错误 500
    
    1.  网络检测功能

5.  预载入效果     :@文杰:

    1.  整页加载     :@文杰:
    
    2.  DONE 商品展示框
    
    3.  应用截图     :@文杰:

6.  返回按钮的显示隐藏（QtWebkit bug：不能记录历史，需要自己实现）     :@新楷:

7.  导航Title信息缺失     :@文杰:@确认:@补充:@王珈:

8.  评论的星星目前都是半颗星星且图片不对     :@文杰:

9.  评分评论下载量的布局不对     :@文杰:

10. 更新设计图时的通知     :@补充:@王珈:@舒乐:

    -   保证方便的前提下，做到通知到相关人员

### 主菜单功能

1.  DONE 登陆

2.  DONE 注销

3.  关于

    1.  补全界面设计图     :@补充:@舒乐:

4.  帮助

    1.  帮助手册内容     :@补充:@王珈:

5.  展示在哪里     :@补充:@王珈:@舒乐:

### 安装应用

1.  界面框架的实现     :@新楷:@补充:

2.  界面细节     :@文杰:

3.  功能

    1.  下载
    
        1.  提供lastore需要的信息     :@新楷:
        
            -   应用包名
            -   来源地区
            -   deepinid
            -   镜像源(lastore处理)
            -   架构(lastore
    
    2.  安装
    
    3.  接口API     :@新楷:@夏彬:@补充:
    
    4.  接口实现     :@夏彬:

4.  中途退出

    1.  如何交互     :@补充:@王珈:

5.  下载进度窗口

    1.  数据接口     :@新楷:@夏彬:@补充:
    
        1.  确定接口API
    
    2.  界面     :@文杰:

### 卸载应用

1.  接口API     :@夏彬:

2.  接口实现     :@夏彬:

3.  界面实现     :@夏彬:@补充:

### 更新

1.  更新数据格式     :@夏彬:@补充:

2.  应用更新     :@夏彬:@补充:

3.  系统更新     :@夏彬:@补充:
