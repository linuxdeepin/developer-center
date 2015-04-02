<!--Meta
category:文档服务
title:编写指南
DO NOT Delete Meta Above -->

## 一、简介

深度文档是基于mkdocs定制的深度开发文档服务，用于指导开发人员使用深度提供的API、服务。

文档服务采用markdown文件静态页面生成html页面，相关代码均托管再github上。

## 二、文档编写

开发人员将直接再github上编写文档，文档服务器会直接拉取github上的开发文档，并生成对应的页面。

### 1 获取文档仓库

````
git clone git@github.com:linuxdeepin/docs.deepin.io.git deepin-docs
````

### 2 添加新页面

````
cd deepin-docs
./new.py "桌面开发" "Widget Developer" dde/widget.md
````

new.py 接受3个参数， 分别为文档的分类目录，文档标题，以及文档的相对文件路径。
上述命名将创建docs/dde/widget.md文件，其内容如下：

````markdown
<!--Meta
category:桌面开发
title:Widget Developer
DO NOT Delete Meta Above -->
````

### 3 编辑页面

直接修改docs/dde/widget.md文件即可。主要不要删除meta信息，如果想改变页面的标题或者分类，可以直接修改meta信息。category表示文档分类，title表示文档标题。

### 4 提交页面

提交前，请先执行./build.py, 检查页面是否正确编写。

````
$ ./build.py 
Genarator mkdocs.yml
('Add:', u"    - ['index.md', '\u9996\u9875', '']")
('Add:', u"    - ['guide/start.md', '\u6587\u6863\u670d\u52a1', '\u7f16\u5199\u6307\u5357']")
('Add:', u"    - ['api/rest.md', 'DeepinID', '\u63a5\u53e3\u8bbe\u8ba1']")
('Add:', u"    - ['api/oauth2.md', 'DeepinID', 'OAuth2\u63a5\u53e3']")
````

build.py执行成功后，直接push到master分支即可。docs.deepin.io会在接受到github的推送消息后更新文档。
