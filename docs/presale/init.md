<!--Meta
category:售前培训
title:系统了解
DO NOT Delete Meta Above -->

#Linux初始化init系统
近年来，Linux 系统的 init 进程经历了两次重大的演进，传统的 sysvinit 已经淡出历史舞台，新系统 UpStart 和 systemd 各有特点，而越来越多的 Linux 发行版采纳了 systemd。本文简要介绍了这三种 init 系统的使用和原理，每个 Linux 系统管理员和系统软件开发者都应该了解它们，以便更好地管理系统和开发应用。
##什么是 Init 系统,init 系统的历史和现状
Linux 操作系统的启动首先从 BIOS 开始，接下来进入 boot loader，由 bootloader 载入内核，进行内核初始化。内核初始化的最后一步就是启动 pid 为 1 的 init 进程。这个进程是系统的第一个进程。它负责产生其他所有用户进程。
init 以守护进程方式存在，是所有其他进程的祖先。init 进程非常独特，能够完成其他进程无法完成的任务。
Init 系统能够定义、管理和控制 init 进程的行为。它负责组织和运行许多独立的或相关的始化工作(因此被称为 init 系统)，从而让计算机系统进入某种用户预订的运行模式。
仅仅将内核运行起来是毫无实际用途的，必须由 init 系统将系统代入可操作状态。比如启动外壳 shell 后，便有了人机交互，这样就可以让计算机执行一些预订程序完成有实际意义的任务。或者启动 X 图形系统以便提供更佳的人机界面，更加高效的完成任务。这里，字符界面的 shell 或者 X 系统都是一种预设的运行模式。
大多数 Linux 发行版的 init 系统是和 System V 相兼容的，被称为 sysvinit。这是人们最熟悉的 init 系统。一些发行版如 Slackware 采用的是 BSD 风格 Init 系统，这种风格使用较少，本文不再涉及。其他的发行版如 Gentoo 是自己定制的。Ubuntu 和 RHEL 采用 upstart 替代了传统的 sysvinit。而 Fedora 从版本 15 开始使用了一个被称为 systemd 的新 init 系统。
可以看到不同的发行版采用了不同的 init 实现，本系列文章就是打算讲述三个主要的 Init 系统：sysvinit，UpStart 和 systemd。了解它们各自的设计特点，并简要介绍它们的使用。
在 Linux 主要应用于服务器和 PC 机的时代，SysVinit 运行非常良好，概念简单清晰。它主要依赖于 Shell 脚本，这就决定了它的最大弱点：启动太慢。在很少重新启动的 Server 上，这个缺点并不重要。而当 Linux 被应用到移动终端设备的时候，启动慢就成了一个大问题。为了更快地启动，人们开始改进 sysvinit，先后出现了 upstart 和 systemd 这两个主要的新一代 init 系统。Upstart 已经开发了 8 年多，在不少系统中已经替换 sysvinit。Systemd 出现较晚，但发展更快。

> 如何指定init程序
> 见/usr/share/initramfs-tools/init 脚本，这个文件即是initrd文件里面的init

##Sysvinit
####Sysinit概况
sysvinit 就是 system V 风格的 init 系统，顾名思义，它源于 System V 系列 UNIX。它提供了比 BSD 风格 init 系统更高的灵活性。是已经风行了几十年的 UNIX init 系统，一直被各类 Linux 发行版所采用。
####运行级别
Sysvinit 用术语 runlevel 来定义"预订的运行模式"。Sysvinit 检查 '/etc/inittab' 文件中是否含有 'initdefault' 项。 这告诉 init 系统是否有一个默认运行模式。如果没有默认的运行模式，那么用户将进入系统控制台，手动决定进入何种运行模式。

sysvinit 中运行模式描述了系统各种预订的运行模式。通常会有 8 种运行模式，即运行模式 0 到 6 和 S 或者 s。

每种 Linux 发行版对运行模式的定义都不太一样。但 0，1，6 却得到了大家的一致赞同：
* 0 关机
* 1 单用户模式
* 6 重启

通常在 /etc/inittab 文件中定义了各种运行模式的工作范围。比如 RedHat 定义了 runlevel 3 和 5。运行模式 3 将系统初始化为字符界面的 shell 模式；运行模式 5 将系统初始化为 GUI 模式。无论是命令行界面还是 GUI，运行模式 3 和 5 相对于其他运行模式而言都是完整的正式的运行状态，计算机可以完成用户需要的任务。而模式 1，S 等往往用于系统故障之后的排错和恢复。

很显然，这些不同的运行模式下系统需要初始化运行的进程和需要进行的初始化准备都是不同的。比如运行模式 3 不需要启动 X 系统。用户只需要指定需要进入哪种模式，sysvinit 将负责执行所有该模式所必须的初始化工作。

