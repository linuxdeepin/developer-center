<!--Meta
category:开发规范
title:Gerrit参与人员要求
DO NOT Delete Meta Above -->

###CL合并者
程序自动把控的基本要求:

* jenkins + 1
* CodeReview + 2

人为把控的要求:

* 涉及到debian目录下的修改，需要build-config +1
* 涉及到最终用户可看到的文字变动，需要i18n + 1（翻译同学需要回复了翻译tower任务地址）
* 涉及到QA人员参与的，需要QA人员给Verified + 1
* 要求CL提交者进行合理的reviewers添加
* 要求CL的commit格式正确、内容合理
* code review人员注意，在代码组织上若无明显优劣方式,则以尊重代码书写者为主

###CL提交者

* 正确的commit格式，统一使用git commit调出编辑器编写commit，会有对应commit错误警告，commit格式如下（实例参考[CL6176](https://cr.deepin.io/#/c/6176/) ）:
```
模块: 一行简述
空行
具体描述 (可选)
空行
bugzilla相关bug地址(若有对应bugzilla条目则必须添加)
空行
Change-Id: (配置好git review会自动添加)
```
* 若有对应bugzilla任务则在commit中最后加上相关链接
* 根据CL的特点增加对应的reviewers。（Hacking Day当天要求增加顾问团所有成员作为reviewers）

###QA
1.  Bugzilla对应条目链接要能在CL的commit信息中找到 (强制性，由CL提交者填写，QA和审核者共同督促)
    * 方便QA以及其他人员获得更多此CL的相关信息
    * 方便QA对bugzilla的处理
    * 方便宣传组定期查找此类CL做版本更新记录
2. 帮助开发人员验证功能完整性
    * 拒绝测试代码更改者自己都完全未测试的代码
    * 少数特殊情况除外，比如提交者测试需要耗费很长时间，而QA已经有对应测试环境

###系统打包人员
1. 对debian目录的修改进行验证 (强制性)
2. 对其他涉及到包生成、系统修改等代码进行验证
3. 一般审查者

###i18n组（翻译组）
任何参与人员如果发现问题，请及时给出负分(若无合适标签则给Verified-1)阻止CL被意外合并



# hackingday时如何提交CL

## 很多项目都不是在master分支上进行开发的，所以需要找到项目负责人询问修改这个bug需要使用的分支

1.  TODO: tower创建的时候就应该标记此bug需要在哪个分支修复
2.  TODO: 开发人员补充tag信息，完善文档

多问对应开发人员

## 切换到此分支，以此作为基础分支，比如此分支为release/2.1

    git clone ssh://foo@cr.deepin.io:29418/bar
    cd bar
    git checkout origin/release/2.1

## 在base的基础上创建一个新的分支作为提交CL时使用的分支

    git checkout -b hackingday/小白/4512
    -b 后面是这个CL的topic信息， 请使用固定的格式
    hackingday/{队名}/{bugid}

windows版本的git review如果无法自动生成topic则需要增加-t参数
 
    git review -t hackingday/小白/4512 ${target_branch}

这样可以直接通访问 <https://cr.deepin.io/#/q/topic:^hackingday.*> 
来查看hackingday相关的CL，
若只想查看当前活动的CL，则在搜索框上增加 *after: 2015-8-06* 这种限定时间

## fix bug

修改后

    git add where/you/modified/codes
    git commit

## 编写commit信息

    summary(第一行不要超过72个字符)
    {此处必须空一行}
    description (optional)

## 提交CL

提交CL需要注意2点
1.  一个CL只能包含一个commit
2.  提交时候需要知道自己要提交到那个分支上，默认是master(但这个一般都是错的)

    git review release/2.1(步骤3中checkout出来的那个分支)

一个CL只能有一个commit，而且一个bug原则上只允许一个CL(多项目不算)。
若多次修改请使用git commit &#x2013;amend;
若已经提交了，可以使用git rebase -i 的方式压缩多个commit到一个上面

提交完了CL后，请在网页上逐一查看自己提交的代码是否和预期一样。
经常会出现一些没有必要的增加空行这种修改。以及不小心提交了一些其他文件
