<!--Meta
category:OpenQA
title:OpenQA测试钩子和test_flags
DO NOT Delete Meta Above -->

### ** 测试钩子 **

* #### post_fail_hook
在一个测试模块失败后自动调用


* #### pre_run_hook
在一个测试模块运行前自动调用 (可用于准备这一项测试的环境)


* #### post_run_hook
在一个测试模块执行成功后自动调用


&emsp; softwarebasetest.pm模块中定义了默认钩子，在一个测试模块头部use strict;后添加use base 'softwarebasetest'即可引入，具体钩子设置看deepin/lib/softwarebasetest.pm源码。  
&emsp; softwarebasetest.pm 只是做了一个抽象层，不一定使用于所有测试，在导入了'softwarebasetest'后可以在测试模块中重新定义新的钩子函数，将softwarebasetest的钩子函数覆盖掉。  

 ** \*\* (如deepin/lib/下没有softwarebasetest.pm模块，请将代码更新到最新版本) **


---
** test_flags **
---

test_flags 函数可选的参数有：** fatal ** 、** milestone ** 、** important **  

 参数 | 说明
 --- | ---
**fatal** | 致关重要，如果出错将直接关闭虚拟机，视为严重错误
**milestone** | 里程碑，如果测试测试成功后将更新lastgood快照位置到当前位置
**important** | 失败将标志这整个测试失败，不会回滚，不会停止测试<br>（个人感觉这个用的地方不是很多，因为软件测试失败后需要回滚，否则会影响下一个测试；安装测试失败了为严重错误，将直接关闭虚拟机，停止测试）
** 空<br> return {} ** | 失败后回滚lastgood快照位置 （在第一次进入桌面并完成新手引导后会做lastgood快照）


---
更多详细请参考新测试脚本