####sysvinit 运行顺序

Sysvinit 巧妙地用脚本，文件命名规则和软链接来实现不同的 runlevel。首先，sysvinit 需要读取/etc/inittab 文件。分析这个文件的内容，它获得以下一些配置信息：
* 系统需要进入的 runlevel
* 捕获组合键的定义
* 定义电源 fail/restore 脚本
* 启动 getty 和虚拟控制台
* 得到配置信息后，sysvinit 顺序地执行以下这些步骤，从而

将系统初始化为预订的 runlevel X。
* /etc/rc.d/rc.sysinit
* /etc/rc.d/rc 和/etc/rc.d/rcX.d/ (X 代表运行级别 0-6)
* /etc/rc.d/rc.local
* X Display Manager（如果需要的话）

首先，运行 rc.sysinit 以便执行一些重要的系统初始化任务。rc.sysinit 主要完成以下这些工作。
* 激活 udev 和 selinux
* 设置定义在/etc/sysctl.conf 中的内核参数
* 设置系统时钟
* 加载 keymaps
* 激活交换分区
* 设置主机名(hostname)
* 根分区检查和 remount
* 激活 RAID 和 LVM 设备
* 开启磁盘配额
* 检查并挂载所有文件系统
* 清除过期的 locks 和 PID 文件

完成了以上这些工作之后，sysvinit 开始运行/etc/rc.d/rc 脚本。根据不同的 runlevel，rc 脚本将打开对应该 runlevel 的 rcX.d 目录(X 就是 runlevel)，找到并运行存放在该目录下的所有启动脚本。每个 runlevel X 都有一个这样的目录，目录名为/etc/rc.d/rcX.d。

在这些目录下存放着很多不同的脚本。文件名以 S 开头的脚本就是启动时应该运行的脚本，S 后面跟的数字定义了这些脚本的执行顺序。在/etc/rc.d/rcX.d 目录下的脚本其实都是一些软链接文件，真实的脚本文件存放在/etc/init.d 目录下。如下所示：

```script
[root@www ~]# ll /etc/rc5.d/
lrwxrwxrwx 1 root root 16 Sep  4  2008 K02dhcdbd -> ../init.d/dhcdbd
....(中间省略)....
lrwxrwxrwx 1 root root 14 Sep  4  2008 K91capi -> ../init.d/capi
lrwxrwxrwx 1 root root 23 Sep  4  2008 S00microcode_ctl -> ../init.d/microcode_ctl
lrwxrwxrwx 1 root root 22 Sep  4  2008 S02lvm2-monitor -> ../init.d/lvm2-monitor
....(中间省略)....
lrwxrwxrwx 1 root root 17 Sep  4  2008 S10network -> ../init.d/network
....(中间省略)....
lrwxrwxrwx 1 root root 11 Sep  4  2008 S99local -> ../rc.local
lrwxrwxrwx 1 root root 16 Sep  4  2008 S99smartd -> ../init.d/smartd
....(底下省略)....
```
当所有的初始化脚本执行完毕。Sysvinit 运行/etc/rc.d/rc.local 脚本。

rc.local 是 Linux 留给用户进行个性化设置的地方。您可以把自己私人想设置和启动的东西放到这里，一台 Linux Server 的用户一般不止一个，所以才有这样的考虑。

####Sysvinit和系统关闭
Sysvinit 不仅需要负责初始化系统，还需要负责关闭系统。在系统关闭时，为了保证数据的一致性，需要小心地按顺序进行结束和清理工作。

比如应该先停止对文件系统有读写操作的服务，然后再 umount 文件系统。否则数据就会丢失。

这种顺序的控制这也是依靠/etc/rc.d/rcX.d/目录下所有脚本的命名规则来控制的，在该目录下所有以 K 开头的脚本都将在关闭系统时调用，字母 K 之后的数字定义了它们的执行顺序。

这些脚本负责安全地停止服务或者其他的关闭工作。

####Sysvinit 的管理和控制功能

