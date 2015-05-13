<!--Meta
category:用户反馈服务
title:JSONRPC接口
DO NOT Delete Meta Above -->
## 入门
### 调用 JSONRPC 接口
POST https://bugzilla.deepin.io/jsonrpc.cgi
测试用 POST http://10.0.0.231/jsonrpc.cgi

#### 请求头
Content-Type : application/json-rpc

#### 字段介绍
* method ： 要调用的方法

* version : JSONRPC 协议版本，填 1.1

* params  : 方法需要的参数

#### 传入数据
为json格式
```
{
	"method" : "Bug.get",
	"version" : "1.1",
	"params":	 {...}
}
```

#### 返回数据
json 格式

*  正常情况
```
{
	"version" : "1.1",
	"result" : { ... }
}
```
* 错误情况
```
示例：
{
   "error" : {
      "code" : 100302,
      "name" : "JSONRPCError",
      "message" : "No such a method : 'abcdefg'."
   },
   "version" : "1.1"
}

```

#### 示例
```
curl -X POST https://bugzilla.deepin.io/jsonrpc.cgi -H Content-Type:application/json-rpc  -d '{"params":{"ids":[1]},"method":"Bug.get","version":"2.0"}'

```

## 接口

### 创建反馈

#### 方法
Deepin.Feedback.putFeedback

#### 参数
* project ： 用户反馈项目下的组件

* summary :  标题

* description : 长描述

* type : 可选 "problem" 或 "suggestion"

* email : 反馈者留下的邮箱

* attachments : 附件文件的 url 列表

#### 传入数据示例

```
{
	"method" : "Deepin.Feedback.create",
	"version" : "1.1",
	"params":	 {
		"project" : "深度影院",
		"description": "asdfasdfa asdf asdf asdfas dfsd sdfas dfasdfasdf",
		"summary" : "a new feedback",
		"attachments": [
			'url1',
			'url2'
		],
 		"email" : "abc@example.org",
		"type" : "problem"
	}
}
```

### 获取产品

####方法
Deepin.Feedback.getProjects

#### 参数
无

#### 例子
```
curl -X POST https://bugzilla.deepin.io/jsonrpc.cgi -H Content-Type:application/json-rpc  -d '{"method":"Deepin.Feedback.getProjects","params":{},"version":"1.1"}'
```

####返回
有以下字段的列表：

* name : 项目名称

* icon : 项目图标

```
{
   "result" : [
      {
         "name" : "深度截图",
         "icon" : ""
      },
      {
         "name" : "深度系统安装",
         "icon" : ""
      }
   ],
   "version" : "1.1"
}



```


### 获取详细
####方法
Deepin.Feedback.getDetail

####参数
* feedback_id : 反馈id

* email : 查阅者 email

#### 返回

* title: 标题

* reporter: 报告者

* id : 反馈id

* heat : 热度

* isAttention: 是否关注，布尔值

* AttentionsCount : 关注数量

例如
```
{
   "version" : "1.1",
   "result" : {
      "reporter" : "bugs@linuxdeepin.com",
      "id" : 3,
      "heat" : 0,
      "title" : "a new bug 0.3577998327996",
      "isAttention" : false, 
      "AttentionsCount":2
   }
}

```


### 获取状态修改历史
####方法
Deepin.Feedback.getStates

####参数
* feedback_id : 反馈id
* email : 查阅者 email

#### 返回
有以下字段的列表，按时间顺序排序

* message : 修改状态时留下的评论

* ts : 状态修改时间

* status : 状态 （一级状态）

* resolution : 解决方案（二级状态）


例如
```
{
   "result" : [
      {
         "message" : "aa",
         "status" : "RESOLVED",
         "ts" : "2015-05-12 09:14:44",
         "resolution" : "FIXED"
      },
      {
         "ts" : "2015-05-12 09:15:45",
         "message" : "abasdf asdf asdf",
         "status" : "RESOLVED",
         "resolution" : "INVALID"
      }
   ],
   "version" : "1.1"
}

```


### 获取所有讨论
####方法
Deepin.Feedback.getDiscuss

####参数
* feedback_id : 反馈id
* email : 查阅者 email

#### 返回
* count : 评论总数
* comments : 评论列表
	字段：
	- id:  评论id 号，不连续的
	- ts: 评论提交时间
	- email: 评论者邮箱
	- content: 评论内容
