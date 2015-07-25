<!--Meta
category:OpenQA
title:OpenQA 测试CL提交流程
DO NOT Delete Meta Above -->

### ** CL提交流程**

#### 1、一个CL对应一个新的测试，尽量不要两个测试一起提交

提交:

#### 2、git review -t "你新添加或修改的测试依赖的环境变量"  
基本测环境变量（如果安装语言用户名等）不用添加

#### 3、提交代码后可以在gerrit看到你的测试触发的jenkins任务  
CL检测完毕后会在jenkins的控制台输出最后列出测试结果和URL
![](/OpenQA/cl_check_jenkins.png)
![](/OpenQA/cl_check_jenkins_2.png)

#### 4、jenkins检测通过是合并代码的基本条件  
通过后可以告知我（唐财俊），review通过后会将代码合并到仓库中

#### 5、如果失败了，在jenkins控制台输出也会列出结果和URL  
如果CL检测失败了，对前一提交修正的patch不要使用 
```shell
git commit -m msg 
```
而是使用
```shell
git commit --amend
```
将修正加入前一个提交，避免在gerrit上同一个问题出现两个commit了
