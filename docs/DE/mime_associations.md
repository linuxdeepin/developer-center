<!--Meta
category:DE
title:文件关联
DO NOT Delete Meta Above -->

要修改文件关联首先需要理解两个重要概念

1. 需要关联什么*文件类型*
2. 需要关联到什么程序


文件类型定义
=============
/usr/share/mime/packages/

具体参见：
[shared-mime-info-spec](http://standards.freedesktop.org/shared-mime-info-spec/shared-mime-info-spec-0.18.html)


关联的程序
===========
目前Freedesktop定义的*程序*是指一个desktop文件。
也就是/usr/share/applications下面出现的这些文件。

文件类型关联
============
大部分的文件关联是通过desktop文件内的MimeType指定的。
但也用户以及系统厂商也可以通过特定的配置文件来修改。

具体参见： [Default applications](https://wiki.archlinux.org/index.php/Default_applications)


示例
==========
本示例展示如何将*.xls*文件关联到gedit上

1. 定义或找到xls本身的*文件类型定义*文件. 在最新的Deepin2014.2上是由/usr/share/mime/packages/wps-office-et.xml文件定义的，
   并找到对应<mime type>字段。 本示例中的是"application/wps-office.xls"。 (也可以使用alias字段)
2. 决定是在系统级别还是用户级别进行修改并选择需要修改的文件，
   本次修改采用系统级别的/usr/share/applications/mimeapps.list文件。
   在"Default Applications"组中添加对应的关联内容，
   Key(文件类型)=Value(需要打开的Desktop文件)

````
	[Default Applications]
	application/wps-office.xls=gedit.desktop
````

3. 运行update-mime。系统级别需要使用sudo运行。
4. 打开文件管理器测试, 且右键可以选择其他关联的程序。
