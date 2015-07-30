<!--Meta
category:售前培训
title:系统了解
DO NOT Delete Meta Above -->

#CGroups及Linux Containers(LXC/Docker)介绍

CGroups是control groups的缩写，是Linux内核提供的一种可以限制、记录、隔离进程组（process groups）所使用的物理资源（如：cpu,memory,IO等等）的机制。最初由google的工程师提出，后来被整合进Linux内核。Cgroups也是LXC为实现虚拟化所使用的资源管理手段，可以说没有cgroups就没有LXC。
##CGooups可以做什么？
Cgroups最初的目标是为资源管理提供的一个统一的框架，既整合现有的cpuset等子系统，也为未来开发新的子系统提供接口。现在的cgroups适用于多种应用场景，从单个进程的资源控制，到实现操作系统层次的虚拟化（OS Level Virtualization）。Cgroups提供了一下功能：

1.限制进程组可以使用的资源数量（Resource limiting ）。比如：memory子系统可以为进程组设定一个memory使用上限，一旦进程组使用的内存达到限额再申请内存，就会出发OOM（out of memory）。

2.进程组的优先级控制（Prioritization ）。比如：可以使用cpu子系统为某个进程组分配特定cpu share。

3.记录进程组使用的资源数量（Accounting ）。比如：可以使用cpuacct子系统记录某个进程组使用的cpu时间

4.进程组隔离（Isolation）。比如：使用ns子系统可以使不同的进程组使用不同的namespace，以达到隔离的目的，不同的进程组有各自的进程、网络、文件系统挂载空间。

5.进程组控制（Control）。比如：使用freezer子系统可以将进程组挂起和恢复。

##Cgroups相关概念及其关系
####相关概念
1.任务（task）。在cgroups中，任务就是系统的一个进程。

2.控制族群（control group）。控制族群就是一组按照某种标准划分的进程。Cgroups中的资源控制都是以控制族群为单位实现。一个进程可以加入到某个控制族群，也从一个进程组迁移到另一个控制族群。一个进程组的进程可以使用cgroups以控制族群为单位分配的资源，同时受到cgroups以控制族群为单位设定的限制。

3.层级（hierarchy）。控制族群可以组织成hierarchical的形式，既一颗控制族群树。控制族群树上的子节点控制族群是父节点控制族群的孩子，继承父控制族群的特定的属性。

4.子系统（subsytem）。一个子系统就是一个资源控制器，比如cpu子系统就是控制cpu时间分配的一个控制器。子系统必须附加（attach）到一个层级上才能起作用，一个子系统附加到某个层级以后，这个层级上的所有控制族群都受到这个子系统的控制。

####相互关系
1.每次在系统中创建新层级时，该系统中的所有任务都是那个层级的默认 cgroup（我们称之为 root cgroup ，此cgroup在创建层级时自动创建，后面在该层级中创建的cgroup都是此cgroup的后代）的初始成员。

2.一个子系统最多只能附加到一个层级。

3.一个层级可以附加多个子系统

4.一个任务可以是多个cgroup的成员，但是这些cgroup必须在不同的层级。

5.系统中的进程（任务）创建子进程（任务）时，该子任务自动成为其父进程所在 cgroup 的成员。然后可根据需要将该子任务移动到不同的 cgroup 中，但开始时它总是继承其父任务的cgroup。

####Cgroups子系统介绍

blkio -- 这个子系统为块设备设定输入/输出限制，比如物理设备（磁盘，固态硬盘，USB 等等）。

cpu -- 这个子系统使用调度程序提供对 CPU 的 cgroup 任务访问。

cpuacct -- 这个子系统自动生成 cgroup 中任务所使用的 CPU 报告。

cpuset -- 这个子系统为 cgroup 中的任务分配独立 CPU（在多核系统）和内存节点。

devices -- 这个子系统可允许或者拒绝 cgroup 中的任务访问设备。

freezer -- 这个子系统挂起或者恢复 cgroup 中的任务。

memory -- 这个子系统设定 cgroup 中任务使用的内存限制，并自动生成由那些任务使用的内存资源报告。

net_cls -- 这个子系统使用等级识别符（classid）标记网络数据包，可允许 Linux 流量控制程序（tc）识别从具体 cgroup 中生成的数据包。

ns -- 名称空间子系统。

##参考资料
http://blog.jtlebi.fr/2013/12/22/introduction-to-linux-namespaces-part-1-uts/
https://blog.jtlebi.fr/2013/12/28/introduction-to-linux-namespaces-part-2-ipc/
https://blog.jtlebi.fr/2014/01/05/introduction-to-linux-namespaces-part-3-pid/
https://blog.jtlebi.fr/2014/01/12/introduction-to-linux-namespaces-part-4-ns-fs/
https://blog.jtlebi.fr/2014/01/19/introduction-to-linux-namespaces-part-5-net/
http://blog.jtlebi.fr/2014/05/29/introduction-to-seccomp-bpf-linux-syscall-filter/
http://www.ibm.com/developerworks/cn/linux/1506_cgroup/index.html
