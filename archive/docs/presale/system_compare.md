<!--Meta
category:售前培训
title:系统了解
DO NOT Delete Meta Above -->

# 基本概念 #

## 桌面环境 ##

包含窗口管理器/常用工具(浏览器/媒体播放器等)等的一个完整的软件组合.<br />
常见的桌面环境有 Gnome2, GnomeShell, KDE, LXDE, XFCE4 等<br />
像 FVWM, *box(openbox, blackbox, fluxbox等), metacity, xfwm 等窗口管理器一般不认为是桌面环境

## 发行版 ##

有个人或组织将系统必须组件及常用软件以软件包(源码包或二进制包)仓库的形式提供给用户使用, 这样一套系统即成为发行版<br />

## 衍生版 ##

在已有发行版上做修改并重新发布的一般认为是该发行版的衍生版.

# 体系 #

各个发行版可以从不同角度划分为不同的体系, 一般按照软件包格式进行划分<br >

## RPM系

### RedHat Enterprise Linux(RHEL)

<http://distrowatch.com/table.php?distribution=redhat><br />
企业级Linux支持,不用详细解释吧

1.  CentOS

<http://distrowatch.com/table.php?distribution=centos><br />
CentOS就是RedHat开源代码重新编译后的发行版,不包含RedHat的收费组件

2.  Fedora

<http://distrowatch.com/table.php?distribution=fedora><br />
RedHat的试验田

### SUSE Linux Enterprise(SLE)

<http://distrowatch.com/table.php?distribution=sle><br />
据我了解Suse Linux用的比较多的是银行单位

1.  OpenSuse Linux

    和Fedora与Redhat关系差不多

### Mandriva

很老的发行版

### 其他

## DEB系

### Debian

<http://lisdn.com/?viewnews-151><br />


#### 衍生版 ####

##### Ubuntu #####

衍生版

1.  Kubuntu/Lubuntu/Xubuntu/等等

基于Ubuntu的不同桌面环境

2.  PearOS/Elementary等等

自行开发的桌面环境

3.  Mint等等

更良好的体验

### Knoppix等等各式各样的发行版

## 其他包管理

### ArchLinux

pacman(也可以自己编译包makepkg)

### Slackware

slackpkg

### Gentoo

portage

## 编译系

### Gentoo

混在两个阵营

### LFS

最干净可控的"发行版"

## 比较

### RPM 和 DEB

刚接触 rpm 的人都了解, rpm最大的问题就是依赖关系乱, 网上的很多教程在安装rpm的时候都是直接给个固定版本的包, 不考虑系统上的包版本, 比较容易出现版本依赖问题.<br />
而像yum之类的工具在解析依赖的时候又非常的慢, 每次更新系统都很纠结<br />
使用deb之后世界都清爽了, 依赖关系解决超快, 也不用关心版本问题, 直接使用apt就可以了.

### Arch 和 Gentoo

这两个其实比较意义不大, 主要是这两个发行版给人的感觉差不多, 定制性很强<br />
Arch的定制性在于AUR和makepkg的组合使用, 可以安装第三方软件或者某些软件的最新版本或特定功能的版本, 还可以修改系统中某个软件的依赖以精简系统.<br />
Gentoo的Portage也有类似的功能, 关闭特定的USE Flags来避免安装某些依赖.<br />
像上述这种裁剪系统的能力对于deb系和rpm系的系统而言就比较麻烦了.

### LFS

LFS最大的好处就是在构建整个系统的过程中可以对系统有更深入的了解, 其他的话日常使用什么的真心不建议用这个.
