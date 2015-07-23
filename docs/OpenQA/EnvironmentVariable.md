<!--Meta
category:OpenQA
title:OpenQA环境变量
DO NOT Delete Meta Above -->

* OpenQA 原生的环境变量有上百个，但是常用的不是很多，从中挑选了一部分比较常见的，结合源码加上了一些自己的理解，希望能帮助大家更好地了解OpenQA

### ARCH
安装的系统的架构

### BOOTFROM
启动顺序，BOOTFROM=c 硬盘启动， n 网络， d 光驱

### FLAVOR
iso类型（不知道怎么翻译）

### HDDMODEL
硬盘模式，默认是virtio-blk

### HDDSIZEGB
分配硬盘的大小

### ISO
iso名字（不带具体路径，而且所指定的iso必须存放在 /var/lib/openqa/share/factory/iso 存储池）

### KEEPHDDS
不清除虚拟机硬盘目录 （需要进行跳过安装时需要添加此类型的变量）

### MACHINE
指定运行的机器，可选机器列表在 OpenQA(web) > Admin > Machines (需要登录后才可见)

### NAME
此次测试的名称，默认是: id-distri-version-flavor-arch-build-testsuit

### NICMODEL
网卡类型，默认是virtio-net

### NUMDISKS
硬盘数量，默认是1，如果多个硬盘时，每个硬盘的

### QEMUCPU
cpu类型，在OpenQA(web) > Admin > Machines可以设置

### QEMUCPUS
分配给虚拟机的cpu数量，默认 1

### QEMURAM
分配给虚拟机的内存（MB），默认1024

### QEMUVGA
显示输出类型

### QEMU_NO_KVM
启动qemu时不启用kvm模式、

### VERSION
iso版本

### WORKER_CLASS
只能由指定类型的worker来执行该任务，workers.ini配置文件可以对指定worker添加 WORKER_CLASS=xxx 属性
