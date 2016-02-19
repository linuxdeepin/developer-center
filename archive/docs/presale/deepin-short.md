<!--Meta
category:售前培训
title:Deepin系统简介
DO NOT Delete Meta Above -->

#深度操作系统
深度操作系统基于GNU/Linux开发
##架构
一般有4个主要部分：
内核、shell、文件系统和应用程序。内核、shell和文件系统一起形成了基本的操作系统结构，它们使得用户可以运行程序、管理文件并使用系统。
部分层次结构如图所示。
![Alt text](./201494163707222.jpg)


Linux系统由硬件、内核、系统调用、shell、库函数构成。

Linux首先启动内核 (kernel)，内核是一段计算机程序，这个程序直接管理管理硬件，包括CPU、内存空间、硬盘接口、网络接口等等。所有的计算机操作都要通过内核传递给硬件。

为了方便调用内核，Linux将内核的功能接口制作成系统调用(system call)。系统调用看起来就像C语言的函数。你可以在程序中直接调用。Linux系统有两百多个这样的系统调用。用户不需要了解内核的复杂结构，就可以使用内核。系统调用是操作系统的最小功能单位。一个操作系统，以及基于操作系统的应用，都不可能实现超越系统调用的功能。

在命令行中输入``$man 2 syscalls``可以查看所有的系统调用。你也可以通过``$man 2 read``来查看系统调用read()的说明。在这两个命令中的2都表示我们要在2类(系统调用类)中查询 (具体各个类是什么可以通过``$man man``看到)。

系统调用提供的功能非常基础，所以使用起来很麻烦。一个简单的给变量分配内存空间的操作，就需要动用多个系统调用。Linux定义一些库函数(library routine)来将系统调用组合成某些常用的功能。上面的分配内存的操作，可以定义成一个库函数(像malloc()这样的函数)。再比如说，在读取文件的时候，系统调用要求我们设置好所需要的缓冲。我可以使用Standard IO库中的读取函数。这个读取函数既负责设置缓冲，又负责使用读取的系统调用函数。使用库函数对于机器来说并没有效率上的优势，但可以把程序员从细节中解救出来。

shell是一个特殊的应用。很多用户将它称为命令行 。shell是一个命令解释器(interpreter)，当我们输入“ls -l”的时候，它将此字符串解释为

1.在默认路径找到该文件(/bin/ls)，
2.执行该文件，并附带参数"-l"。

用>表示重新定向，用|表示管道 ，也是通过shell解释&或者|的含义。Shell接着通过系统调，用指挥内核，实现具体的重定向或者管道。在没有图形界面之前，shell充当了用户的界面，当用户要运行某些应用时，通过shell输入命令，来运行程序。shell是可编程的，它可以执行符合shell语法的文本。这样的文本叫做shell脚本(script)。可以在架构图中看到，shell下通系统调用，上通各种应用，同时还有许多自身的小工具可以使用。Shell脚本可以在寥寥数行中，实现复杂的功能。

![Alt text](./201494163822613.png)


UNIX的一条哲学是让每个程序尽量独立的做好一个小的功能。而shell充当了这些小功能之间的"胶水"，让不同程序能够以一个清晰的接口(文本流)协同工作，从而增强各个程序的功能。

##组成
Linux 系统一般有4个主要部分:内核、shell、文件系统和应用程序。
Deepin目前集中于应用程序开发。

##启动流程
linux启动过程也分为几个过程，基本的激动流程图如下：
![Alt text](./20131104084047435.gif)
无论是目前2014.3还是2015系统，都只是在/sbin/init执行后不同，开始一直到/sbin/init启动流程是一致的。

###守护进程(init)
目前Deepin支持sysv、upstrart，以及2015支持systemd作为服务管理
####sysv
SysVinit守护进程（sysvinit软件包）是一个基于运行级别的系统，它使用运行级别（单用户、多用户以及其他更多级别）和链接（位于/etc /rc?.d目录中，分别链接到/etc/init.d中的init脚本）来启动和关闭系统服务。
####upstart
Upstart init守护进程（upstart软件包）是基于事件的系统，它使用事件来启动和关闭系统服务。
####systemd
systemd 是 Linux 下一个与 SysV 和 LSB 初始化脚本兼容的系统和服务管理器。systemd 使用 socket 和 D-Bus 来开启服务，提供基于守护进程的按需启动策略，保留了 Linux cgroups 的进程追踪功能，支持快照和系统状态恢复，维护挂载和自挂载点，实现了各服务间基于从属关系的一个更为精细的逻辑控制，拥有前卫的并行性能。systemd 无需经过任何修改便可以替代 sysvinit 。

> Upstart 及 Systemd 都兼容SysV，所以依然可以处理那些在目录/etc/init.d中包含服务脚本的服务，runlevel的概念也是只存在于 Sysv。在使用Upstart和Systemd的系统中，runlevel的概念也基本不存在了。
> 但是Upstart和Systemd二者是不能互相兼容的。

## 服务进程和管理
用service命令和chkconfig命令管理服务进程
如果用apt-get命令安装mysql,nginx等服务程序,安装程序都会自动在/etc/init.d/目录中创建一个管理此服务进程用的shell脚本,如:
 
* /etc/init.d/mysql
* /etc/init.d/nginx
* /etc/init.d/keepalived

这样我们就用可以用``/etc/init.d/{脚本文件名} start ``或 ``service {脚本文件名} start ``来启动一个服务,如:
 
####启动mysql服务
``/etc/init.d/mysql start``
``service mysql start``

如果进程管理脚本支持restart命令参数,还可以用`` /etc/init.d/{脚本文件名} restart`` 或 ``service {脚本文件名} restart`` 来重新启动 一个服务,如:
####重新启动mysql服务
``/etc/init.d/mysql restart``
``service mysql restart``
上面两个命令的效果是一样的,这样重启mysql或php-fpm的时候就不用每次都先把进程kill掉,然后写一大段路径和参数来启动服务了.只不过用service命令的话只要记住脚本文件名,不用写绝对地址,这样比较方便,默认的脚本文件名都是和服务程序的名字一样的。

> service 命令不仅仅支持sysv-init启动脚本，也支持upstart和systemd，所以为了统一，尽量可以使用service进行服务管理。

### 持久性启用/禁用服务
SysV默认管理工具为``chkconfig``，Systemd默认为``systemctl``，upstart默认并未提供一个工具进行此操作。
但是Ubuntu和Debian对各个启动管理都进行了一个封装，提供``update-rc.d``进行服务持久性管理。
也就是说，在Deepin系统上，我们可以直接使用``update-rc.d``来持久性启用/禁用服务。

> 需要进一步进行说明的是，chkconfig只会列出SysV的服务，而不会列出upstart以及systemd的服务。
