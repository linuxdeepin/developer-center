<!--Meta
category:OpenQA
title:Test Developer API
DO NOT Delete Meta Above -->

## OpenQA Test Developer API Docs

（说明：perl中无True和False，为了好表达，以下将undef、空字符串、0唤为False，其他唤为True）

### ** assert_screen **
对比needle  
匹配结果会影响本次测试结果

#### 参数
* NEEDLE neelde名字
* TIMEOUT 最长等待时间

#### 返回值
True 或 False

#### 例子
```perl
# 预测 10 秒内出现对应needle，若不出现则标识此次对比失败
assert_screen "your-needle-name", 10;
```

### ** assert_and_click **
对比needle，若匹配，则点击needle匹配区域的最中间部位  
匹配结果会影响本次测试结果

#### 参数
* NEEDLE neelde名字
* BUTTON 键位名，默认为"left"，可选值："left" 、"right" 、"middle"
* TIMEOUT 最长等待时间

#### 返回值
无

#### 例子
```perl
assert_and_dclick "launcher-btn-click";  # 匹配名字为launcher-btn-click的needle，如果匹配成功，则单击needle中间部位
```


### ** assert_and_dclick **
对比needle，若匹配，则双击needle匹配区域的最中间部位
匹配结果会影响本次测试结果

#### 参数
* NEEDLE neelde名字
* BUTTON 键位名，默认为"left"，可选值："left" 、"right" 、"middle"
* TIMEOUT 最长等待时间

#### 返回值
无

#### 例子
```perl
assert_and_dclick "launcher-btn-click";  # 匹配名字为launcher-btn-click的needle，如果匹配成功，则双击needle中间部位
```


### ** check_screen **
对比needle，和assert_screen区别是，对比的结果对测试无影响
#### 参数
* NEEDLE neelde名字
* TIMEOUT 最长等待时间

#### 返回值
True 或 False

#### 例子
```perl
# 10秒内出现对应needle则执行if语句中的内容
if (check_screen "your-needle-name", 10){
    # do your work
}

```

### ** check_var **

验证环境变量值

#### 参数
* NAME 变量名
* CONTENT 对比值

#### 返回值
对比在开始测试前预设的变量值

#### 例子
```perl
openqa-test FOO=BAR   # 启动一个测试，设置环境变量FOO的值为BAR

# 在测试脚本中调用  
check_var "FOO"， "BAR";  # 返回1
```

### ** get_var **

获取环境变量值

#### 参数
* NAME 变量名

#### 返回值
返回在开始测试前预设的变量值，若没有设置改环境变量则返回undef

#### 例子
```perl
openqa-test FOO=BAR   # 启动一个测试，设置环境变量FOO的值为BAR

# 在测试脚本中调用：  
get_var "FOO";  # 返回BAR
```

### ** make_snapshot **
生成快照
生成的快照存储在虚拟机硬盘文件中，可通过以下命令列出硬盘所有快照
```shell
qemu-img snapshot -l disk.img  # disk.img 是虚拟机硬盘文件

# 虚拟机硬盘文件存放位置为 /var/lib/openqa/pool/#work-id#/raid/1
```

#### 参数
* NAME 快照名

#### 返回值
无

#### 例子
```perl
make_snapshot "snapshot-name";
```

### ** mouse_click **
移动点击事件

#### 参数
* BUTTON 键位，默认为"left"，可选值："left" 、"right" 、"middle"
* TIME 点击时，按下按键到放开按键的间隔，默认为0.15（这个值一般不需要修改）

#### 返回值
无

#### 例子
```perl
mouse_click "right";  # 右键
```


### ** mouse_dclick **
移动点击事件

#### 参数
* BUTTON 键位，默认为"left"，可选值："left" 、"right" 、"middle"
* TIME 点击时，按下按键到放开按键的间隔，和两次点击间的间隔，默认为0.10（这个值一般不需要修改）

#### 返回值
无

#### 例子
```perl
mouse_dclick;  # 左键双击
```


### ** mouse_hide **

隐藏鼠标，将鼠标移动到右上角隐藏（用于对比匹配率要求较高的测试）

#### 参数
无

#### 返回值
无

#### 例子
```perl
# 移动鼠标到右上角，然后截图
mouse_hide;
save_screenshot;
```


### ** mouse_set **
移动鼠标

#### 参数
* X x坐标
* Y y坐标

#### 返回值
无

#### 例子
```perl
mouse_set 1023, 767;  # 移动到右下角，召唤控制中心
```


### ** load_snapshot **
加载快照  
快照名可通过下面命令查看
```shell
# 列出硬盘所有快照
qemu-img snapshot -l disk.img  # disk.img 是虚拟机的硬盘文件
```

#### 参数
* NAME 快照名

#### 返回值
无

#### 例子
```perl
load_snapshot "snapshot-name";
```


### ** save_screenshot **

保存截图，所有保存的截图都会在测试结果中列出

#### 参数
无

#### 返回值
无

#### 例子
```perl
save_screenshot;
```

### ** send_key **

发送特殊按键或按键组合

#### 参数
* KEY 发送的按键组合 **注意：多个按键的连接符是“-”，不是“+”**
* WAITIDLE（可选）可设值 [1 | 0]，是否等待cpu空闲后返回，最大等待19秒  
（比如说你发送了一个按键组合，启动了某些操作，虚拟机cpu使用率升高了，此时send_key函数进入等待状态，直到cpu使用率变为空闲状态或超过了最大等待时间此函数才结束）

#### 返回值
无

#### 例子
```perl
send_key "ctrl-alt-t"     # 召唤终端
```

#### 附所有特殊按键表达式：
```java
alt
backspace
ctrl
delete
down
end
equal
esc
home
insert
left
meta
minus
pgdn
pgup
ret
right
shift
spc
sysrq
tab
up
win
```


### ** type_string **

输入字符

#### 参数
* STRING 字符

#### 返回值
无

#### 例子
```perl
type_string "deepin";
```


### ** wait_idle **
进入睡眠，等待cpu空闲  
比如在执行了一条复制文件指令，但是完成时间未知，则可用此函数接管

#### 参数
* TIMEOUT 最大等待时间

#### 返回值
无

#### 例子
```perl
wait_idle 20;
```

### ** wait_still_screen **
等待屏幕画面停止变化

#### 参数
* STILLTIME 停止变化持续时间
* TIMEOUT 最大等待时间
* SIMLEVEL 前后对比图片相似百分比

#### 返回值
1 在TIMEOUT时间内停止变化了  
0 超时

#### 例子
```perl
# 暂无
```
