目的
====

1.  准确交流,避免歧义
2.  方便测试用例编写
3.  代码名称和设计思维的一致

所有相关人员有遵守以下规范的责任

1.  看到不规范用语请制止。
2.  发现不合理地方及时指出
3.  本文档未更新前不要擅自使用“更好”的用词
4.  规范变更时，有责任传达到小组人员
5.  此规范影响，设计图用词，图片命名用词，代码命名用词，数据库表命名用词

深度商店 (deepin store, dstore)
===============================

项目总名称为"深度商店", 不是"软件商店","应用商店"等

仓库与商店
==========

仓库 (repository)
-----------------

### 软件(softwares)

1.  应用(application)
2.  驱动(driver)
3.  开发框架(framework)
4.  各类主题(theme)

### 软件原始信息(dsc)

原始信息包含，版本信息(version)，软件的id(package id),
支持的架构(architecture), 作者(author), 主页(home page)等信息.

### 软件描述数据(metadatas)

dsc+管理员编辑后合成为metadatas

### 仓库源地址 (repository source url)

### 镜像源列表 (mirror list)

商店 (store)
------------

### 专题(topics)

### 橱窗 (shopwindow)

-   栏目橱窗(column shopwindows)
-   专题橱窗(topic shopwindows)
-   商品展示窗口 (泛指) (goods)
-   应用商品展示窗口 (特指应用) (application goods)
-   专题商品展示窗口 (特指专题) (topic goods)
-   商品宣传图区域 (banner of goods)
    1.  文字区域 (此区域的内容,slogan of goods)
    2.  图片 (banner of goods)
-   商品宣传文字区域
-   轮播橱窗 (顶部轮播，特指当前版本的顶部的轮播橱窗区) (slider
    shopwindows)

### 应用(applications)

-   如"精品应用"，"推荐应用". 不要使用"软件"一词

几大组件
========

商店页面 (dstore site)
----------------------

### 首页 (home page)

### 排行榜页面 (rakings page) (不是下载排行榜页面)

1.  载量排行榜　(downloaded raking)
2.  评分排行榜 (score raking　)

### 专题页面 (topic page)

1.  背景图 (topic background iamge, 简称topic background)
2.  背景颜色 (topic background color)

### 应用详情页面　(不是"软件详情"页面) (application detail page)

#### 相关推荐 (relative apps)

#### 描述 (description)

#### 简介 (summary) 注意和宣传语(slogan)的区别

-   目前深度商店并没有summary这个概念

### 搜索结果页面 (search result page)

### 分类展示页面 (cateogry page)

### 侧边导航栏 (side navigation?)

商店客户端 (dstore client, 简称dstore)
--------------------------------------

商店客户端后端 (lastore)
------------------------

商店CMS (dstore cms)
--------------------
