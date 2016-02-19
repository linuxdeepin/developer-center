<!--Meta
category:OpenQA
title:Needle助手使用
DO NOT Delete Meta Above -->


## needle助手使用教程

(本教程建立在《Worker服务器使用》教程之上)

### 1、准备好安装好系统的虚拟机硬盘
在跑完一次测试完成后，硬盘文件的路径为
```shell
/var/lib/openqa/pool/worker-id/raid/1  # work-id 为跑该测试的worker ID
```

以后将硬盘文件统一备份到/home/deepin/OpenQA/share/HDD 目录下  
备份时以iso日期作为其名字，如果名字重复了，以下划线加序号命名，如：20150706_2
```shell
# 如，备份7月6号iso虚拟硬盘文件，worker-id为10
cp /var/lib/openqa/pool/10/raid/1 /home/deepin/OpenQA/share/HDD/20150706
```


### 2、到相应的pool目录给硬盘建立软链接
比炉说：
```shell
# 如果你在服务器使用的worker的ID是10
mkdir -p /var/lib/openqa/pool/10/raid  # -p 表示连同父目录一起创建
sudo ln -sfn your-vDisk-path /var/lib/openqa/pool/10/raid/l1  # your-vDisk-path 你的硬盘文件路径

# 当然，如果你觉得麻烦的话，可以直接使用服务器的~/OpenQA/share目录的LinkHDD工具
# (LinkHDD 工具是对上面两行代码的包装)
./LinkHDD 10 20150706   # 10 为worker-ID, 20150706 为硬盘名字
```

### 3、启动测试
####（1）下载文件 openqa-needlemaker

[openqa-needlemaker下载](/OpenQA/openqa-needlemaker.zip)

(注：openqa-needlemaker 和 下面的Needle助手都是运行在你的系统上的)

#### 参数
* name-spell  你名字的拼写
* needle-port 用于助手连接的端口号（文档末尾附有端口号分配）


#### 例子
```shell
# 可以把它放在你的/usr/bin/目录下，方便下次启动
sudo cp openqa-needlemaker /usr/bin/

# 直接执行
openqa-needlemaker tangcaijun 7010
```


### 4、在openqa任务启动完成后，启动needle助手 NeedleAssistant

[Needle助手下载](/OpenQA/NeedleAssistant.zip)

NeedleAssistant 启动时接受一个或两个参数

####  一个参数时
* port 服务器开放端口 （默认连接10.0.4.119）


####  两个参数时
* ip  服务器IP
* port 服务器开放端口


#### 例子
```shell
# 可以把它放在你的/usr/bin/目录下，方便下次启动
sudo cp NeedleAssistant /usr/bin/

# 启动
NeedleAssistant 7010
```

### 5、助手使用
一看就会用的啦  ^ ^

![](/OpenQA/NeedleAssistant.png)

* 输入框可输入perl脚本，execute执行脚本
* screenshot 保存截图

** 注意：退出助手表示主动结束测试 **


### 6、vncviewer

如果你需要连接到虚拟机进行操作，可以使用vncviewer进行远程连接  
```shell
# 假如我启动的虚拟机的vnc端口是6000
vncviewer 10.0.4.119:6000
```
暂时能想到的vnc端口获取方式：  
连接到服务器使用  
```shell
sudo netstat -plent

# 端口号一般以60开头，进程名为：qemu-system-x86_64

```

---
### 补充一下 Needle 环境变量说明
** Needle 制作记得要加的：**

1、** needle名字 **   

2、** needle文件名 **  默认是带日期的，统一都改成都不要带日期，文件名有一定描述性。如果needle更新了，就采用覆盖的方式来变更needle，对不用的needle要进行删除。不要像opensuse的needle那样堆得太多了，同步needle需要花的时间好长好长，清理无用needle需要花的功夫好大好大...  

3、** 语言环境变量 **  以后可能还会测其他语言，所以这个变量保留，用以区分不同语言环境下的needle  

** 不要保留：**  
如下经常会自动勾上的变量，记得把勾去掉，不需添加  
ENV-DISTRI-deepin  &emsp;&emsp;&emsp;  我们就只测deepin不测其他,没必要添加发行版限定  
ENV-FLAVOR-SID-DVD    &emsp;&nbsp;   我们现在测试只有sid版，是单版本测试，没必要限定iso类型；还有以后flavor不一定会叫这个  
ENV-VERSION-2014.3    &emsp;&emsp;   随着iso发布，系统版本号也会发生改变，所以无须限定needle对应的系统版本  
...

** <font color=#DE5336> \*\* 其他的环境变量如果不是非得依赖的话就尽量不要添加进去(尽量保证needle整洁 ;)  )</font>**


### 附端口分配：
```shell
姓名        端口

唐财俊      7010
郭健        7015
王艳丽      7020
...

（其余的同学以递增加5的形式自行分配，分配后请告知其他小伙伴）
```
