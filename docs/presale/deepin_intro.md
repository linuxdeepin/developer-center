<!--Meta
category:售前培训
title: 深度操作系统概述
DO NOT Delete Meta Above -->

- [开发计划](#sec-1)
  - [与国内其他厂商的对比](#sec-1-1)
- [系统组成](#sec-2)
  - [Linux内核](#sec-2-1)
  - [基础运行环境](#sec-2-2)
    - [软件仓库里面包含了哪些东西?](#sec-2-2-1)
    - [系统运行环境](#sec-2-2-2)
  - [桌面运行环境](#sec-2-3)
    - [常见的DE](#sec-2-3-1)
    - [常见组件](#sec-2-3-2)
    - [DDE运行机制](#sec-2-3-3)
  - [应用程序](#sec-2-4)
    - [那么应用程序有哪些分类呢？](#sec-2-4-1)
    - [MIME类型](#sec-2-4-2)
    - [deepin开发的应用程序](#sec-2-4-3)
- [课后测试](#sec-3)


# 开发计划<a id="sec-1" name="sec-1"></a>

-   2004~2011 中文定制版Linux系统-&#x2014; 推广Linux的先驱
-   2011~2013 通过少而精的应用吸引用户-&#x2014; 解决Linux用户的痛点，加强知名度
-   2013~2015 独立的桌面环境&#x2013;&#x2014;改善用户体验，掌握核心话语权
-   2014~2015 独立的软件仓库&#x2013;&#x2014;从根本上脱离任何第三方厂商，完全掌控deepin系统的各组件
-   2015~2016 革新的软件开发机制&#x2013;&#x2014;改善开发者和系统维护者的体验，分离系统与应用
-   2015~2017 健全的生态环境&#x2013;&#x2014;改善第三方厂商进入的门槛，促进产业链升级

## 与国内其他厂商的对比<a id="sec-1-1" name="sec-1-1"></a>

-   优麒麟
-   起点
-   红旗
-   中标

# 系统组成<a id="sec-2" name="sec-2"></a>

整个deepin系统由4部分组成
1.  内核
2.  系统运行环境
3.  桌面运行环境
4.  应用程序

deepin是从 **个别** 应用程序入手，扩展到 **整个** 桌面运行环境，再逐步去 **影响** 系统运行环境，
进而做到控制整个产品。

## Linux内核<a id="sec-2-1" name="sec-2-1"></a>

deepin目前未对内核进行大的调整<sup>来源请求</sup>,直接使用了debian(2015版之前是ubuntu)仓库提供的内核。

可行的方向有
-   中文支持
-   参数调整: 性能参数、兼容参数、安全参数
-   驱动调整
-   新添特性

## 基础运行环境<a id="sec-2-2" name="sec-2-2"></a>

讲到系统运行环境，先请大家说说软件仓库到底是个什么东西？

### 软件仓库里面包含了哪些东西?<a id="sec-2-2-1" name="sec-2-2-1"></a>

-   内核
-   基础文件系统
-   驱动
-   文档
-   甚至源列表文件

系统上所有文件以及软件都是直接或间接的包含在软件仓库里面。    

常用的几个命令

1.  如何查看一个文件所属的软件包?

    dpkg -S 文件路径 or
    apt-file search 

2.  如何查看一个正在运行的窗口是那个程序?

    xprop \_NET<sub>WM</sub><sub>PID</sub> 后鼠标变成X状态，点击对应的程序。得到进程ID
    通过readlink /proc/进程ID/exe 获得启动路径。

3.  如何查看当前安装的某个软件的版本以及候选版本?

    apt-cache policy 包名

### 系统运行环境<a id="sec-2-2-2" name="sec-2-2-2"></a>

-   静态的

根据LFS的指导规范存放在文件系统上的一些基础软件以及数据比如，/etc/passwd,/lib/ld-linux.so,/etc/apt/sources.list等
-   动态的

运行中的内核以及通过systemd或者upstart管理启动的一些列如网络，磁盘挂载服务。

## 桌面运行环境<a id="sec-2-3" name="sec-2-3"></a>

几乎影响所有桌面环境的几个组织
-   X.Org
-   Freedesktop
-   Gnome
-   KDE

### 常见的DE<a id="sec-2-3-1" name="sec-2-3-1"></a>

-   Gnome(gtk)
-   KDE(qt)
-   Lxde(gtk) LxQt(qt5)
-   Xfce(gtk)
-   DDE(gtk/qt)

### 常见组件<a id="sec-2-3-2" name="sec-2-3-2"></a>

-   Windows Manager
-   Input Method
-   Launcher
-   Panel (dock)
-   Session Manager
-   Appearance
-   Configure Modules
-   many service daemon, like
    audio, network, volume, power, login
-   Basic Applications
    Document Reader、Browser、File Manager

### DDE运行机制<a id="sec-2-3-3" name="sec-2-3-3"></a>

1.  display manager

    <https://en.wikipedia.org/wiki/X_display_manager_(program_type)>
    
    -   KDM
    -   GDM
    -   LightDM (deepin所使用的)
    
    1.  重点说LightDM
    
        lightdm作为display manager主要的责任是
        1.  启动一个Xserver
        2.  让用户输入账户密码以及选择桌面环境。
        
        这个程序在lightdm里面叫做greeter，目前有lightdm-gtk-greeter以及deepin自己写的lightm-deepin-greeter.
        可以通过/etc/lightdm/lightdm.conf去修改使用的greeter. 这个在登陆出现问题的时候，可以先尝试切换默认
        greeter到lightdm-gtk-greeter(需要单独安装)后看是否可以登陆。
        1.  greeter验证账号密码通过后启动选择的桌面环境(通过/usr/share/xsessions下的文件选择)
        2.  根据/usr/share/xsessions/deepin.desktop(或gnome.desktop等)中的Exec字段，启动桌面环境(session)

2.  session

    session表示本次会话，一般都是由一个叫做startXX的程序来担当，比如startdde，startxfce等。
    session程序的主要功能
    1.  启动桌面环境的核心组件(core component)
    2.  根据Freedesktop的定义设置一些基本的环境变量(大部分需要正常工作的变量其实是由display manmanger做了)，
    
    以及启动/etc/xdg/autostart,~/.config/xdg/autostart等目录下的文件。
    <http://standards.freedesktop.org/autostart-spec/autostart-spec-latest.html>
    
    session同时也是绝大部分桌面环境相关进程的祖父进程。这个程序如果挂掉，
    整个桌面环境会立刻退出到display manager的界面。 

3.  core component

    -   dde-session-daemon 每个用户会话都有一个实例
    -   dde-system-daemon 整个系统会话只有一个实例
    -   dde-desktop  桌面进程
    -   dde-dock  dock进程
    -   dde-launcher  launcher进程,可以随意kill
    -   dde-control-center 控制中心进程,可以随意kill
    
    以及一些非deepin实现，但非常重要的组件(均为系统会话)
    -   networkmanager 网络服务
    -   pulseaudio 声音服务
    -   udisk2  磁盘挂载等
    -   upower 电源管理服务
    -   systemd 时间，注销管理等服务

## 应用程序<a id="sec-2-4" name="sec-2-4"></a>

应用程序本身种类繁多，Apple Store，Android市场等等，里面放的都叫做应用程序。

### 那么应用程序有哪些分类呢？<a id="sec-2-4-1" name="sec-2-4-1"></a>

按大家熟悉的方式可以归类为
1.  影音娱乐
2.  社交通讯
3.  实用工具
4.  学习办公
5.  金融理财
6.  系统工具

等等

但还可以按此程序对特定文件格式的角色归类3种为
1.  编辑器: 读取、展示、操作、保存某类格式的文件
    编辑图片、编辑文本、编辑电子表格
2.  查看器: 读取、展示特定的文件类型，但无法操作或者保存文件
    查看图片、播放电影、播放音乐
3.  其他: 无法操作特定格式的文件.

按照角色归类就和MIME这个东西紧密关联。

### MIME类型<a id="sec-2-4-2" name="sec-2-4-2"></a>

<https://en.wikipedia.org/wiki/MIME>
MIME源于电子邮件，但如今被广泛应用在文件类型识别上。
常见的类型有:
-   image/png
-   text/plain
-   text/html
-   application/pdf

以及一些数据流上如
-   application/x-www-form-urlencoded
-   multipart/form-data

桌面环境中关于MIME的具体规范可以参见:
<http://standards.freedesktop.org/shared-mime-info-spec/shared-mime-info-spec-0.18.html>

1.  如何设置文件关联

    1.  找到想关联的文件类型，也就是和他相关的MIME类型
    2.  调整影响去关联的文件
    
    具体参见: 
    <https://docs.deepin.io/DE/mime_associations/>     

### deepin开发的应用程序<a id="sec-2-4-3" name="sec-2-4-3"></a>

通用程序
1.  deepin-music
2.  deepin-movie
3.  deepin-screenshot
4.  deepin-terminal
5.  deepin-translator

系统程序
1.  deepin-boot-maker
2.  deepin-installer
3.  deepin-store
4.  deepin-remote-assistance
5.  deepin-manual
6.  deepin-feedback

# 课后测试<a id="sec-3" name="sec-3"></a>

1.  找出系统上所有deepin开发的应用软件。
2.  获得第一题中这些应用软件能打开的文件种类。
3.  尽你所能找出更多重新初始化桌面环境的方式。
4.  揣测下前3题的目的。