此外，在系统启动之后，管理员还需要对已经启动的进程进行管理和控制。原始的 sysvinit 软件包包含了一系列的控制启动，运行和关闭所有其他程序的工具。
**halt**
停止系统。
**init**
这个就是 sysvinit 本身的 init 进程实体，以 pid1 身份运行，是所有用户进程的父进程。最主要的作用是在启动过程中使用/etc/inittab 文件创建进程。
**killall5**
就是 SystemV 的 killall 命令。向除自己的会话(session)进程之外的其它进程发出信号，所以不能杀死当前使用的 shell。
**last**
回溯/var/log/wtmp 文件(或者-f 选项指定的文件)，显示自从这个文件建立以来，所有用户的登录情况。
**lastb**
作用和 last 差不多，默认情况下使用/var/log/btmp 文件，显示所有失败登录企图。
**mesg**
控制其它用户对用户终端的访问。
**pidof**
找出程序的进程识别号(pid)，输出到标准输出设备。
**poweroff**
等于 shutdown -h –p，或者 telinit 0。关闭系统并切断电源。
**reboot**
等于 shutdown –r 或者 telinit 6。重启系统。
**runlevel**
读取系统的登录记录文件(一般是/var/run/utmp)把以前和当前的系统运行级输出到标准输出设备。
**shutdown**
以一种安全的方式终止系统，所有正在登录的用户都会收到系统将要终止通知，并且不准新的登录。
**sulogin**
当系统进入单用户模式时，被 init 调用。当接收到启动加载程序传递的-b 选项时，init 也会调用 sulogin。
**telinit**
实际是 init 的一个连接，用来向 init 传送单字符参数和信号。
**utmpdump**
以一种用户友好的格式向标准输出设备显示/var/run/utmp 文件的内容。
**wall**
向所有有信息权限的登录用户发送消息。

不同的 Linux 发行版在这些 sysvinit 的基本工具基础上又开发了一些辅助工具用来简化 init 系统的管理工作。比如 RedHat 的 RHEL 在 sysvinit 的基础上开发了 initscripts 软件包，包含了大量的启动脚本 (如 rc.sysinit) ，还提供了 service，chkconfig 等命令行工具，甚至一套图形化界面来管理 init 系统。其他的 Linux 发行版也有各自的 initscript 或其他名字的 init 软件包来简化 sysvinit 的管理。
只要您理解了 sysvinit 的机制，在一个最简的仅有 sysvinit 的系统下，您也可以直接调用脚本启动和停止服务，手动创建 inittab 和创建软连接来完成这些任务。因此理解 sysvinit 的基本原理和命令是最重要的。您甚至也可以开发自己的一套管理工具。

####Sysvinit 的小结
Sysvinit 的优点是概念简单。Service 开发人员只需要编写启动和停止脚本，概念非常清楚；将 service 添加/删除到某个 runlevel 时，只需要执行一些创建/删除软连接文件的基本操作；这些都不需要学习额外的知识或特殊的定义语法(UpStart 和 Systemd 都需要用户学习新的定义系统初始化行为的语言)。

其次，sysvinit 的另一个重要优点是确定的执行顺序：脚本严格按照启动数字的大小顺序执行，一个执行完毕再执行下一个，这非常有益于错误排查。UpStart 和 systemd 支持并发启动，导致没有人可以确定地了解具体的启动顺序，排错不易。

但是串行地执行脚本导致 sysvinit 运行效率较慢，在新的 IT 环境下，启动快慢成为一个重要问题。此外动态设备加载等 Linux 新特性也暴露出 sysvinit 设计的一些问题。针对这些问题，人们开始想办法改进 sysvinit，以便加快启动时间，并解决 sysvinit 自身的设计问题。

##Upstart
####Upstart简介
upstart不再使用/etc/inittab 文件了，这是因为 Ubuntu 使用了一种被称为 upstart 的新型 init 系统。

