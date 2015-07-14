<!--Meta
category:OpenQA
title:Needle助手使用
DO NOT Delete Meta Above -->


## needle助手使用教程
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
```

### 3、启动测试
####（1）下载文件 openqa-needlemaker
* [openqa-needlemaker下载](/OpenQA/openqa-needlemaker.zip)  下载解压后可能需要手动添加可执行权限

添加可执行权限：
```shell
chmod a+x openqa-needlemaker
```
把它放在你的/usr/bin/目录下，方便下次启动

####（2）启动
如：我在worker服务器的目录名字是tangcaijun，我使用的端口是7010（参考文档后面端口分配）

```shell
openqa-needlemaker tangcaijun 7010
```

### 4、在openqa任务启动完成后，启动needle助手 NeedleAssistant

* [Needle助手下载](/OpenQA/NeedleAssistant.zip)  下载后解压，可能需要手动添加可执行权限

NeedleAssistant 启动时接受一个或两个参数

####  一个参数时
* port 服务器开放端口 （默认连接10.0.4.119）


####  两个参数时
* ip  服务器IP
* port 服务器开放端口


#### 例子
```shell
NeedleAssistant 7010
```

### 5、助手使用
一看就会用的啦  ^ ^

![](/OpenQA/NeedleAssistant.png)

* 输入框可输入perl脚本，execute执行脚本
* screenshot 保存截图

#### 注意：退出助手表示主动结束测试


    
### 附端口分配：
```shell
姓名        端口

唐财俊      7010
郭健        7020
王艳丽      7030
...

（其余的同学以递增加10的形式自行分配，分配后请通知其他小伙伴）
```
