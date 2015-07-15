<!--Meta
category:OpenQA
title:Worker服务器使用
DO NOT Delete Meta Above -->

   
## worker服务器使用
### 1、ssh连接到worker服务器  
ssh deepin@10.0.4.119  
密码：（你猜）

### 2、sshfs远程挂载你的脚本目录到服务器上

#### （1）在/home/deepin/OpenQA/share/创建以你名字拼音命名的文件夹，如：

```shell
mkdir -p tangcaijun/deepin  # 将tangcaijun换成你的名字拼音拼写
```

#### （2）在/home/deepin/OpenQA/share/目录中执行挂载，如：

```shell
# 第一个参数为你PC的ssh连接地址，第二个为你的名字拼写
./mount choldrim@10.0.1.62 tangcaijun
```

#### （3）查看是否挂载成功

```shell
ls /home/deepin/OpenQA/share/tangcaijun/deepin  # 记得替换tangcaijun
```
能列出你的脚本则表示挂载成功


经过这几步就已经将你的代码挂到服务器了，你可以随意的在你的pc上修改你的代码，服务器那边也会同步

### 3、在服务器配置一个你的专属worker

#### （1）获取本地key和secret

在 ***你的系统*** 上启动openqa-webui （注意，是你的系统）
```shell
sudo openqa-webui
```

打开你本地的openqa页面

登录 -> 点击右上角的 manage API keys

若没有expires（过期时间）为never的key，则点击左边的create 生成一个

#### （2）配置远程Worker
把你的key和secret存放到 ***服务器*** 的/etc/openqa/client.conf中 （注意，是服务器）

如：
我的ip是10.0.1.62，则：
```ini
[10.0.1.62]
key = MYKEYXXXXXXXXXX
secret = MYSECRETXXXXXXX
```

在/etc/openqa/workers.ini中添加:
```ini
[10]
HOST=http://10.0.1.62
```
表示指定ID为10的worker所连接的服务器IP为10.0.1.62  
(文档后面附有 Worker ID 分配方式)

### 4、启动测试
把你的目录挂载到服务器了，哪剩下的就是要怎么让服务器跑你的代码了
#### （1）在你的PC上启动webui
```shell
sudo openqa-webui  # 如果已经启动了就跳过这一步
```

#### （2）在服务器启动对应worker
```shell
sudo openqa-worker Worker-ID
```
如，我使用的WorkerID为 10，则
```shell
sudo openqa-worker 10
```


#### （3）回到你的pc上，启动测试

```shell
# 和普通启动测试一样，但需要额外添加指定的CASEDIR环境变量，tangcaijun修改为你的名字
openqa-test CASEDIR=/home/deepin/OpenQA/share/tangcaijun/deepin
```

或者也可以在你pc上的配置文件 /etc/openqa/deepin.ini 中添加 CASEDIR 环境变量，然后直接openqa-test也可以达到同样效果


### 附录：

因为一个worker只能连接一个OpenQA服务机，为了避免worker冲突，所以使用强制性分配workerID

```shell
姓名     WorkerID

唐财俊      10

郭健        15

王艳丽      20
...

# 其他同学需要用到worker服务器时以递增加5的形式自行分配，分配后记得通知其他小伙伴，避免冲突
# 如果有特殊要求需要启动两个或多个worker的，则在你的ID到下一个人的ID之间选择一个自己觉得合适的ID去启动worker就可以了
```