```
{
   "version" : "1.1",
   "result" : {
      "count" : 2,
      "comments" : [
         {
            "content" : "abcdeasdfasdf asdf asdfa sdfa sdf asdf asdfadsf",
            "id" : 31,
            "ts" : "2015-05-06 11:17:36",
            "email" : "bugs@linuxdeepin.com"
         },
         {
            "email" : "elelectricface@qq.com",
            "ts" : "2015-05-12 09:55:32",
            "content" : "lkjlasjdfl ajsdlf asdf",
            "id" : 136
         }
      ]
   }
}

```

### 关注/取消关注
####方法
Deepin.Feedback.putAttention

####参数
* feedback_id : 反馈id
* email : 查阅者 email
* status: 是否关注，布尔值
	- true: 关注
	- false: 取消关注

#### 返回
关注返回 true，取消关注返回 false



### 获取关注列表
####方法
Deepin.Feedback.getAttentions

####参数
* feedback_id : 反馈id


#### 返回

* followers : 关注者，列表

* reporter : 报告者

* id : 反馈 id

* title : 反馈标题

例如

```
{
   "result" : {
      "id" : 2,
      "reporter" : "bugs@linuxdeepin.com",
      "title" : "再次测试 bugzilla 到 tower 功能",
      "followers" : [
         "1624911372@qq.com",
         "elelectricface@qq.com",
         "weixin@qq.com"
      ]
   },
   "version" : "1.1"
}

```



### 搜索框即时搜索
####方法
Deepin.Feedback.searchBox

####参数
* count: 限制数量
* keyword : 用户输入的字符

#### 返回
有以下字段的列表，按id 排序

* id : 反馈 id

* title : 反馈标题

例如
```
{
   "version" : "1.1",
   "result" : [
      {
         "id" : 1,
         "title" : "测试bugzilla to tower"
      },
      {
         "id" : 2,
         "title" : "再次测试 bugzilla 到 tower 功能"
      }
   ]
}

```


### 搜索反馈
####方法
Deepin.Feedback.searchFeedback

####参数
* keyword : 用户输入的字符

* perPageNum : 每页几条

* page : 第几页

#### 返回
* total : 搜索结果总数

* pageTotal : 页面总数

* feedbacks : 搜索到的反馈列表
	字段：
	* id : 反馈 id
	* title : 反馈标题
	* project : 项目
	* status: 状态 （一级状态）
	* resolution: 解决方案 （二级状态）
	* reporter: 报告者
	* statusChangeTs: 状态最后修改时间
	* heat : 热度

例如

```
{
   "result" : {
      "feedbacks" : [
         {
            "heat" : 8,
            "project" : "TestProduct",
            "statusChangeTs" : "2015-05-12 14:45:31",
            "status" : "RESOLVED",
            "repoter" : "bugs@linuxdeepin.com",
            "title" : "再次测试 bugzilla 到 tower 功能",
            "id" : 2,
            "resolution" : "FIXED"
         },
         {
            "status" : "RESOLVED",
            "repoter" : "bugs@linuxdeepin.com",
            "title" : "测试bugzilla to tower",
            "id" : 1,
            "resolution" : "FIXED",
            "heat" : 0,
            "project" : "TestProduct",
            "statusChangeTs" : null
         }
      ],
      "total" : 2,
      "pageTotal" : 1
   },
   "version" : "1.1"
}

```



### 获取反馈
####方法
Deepin.Feedback.getFeedbacks

####参数

* perPageNum : 每页几条

* page : 第几页

* project : 筛选项目，可选

* status : 筛选状态，可选，一般为 RESOLVED

* order: 按什么排序，类型：列表，可选
	字段可选 "id", "statusChangeTime", "heat"，默认升序排列。
	降序： 字段名在后面加 一个空格 + "DESC"，如 “id DESC”，以 id 降序排序


#### 返回
* total : 搜索结果总数

* pageTotal : 页面总数

* feedbacks : 搜索到的反馈列表
字段参见 searchFeedback 方法

### 获取我的反馈
####方法
Deepin.Feedback.getMyFeedbacks

####参数
* email : 查阅者邮箱

* perPageNum : 每页几条

* page : 第几页

* type: 关系类型,字符串
	值可选其中之一：
	- attention: 关注的
	- comment : 评论的
	- report: 报告的

* project : 筛选项目，可选

* status : 筛选状态，可选，一般为 RESOLVED

* order: 按什么排序，类型：列表，可选
	字段可选 "id", "statusChangeTime", "heat"，默认升序排列。
	降序： 字段名在后面加 一个空格 + "DESC"，如 “id DESC”，以 id 降序排序


#### 返回
* total : 搜索结果总数

* pageTotal : 页面总数

* feedbacks : 搜索到的反馈列表
字段参见 searchFeedback 方法