####开发 Upstart 的缘由
大约在 2006 年或者更早的时候， Ubuntu 开发人员试图将 Linux 安装在笔记本电脑上。在这期间技术人员发现经典的 sysvinit 存在一些问题：它不适合笔记本环境。这促使程序员 Scott James Remnant 着手开发 upstart。
当 Linux 内核进入 2.6 时代时，内核功能有了很多新的更新。新特性使得 Linux 不仅是一款优秀的服务器操作系统，也可以被用于桌面系统，甚至嵌入式设备。桌面系统或便携式设备的一个特点是经常重启，而且要频繁地使用硬件热插拔技术。在现代计算机系统中，硬件繁多、接口有限，人们并非将所有设备都始终连接在计算机上，比如 U 盘平时并不连接电脑，使用时才插入 USB 插口。因此，当系统上电启动时，一些外设可能并没有连接。而是在启动后当需要的时候才连接这些设备。在 2.6 内核支持下，一旦新外设连接到系统，内核便可以自动实时地发现它们，并初始化这些设备，进而使用它们。这为便携式设备用户提供了很大的灵活性。
可是这些特性为 sysvinit 带来了一些挑战。当系统初始化时，需要被初始化的设备并没有连接到系统上；比如打印机。为了管理打印任务，系统需要启动 CUPS 等服务，而如果打印机没有接入系统的情况下，启动这些服务就是一种浪费。Sysvinit 没有办法处理这类需求，它必须一次性把所有可能用到的服务都启动起来，即使打印机并没有连接到系统，CUPS 服务也必须启动。
还有网络共享盘的挂载问题。在/etc/fstab 中，可以指定系统自动挂载一个网络盘，比如 NFS，或者 iSCSI 设备。在本文的第一部分 sysvinit 的简介中可以看到，sysvinit 分析/etc/fstab 挂载文件系统这个步骤是在网络启动之前。可是如果网络没有启动，NFS 或者 iSCSI 都不可访问，当然也无法进行挂载操作。Sysvinit 采用 netdev 的方式来解决这个问题，即/etc/fstab 发现 netdev 属性挂载点的时候，不尝试挂载它，在网络初始化并使能之后，还有一个专门的 netfs 服务来挂载所有这些网络盘。这是一个不得已的补救方法，给管理员带来不便。部分新手管理员甚至从来也没有听说过 netdev 选项，因此经常成为系统管理的一个陷阱。
针对以上种种情况，Ubuntu 开发人员在评估了当时的几个可选 init 系统之后，决定重新设计和开发一个全新的 init 系统，即 UpStart。UpStart 基于事件机制，比如 U 盘插入 USB 接口后，udev 得到内核通知，发现该设备，这就是一个新的事件。UpStart 在感知到该事件之后触发相应的等待任务，比如处理/etc/fstab 中存在的挂载点。采用这种事件驱动的模式，upstart 完美地解决了即插即用设备带来的新问题。
此外，采用事件驱动机制也带来了一些其它有益的变化，比如加快了系统启动时间。sysvinit 运行时是同步阻塞的。一个脚本运行的时候，后续脚本必须等待。这意味着所有的初始化步骤都是串行执行的，而实际上很多服务彼此并不相关，完全可以并行启动，从而减小系统的启动时间。在 Linux 大量应用于服务器的时代，系统启动时间也许还不那么重要；然而对于桌面系统和便携式设备，启动时间的长短对用户体验影响很大。此外云计算等新的 Server 端技术也往往需要单个设备可以更加快速地启动。
UpStart 满足了这些需求，目前不仅桌面系统 Ubuntu 采用了 UpStart，甚至企业级服务器级的 RHEL 也默认采用 UpStart 来替换 sysvinit 作为 init 系统。

####Upstart 的特点
UpStart 解决了之前提到的 sysvinit 的缺点。采用事件驱动模型，UpStart 可以：
* 更快地启动系统
* 当新硬件被发现时动态启动服务
* 硬件被拔除时动态停止服务

这些特点使得 UpStart 可以很好地应用在桌面或者便携式系统中，处理这些系统中的动态硬件插拔特性。

####Upstart概念和术语
Upstart 的基本概念和设计清晰明确。UpStart 主要的概念是 job 和 event。Job 就是一个工作单元，用来完成一件工作，比如启动一个后台服务，或者运行一个配置命令。每个 Job 都等待一个或多个事件，一旦事件发生，upstart 就触发该 job 完成相应的工作。
**Job**
Job 就是一个工作的单元，一个任务或者一个服务。可以理解为 sysvinit 中的一个服务脚本。有三种类型的工作：
* task job；
* service job；
* abstract job；

task job 代表在一定时间内会执行完毕的任务，比如删除一个文件；

service job 代表后台服务进程，比如 apache httpd。这里进程一般不会退出，一旦开始运行就成为一个后台精灵进程，由 init 进程管理，如果这类进程退出，由 init 进程重新启动，它们只能由 init 进程发送信号停止。它们的停止一般也是由于所依赖的停止事件而触发的，不过 upstart 也提供命令行工具，让管理人员手动停止某个服务；

Abstract job 仅由 upstart 内部使用，仅对理解 upstart 内部机理有所帮助。我们不用关心它。

除了以上的分类之外，还有另一种工作（Job）分类方法。Upstart 不仅可以用来为整个系统的初始化服务，也可以为每个用户会话（session）的初始化服务。系统的初始化任务就叫做 system job，比如挂载文件系统的任务就是一个 system job；用户会话的初始化服务就叫做 session job。

**Job 生命周期**

Upstart 为每个工作都维护一个生命周期。一般来说，工作有开始，运行和结束这几种状态。为了更精细地描述工作的变化，Upstart 还引入了一些其它的状态。比如开始就有开始之前(pre-start)，即将开始(starting)和已经开始了(started)几种不同的状态，这样可以更加精确地描述工作的当前状态。

工作从某种初始状态开始，逐渐变化，或许要经历其它几种不同的状态，最终进入另外一种状态，形成一个状态机。在这个过程中，当工作的状态即将发生变化的时候，init 进程会发出相应的事件（event）。

