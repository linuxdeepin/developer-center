<!--Meta
category:systemd
title:用户级别 service 文件编写
DO NOT Delete Meta Above -->

##用户级别 systemd service 文件编写
标签： systemd
---

### 参考文档
[openSUSE:How to write a systemd service](https://zh.opensuse.org/index.php?title=openSUSE:How_to_write_a_systemd_service&variant=zh-sg)

[Arch Linux Wiki Systemd Writing_unit_files](https://wiki.archlinux.org/index.php/Systemd_%28%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%29#Writing_unit_files)

### 文件位置

系统管理员编写的服务配置文件放在 /etc/systemd/system

软件打包的服务配置文件放在 /usr/lib/systemd

用户级别的放在 $HOME/.config/systemd/user

sytemd.unit [Unit] 段参考

http://www.freedesktop.org/software/systemd/man/systemd.unit.html

systemd.service [Service] 段参考

http://www.freedesktop.org/software/systemd/man/systemd.service.html

### 服务开机自启动

要让用户级别的服务脚本在用户未登陆的情况下自启动，并且用户注销登录后服务依旧运行，需要设置 用户 Linger 属性为 "Yes" 。

[更详细](https://wiki.archlinux.org/index.php/Systemd/User#Automatic_start-up_of_systemd_user_instances)

```
# 为用户启用 linger
loginctl enable-linger $USER

# 查看用户相关信息
loginctl show-user $USER

# 为户禁用 linger
loginctl disable-linger $USER
```

### 例子
dtask server 的例子
```
[Unit]
Description = Dtask Server
After= networking.service

[Service]
Type = simple
ExecStart = /usr/bin/perl -I /home/gerrit/dtask.deepin.io/lib \
        /home/gerrit/dtask.deepin.io/script/dtask_server.pl daemon -l http://*:3300
Restart = always
RestartSec= 5s

[Install]
WantedBy = default.target
```


## 命令
接入用户级别的 systemctl 都要在命令 systemctl 后加 --user

重新载入变动的 service 文件
```
systemctl --user daemon-reload
```

### 启用服务自启动

```
systemctl --user enable foo.service
```
将会创建符号链接

### 禁用服务自启动
```
systemctl --user disable foo.service
```

### 查看服务状态
```
systemctl --user status foo.service
```

### 查看日志
遇到服务不起来的情况先检查相关的日志
```
journalctl --user
```