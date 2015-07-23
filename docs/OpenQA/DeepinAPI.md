<!--Meta
category:OpenQA
title:OpenQA deepin API
DO NOT Delete Meta Above -->


##### 注：使用deepin API的时候记得在测试模块头部添加函数引用，如：
```perl
use deepinapi qw(download_local_file start_program);
```

### collect_logs
收集日志  
此函数会收集 $HOME/.xsession-errors\*  、 /var/log/X\*  、$HOME/core 文件到测试结果Uploaded Logs中

#### 参数
无

#### 返回值
无

#### 例子
```perl
# 直接调用
collect_logs;
```


### download_local_file
从deepin/data目录下载软件（先要在deepin/data中存放相应文件）

#### 参数
* file 文件名
* store 虚拟机中的存放目录，不存在会自动创建
* timeout 下载超时，可选，默认60秒

#### 返回值
无

#### 例子
```perl
# 从deepin/data目录一首歌曲到虚拟机home/mp3目录
download_local_file("music.mp3", "~/mp3");
```


### ensure_install
安装软件，如果该软件已经安装跳过安装

#### 参数
* pkglist 软件包名，可以接受列表或单个字符串

#### 返回值
无

#### 例子
```perl
# install packages from apt
ensure_install("wput");
```


### install_from_local
从deepin/data目录下安装软件（先要在deepin/data中存放相应deb包）

#### 参数
* pkglist 软件包名，可以接受列表或单个字符串

#### 返回值
无

#### 例子
```perl
# install packages from deepin/data
my @pkglist = ("curl.deb", "deepin-internal-debug.deb");
install_from_local(@pkglist);
```


### open_tty
打开并登录tty

#### 参数
* tty tty序号，默认 f1

#### 返回值
无

#### 例子
```perl
open_tty;  # 打开tty1

type_string "zip -r /var/log/X* /tmp/X-SERVER_log.zip\n";  # zip some log files
type_string "...";
```


### run_on_tty
打开登录tty，并运行命令。在运行命令后：如果屏幕静止10秒不动，并且cpu处于空闲状态，则默认表示完成命令，将退出当前tty

#### 参数
* script 需要运行的脚本
* sudo 是否需要超级用户权限运行，可选 [0, 1]，默认为 0
* tty tty序号，默认 f1
* timeout 等待超时时间，超过这个时间将发送ctrl-c命令结束程序

#### 返回值
无

#### 例子
```perl
my $cmd = "pacmd set-sink-volume 0 65536";  # volume up

run_on_tty($cmd, 0, "f2");  # 在tty2中调大系统音量，0表示普通用户执行该命令
```

### start_program
启动程序

#### 参数
* name 程序名
* needle 程序启动的needle

#### 返回值
无

#### 例子
```perl
# 启动深度音乐，详细可参考最新代码中的深度音乐测试脚本
start_program "deepin-music-player", "laucher-search-deepin-music-player";
```