| 状态名     |    含义    | 
| :-------- | ------ --:| 
| Waiting   | 初始状态   |
| Staring   | Job即将开始   |
|pre-start  |执行 pre-start 段，即任务开始前应该完成的工作|
|Spawned    |准备执行 script 或者 exec 段|
|post-start |执行 post-start 动作|
|Running    |interim state set after post-start section processed denoting job is running (But it may have no associated PID!)|
|pre-stop   |执行 pre-stop 段|
|Stopping   |interim state set after pre-stop section processed|
|Killed |任务即将被停止|
|post-stop  |执行 post-stop 段|

 **Job 的状态机**
 ![Job的状态机](http://www.ibm.com/developerworks/cn/linux/1407_liuming_init2/image003.jpg)
 其中有四个状态会引起 init 进程发送相应的事件，表明该工作的相应变化：
* Starting
* Started
* Stopping
* Stopped

而其它的状态变化不会发出事件。那么我们接下来就来看看事件的详细含义吧。

####事件 Event
顾名思义，Event 就是一个事件。事件在 upstart 中以通知消息的形式具体存在。一旦某个事件发生了，Upstart 就向整个系统发送一个消息。没有任何手段阻止事件消息被 upstart 的其它部分知晓，也就是说，事件一旦发生，整个 upstart 系统中所有工作和其它的事件都会得到通知。

Event 可以分为三类: signal，methods 或者 hooks。

**Signals**
Signal 事件是非阻塞的，异步的。发送一个信号之后控制权立即返回。

**Methods**
Methods 事件是阻塞的，同步的。

**Hooks**
Hooks 事件是阻塞的，同步的。它介于 Signals 和 Methods 之间，调用发出 Hooks 事件的进程必须等待事件完成才可以得到控制权，但不检查事件是否成功。

事件是个非常抽象的概念，下面我罗列出一些常见的事件，希望可以帮助您进一步了解事件的含义：
* 系统上电启动，init 进程会发送"start"事件
* 根文件系统可写时，相应 job 会发送文件系统就绪的事件
* 一个块设备被发现并初始化完成，发送相应的事件
* 某个文件系统被挂载，发送相应的事件
* 类似 atd 和 cron，可以在某个时间点，或系统上电后运行 GRUB 载入内核。内核执行硬件初始化和内核自身初始化。在内核初始化的最后，内核将启动 pid 为 1 的 init 进程，即 UpStart 进程。
Upstart 进程在执行了一些自身的初始化工作后，立即发出"startup"事件。上图中用红色方框加红色箭头表示事件，可以在左上方看到"startup"事件。
所有依赖于"startup"事件的工作被触发，其中最重要的是 mountall。mountall 任务负责挂载系统中需要使用的文件系统，完成相应工作后，mountall 任务会发出以下事件：local-filesystem，virtual-filesystem，all-swaps，
其中 virtual-filesystem 事件触发 udev 任务开始工作。任务 udev 触发 upstart-udev-bridge 的工作。Upstart-udev-bridge 会发出 net-device-up IFACE=lo 事件，表示本地回环 IP 网络已经准备就绪。同时，任务 mountall 继续执行，最终会发出 filesystem 事件。
此时，任务 rc-sysinit 会被触发，因为 rc-sysinit 的 start on 条件如下：
start on filesystem and net-device-up IFACE=lo
任务 rc-sysinit 调用 telinit。Telinit 任务会发出 runlevel 事件，触发执行/etc/init/rc.conf。
rc.conf 执行/etc/rc$.d/目录下的所有脚本，和 SysVInit 非常类似，读者可以参考本文第一部分的描述。者周期的时间点发送事件
* 另外一个 job 开始或结束时，发送相应的事件
* 一个磁盘文件被修改时，可以发出相应的事件
* 一个网络设备被发现时，可以发出相应的事件
* 缺省路由被添加或删除时，可以发出相应的事件

不同的 Linux 发行版对 upstart 有不同的定制和实现，实现和支持的事件也有所不同，可以用man 7 upstart-events来查看事件列表。

####Job 和 Event 的相互协作
Upstart 就是由事件触发工作运行的一个系统，每一个程序的运行都由其依赖的事件发生而触发的。

系统初始化的过程是在工作和事件的相互协作下完成的，可以大致描述如下：系统初始化时，init 进程开始运行，init 进程自身会发出不同的事件，这些最初的事件会触发一些工作运行。每个工作运行过程中会释放不同的事件，这些事件又将触发新的工作运行。如此反复，直到整个系统正常运行起来。

究竟哪些事件会触发某个工作的运行？这是由Job配置文件定义的。

####Job配置文件
任何一个工作都是由一个工作配置文件（Job Configuration File）定义的。这个文件是一个文本文件，包含一个或者多个小节（stanza）。每个小节是一个完整的定义模块，定义了工作的一个方面，比如 author 小节定义了工作的作者。工作配置文件存放在/etc/init 下面，是以.conf 作为文件后缀的文件。
```bash
#This is a simple demo of Job Configure file
#This line is comment, start with #

#Stanza 1, The author
author “Liu Ming”

#Stanza 2, Description
description “This job only has author and description, so no use, just a demo”
```

上面的例子不会产生任何作用，一个真正的工作配置文件会包含很多小节，其中比较重要的小节有以下几个：

**"expect" Stanza**
Upstart 除了负责系统的启动过程之外，和 SysVinit 一样，Upstart 还提供一系列的管理工具。当系统启动之后，管理员可能还需要进行维护和调整，比如启动或者停止某项系统服务。或者将系统切换到其它的工作状态，比如改变运行级别。本文后续将详细介绍 Upstart 的管理工具的使用。

为了启动，停止，重启和查询某个系统服务。Upstart 需要跟踪该服务所对应的进程。比如 httpd 服务的进程 PID 为 1000。当用户需要查询 httpd 服务是否正常运行时，Upstart 就可以利用 ps 命令查询进程 1000，假如它还在正常运行，则表明服务正常。当用户需要停止 httpd 服务时，Upstart 就使用 kill 命令终止该进程。为此，Upstart 必须跟踪服务进程的进程号。

部分服务进程为了将自己变成后台精灵进程(daemon)，会采用两次派生(fork)的技术，另外一些服务则不会这样做。假如一个服务派生了两次，那么 UpStart 必须采用第二个派生出来的进程号作为服务的 PID。但是，UpStart 本身无法判断服务进程是否会派生两次，为此在定义该服务的工作配置文件中必须写明 expect 小节，告诉 UpStart 进程是否会派生两次。

Expect 有两种，"expect fork"表示进程只会 fork 一次；"expect daemonize"表示进程会 fork 两次。

**"exec" Stanza 和"script" Stanza**
一个 UpStart 工作一定需要做些什么，可能是运行一条 shell 命令，或者运行一段脚本。用"exec"关键字配置工作需要运行的命令；用"script"关键字定义需要运行的脚本。

```
# mountall.conf
description “Mount filesystems on boot”
start on startup
stop on starting rcS
...
script
  . /etc/default/rcS
  [ -f /forcefsck ] && force_fsck=”--force-fsck”
  [ “$FSCKFIX”=”yes” ] && fsck_fix=”--fsck-fix”
   
  ...
  
  exec mountall –daemon $force_fsck $fsck_fix
end script
```
这是 mountall 的例子，该工作在系统启动时运行，负责挂载所有的文件系统。该工作需要执行复杂的脚本，由"script"关键字定义；在脚本中，使用了 exec 来执行 mountall 命令。

**"start on" Stanza 和"stop on" Stanza**
"start on"定义了触发工作的所有事件。"start on"的语法很简单，如下所示：
start on EVENT [[KEY=]VALUE]... [and|or...]

EVENT 表示事件的名字，可以在 start on 中指定多个事件，表示该工作的开始需要依赖多个事件发生。多个事件之间可以用 and 或者 or 组合，"表示全部都必须发生"或者"其中之一发生即可"等不同的依赖条件。除了事件发生之外，工作的启动还可以依赖特定的条件，因此在 start on 的 EVENT 之后，可以用 KEY=VALUE 来表示额外的条件，一般是某个环境变量(KEY)和特定值(VALUE)进行比较。如果只有一个变量，或者变量的顺序已知，则 KEY 可以省略。

"stop on"和"start on"非常类似，只不过是定义工作在什么情况下需要停止。

start on/ stop on 例子
```
#dbus.conf
description     “D-Bus system message bus”

start on local-filesystems
stop on deconfiguring-networking
…
```
D-Bus 是一个系统消息服务，上面的配置文件表明当系统发出 local-filesystems 事件时启动 D-Bus；当系统发出 deconfiguring-networking 事件时，停止 D-Bus 服务。

####Session Init
UpStart 还可以用于管理用户会话的初始化。

首先让我们了解一下 Session 的概念。Session 就是一个用户会话，即用户从远程或者本地登入系统开始工作，直到用户退出。这整个过程就构成一个会话。

每个用户的使用习惯和使用方法都不相同，因此用户往往需要为自己的会话做一个定制，比如添加特定的命令别名，启动特殊的应用程序或者服务，等等。这些工作都属于对特定会话的初始化操作，因此可以被称为 Session Init。

用户使用 Linux 可以有两种模式：字符模式和图形界面。在字符模式下，会话初始化相对简单。用户登录后只能启动一个 Shell，通过 shell 命令使用系统。各种 shell 程序都支持一个自动运行的启动脚本，比如~/.bashrc。用户在这些脚本中加入需要运行的定制化命令。字符会话需求简单，因此这种现有的机制工作的很好。

在图形界面下，事情就变得复杂一些。用户登录后看到的并不是一个 shell 提示符，而是一个桌面。一个完整的桌面环境由很多组件组成。

一个桌面环境包括 window manager，panel 以及其它一些定义在/usr/share/gnome-session/sessions/下面的基本组件；此外还有一些辅助的应用程序，共同帮助构成一个完整的方便的桌面，比如 system monitors，panel applets，
NetworkManager，Bluetooth，printers 等。当用户登录之后，这些组件都需要被初始化，这个过程比字符界面要复杂的多。目前启动各种图形组件和应用的工作由 gnome-session 完成。过程如下：

当用户登录图形界面后，显示管理器(Display Manager)lightDM 启动 Xsession。Xsession 接着启动 gnome-session，gnome-session 负责其它的初始化工作，然后就开始了一个 desktop session。

传统desktop session 启动过程
```
init
 |- lightdm
 |   |- Xorg
 |   |- lightdm ---session-child
 |        |- gnome-session --session=ubuntu
 |             |- compiz
 |             |- gwibber
 |             |- nautilus
 |             |- nm-applet
 |             :
 |             :
 |
 |- dbus-daemon --session
 |
 :
 :
```

这个过程有一些缺点（和 sysVInit 类似）。一些应用和组件其实并不需要在会话初始化过程中启动，更好的选择是在需要它们的时候才启动。比如 update-notifier 服务，该服务不停地监测几个文件系统路径，一旦这些路径上发现可以更新的软件包，就提醒用户。这些文件系统路径包括新插入的 DVD 盘等。Update-notifier 由 gnome-session 启动并一直运行着，在多数情况下，用户并不会插入新的 DVD，此时 update-notifier 服务一直在后台运行并消耗系统资源。更好的模式是当用户插入 DVD 的时候再运行 update-notifier。这样可以加快启动时间，减小系统运行过程中的内存等系统资源的开销。对于移动，嵌入式等设备等这还意味着省电。除了 Update-notifier 服务之外，还有其它一些类似的服务。比如 Network Manager，一天之内用户很少切换网络设备，所以大部分时间 Network Manager 服务仅仅是在浪费系统资源；再比如 backup manager 等其它常驻内存，后台不间断运行却很少真正被使用的服务。

用 UpStart 的基于事件的按需启动的模式就可以很好地解决这些问题，比如用户插入网线的时候才启动 Network Manager，因为用户插入网线表明需要使用网络，这可以被称为按需启动。

采用 Upstart 的 Desktop session init 过程
```
init
 |- lightdm
 |   |- Xorg
 |   |- lightdm ---session-child
 |        |- session-init # <-- upstart running as normal user
 |             |- dbus-daemon --session
 |             |- gnome-session --session=ubuntu
 |             |- compiz
 |             |- gwibber
 |             |- nautilus
 |             |- nm-applet
 |             :
 |             :
 :
 :
```

####Upstart使用

对于Upstart配置来说不仅需要掌握工作配置文件的写法，还需要了解一些针对服务进程编程上的要求。本文仅列出了少数工作配置文件的语法。要全面掌握工作配置文件的写法，需要详细阅读 Upstart 的手册。这里让我们来分析一下如何用 Upstart 来实现传统的运行级别，进而了解如何灵活使用工作配置文件。

#####Upstart 系统中的运行级别
Upstart 的运作完全是基于工作和事件的。工作的状态变化和运行会引起事件，进而触发其它工作和事件。

而传统的 Linux 系统初始化是基于运行级别的，即 SysVInit。因为历史的原因，Linux 上的多数软件还是采用传统的 SysVInit 脚本启动方式，并没有为 UpStart 开发新的启动脚本，因此即便在 Debian 和 Ubuntu 系统上，还是必须模拟老的 SysVInit 的运行级别模式，以便和多数现有软件兼容。

虽然 Upstart 本身并没有运行级别的概念，但完全可以用 UpStart 的工作模拟出来。

UpStart 机制下的系统启动过程。
![enter image description here](http://www.ibm.com/developerworks/cn/linux/1407_liuming_init2/image004.png)

系统上电后运行 GRUB 载入内核。内核执行硬件初始化和内核自身初始化。在内核初始化的最后，内核将启动 pid 为 1 的 init 进程，即 UpStart 进程。

Upstart 进程在执行了一些自身的初始化工作后，立即发出"startup"事件。上图中用红色方框加红色箭头表示事件，可以在左上方看到"startup"事件。

所有依赖于"startup"事件的工作被触发，其中最重要的是 mountall。mountall 任务负责挂载系统中需要使用的文件系统，完成相应工作后，mountall 任务会发出以下事件：local-filesystem，virtual-filesystem，all-swaps，
其中 virtual-filesystem 事件触发 udev 任务开始工作。任务 udev 触发 upstart-udev-bridge 的工作。Upstart-udev-bridge 会发出 net-device-up IFACE=lo 事件，表示本地回环 IP 网络已经准备就绪。同时，任务 mountall 继续执行，最终会发出 filesystem 事件。

此时，任务 rc-sysinit 会被触发，因为 rc-sysinit 的 start on 条件如下：
```start on filesystem and net-device-up IFACE=lo```

任务 rc-sysinit 调用 telinit。Telinit 任务会发出 runlevel 事件，触发执行/etc/init/rc.conf。

rc.conf 执行/etc/rc$.d/目录下的所有脚本，和 SysVInit 非常类似。

#####程序开发时需要注意的事项
在编写系统服务时，需要了解 UpStart 的一些特殊要求。只有符合这些要求的软件才可以被 UpStart 管理。
**规则一，派生次数需声明。**
很多 Linux 后台服务都通过派生两次的技巧将自己变成后台服务程序。如果您编写的服务也采用了这个技术，就必须通过文档或其它的某种方式明确地让 UpStart 的维护人员知道这一点，这将影响 UpStart 的 expect stanza，在前面已经详细介绍过这个 stanza 的含义。

**规则二，派生后即可用。**
后台程序在完成第二次派生的时候，必须保证服务已经可用。因为 UpStart 通过派生计数来决定服务是否处于就绪状态。

**规则三，遵守 SIGHUP 的要求。**
UpStart 会给精灵进程发送 SIGHUP 信号，此时，UpStart 希望该Daemon进程做以下这些响应工作：
* 完成所有必要的重新初始化工作，比如重新读取配置文件。这是因为 UpStart 的命令"initctl reload"被设计为可以让服务在不重启的情况下更新配置。
* Daemon进程必须继续使用现有的 PID，即收到 SIGHUP 时不能调用 fork。如果服务必须在这里调用 fork，则等同于派生两次，参考上面的规则一的处理。这个规则保证了 UpStart 可以继续使用 PID 管理本服务。

**规则四，收到 SIGTEM 即 shutdown。**
当收到 SIGTERM 信号后，UpStart 希望Daemon进程进程立即干净地退出，释放所有资源。如果一个进程在收到 SIGTERM 信号后不退出，Upstart 将对其发送 SIGKILL 信号。

#####Upstart命令
UpStart 提供了一系列的命令来完成这些工作。其中的核心是initctl，这是一个带子命令风格的命令行工具。

比如可以用 initctl list 来查看所有工作的概况：

```$initctl list
alsa-mixer-save stop/waiting
avahi-daemon start/running, process 690
mountall-net stop/waiting
rc stop/waiting
rsyslog start/running, process 482
screen-cleanup stop/waiting
tty4 start/running, process 859
udev start/running, process 334
upstart-udev-bridge start/running, process 304
ureadahead-other stop/waiting```

第一列是工作名，比如 rsyslog。第二列是工作的目标；第三列是工作的状态。

此外还可以用 initctl stop 停止一个正在运行的工作；用 initctl start 开始一个工作；还可以用 initctl status 来查看一个工作的状态；initctl restart 重启一个工作；initctl reload 可以让一个正在运行的服务重新载入配置文件。这些命令和传统的 service 命令十分相似。

一些命令是为了兼容其它系统(主要是 sysvinit)，比如显示 runlevel 用/sbin/runlevel 命令：
```$runlevel
N 2```
这个输出说明当前系统的运行级别为 2。而且系统没有之前的运行级别，也就是说在系统上电启动进入预定运行级别之后没有再修改过运行级别。

那么如何修改系统上电之后的默认运行级别呢？

在 Upstart 系统中，需要修改```/etc/init/rc-sysinti.conf ```中的``` DEFAULT_RUNLEVEL ```这个参数，以便修改默认启动运行级别。
还有一些随 UpStart 发布的小工具，用来帮助开发 UpStart 或者诊断 UpStart 的问题。比如 init-checkconf 和 upstart-monitor
还可以使用 initctl 的 emit 命令从命令行发送一个事件。
```#initctl emit <event>```
这一般是用于 UpStart 本身的排错。

##Systemd
####Systemd简介和特点
Systemd 是 Linux 系统中最新的初始化系统（init），它主要的设计目标是克服 sysvinit 固有的缺点，提高系统的启动速度。
由于篇幅较长，将在另一份文档中详细说明
