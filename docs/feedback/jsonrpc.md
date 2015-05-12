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

返回
{
   "version" : "1.1",
   "result" : {
      "bugs" : [
         {
            "cf_fixversion" : "",
            "id" : 1,
            "component" : "TestComponent",
            "cf_probability" : "稳定出现",
            "creator" : "yujingmei@linuxdeepin.com",
            "is_open" : false,
            "see_also" : [],
            "platform" : "PC",
            "is_confirmed" : true,
            "qa_contact" : "",
            "cf_techassessment" : "---",
            "whiteboard" : "",
            "product" : "TestProduct",
            "assigned_to" : "yujingmei@linuxdeepin.com",
            "blocks" : [],
            "creation_time" : "2015-01-23T08:51:00Z",
            "last_change_time" : "2015-03-23T07:13:30Z",
            "is_creator_accessible" : true,
            "alias" : null,
            "dupe_of" : null,
            "cf_secondselect" : "---",
            "priority" : "Lowest",
            "cf_firstselect" : "---",
            "cc" : [
               "852533897@qq.com",
               "bugzilla@linuxdeepin.com",
               "songwentai@linuxdeepin.com"
            ],
            "resolution" : "FIXED",
            "summary" : "222",
            "groups" : [],
            "status" : "CLOSED",
            "depends_on" : [],
            "cf_review" : "---",
            "flags" : [],
            "classification" : "Unclassified",
            "cf_contactinfo" : "",
            "keywords" : [],
            "cf_bugorreq" : "---",
            "version" : "unspecified",
            "op_sys" : "Linux",
            "severity" : "normal",
            "target_milestone" : "---",
            "url" : "",
            "is_cc_accessible" : true
         }
      ],
      "faults" : []
   }
}

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

返回


```


### 获取详细
####方法
Deepin.Feedback.getDetail

####参数
* feedback_id : 反馈id
* email : 查阅者 email

#### 返回
```
{
   "version" : "1.1",
   "result" : {
      "reporter" : "bugs@linuxdeepin.com",
      "id" : 3,
      "heat" : 0,
      "title" : "a new bug 0.3577998327996",
      "in_cc_list" : false,
      "cc_count" : 2
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
```
{
   "version" : "1.1",
   "result" : {
      "count" : 2,
      "comments" : [
         {
            "content" : "abcdeasdfasdf asdf asdfa sdfa sdf asdf asdfadsf",
            "id" : "31",
            "ts" : "2015-05-06 11:17:36",
            "email" : "bugs@linuxdeepin.com"
         },
         {
            "email" : "elelectricface@qq.com",
            "ts" : "2015-05-12 09:55:32",
            "content" : "lkjlasjdfl ajsdlf asdf",
            "id" : "136"
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
* status: true or false

#### 返回

```
{
   "result" : true or false,
   "version" : "1.1"
}

```


### 获取关注列表
####方法
Deepin.Feedback.getAttentions

####参数
* feedback_id : 反馈id


#### 返回

例如

```
{
   "version" : "1.1",
   "result" : {
      "id" : "3",
      "reporter" : "bugs@linuxdeepin.com",
      "title" : "a new bug 0.3577998327996",
      "cc" : [
         "elelectricface@qq.com"
      ]
   }
}


```



### 搜索框即时搜索
####方法
Deepin.Feedback.searchBox

####参数
* count: 限制数量
* keyword : 用户输入的字符

#### 返回
例如

```
{
   "version" : "1.1",
   "result" : [
      {
         "title" : "测试bugzilla to tower",
         "id" : "1"
      },
      {
         "title" : "再次测试 bugzilla 到 tower 功能",
         "id" : "2"
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

* page : 第一页

#### 返回
* total : 搜索结果总数

* pageTotal : 页面总数

* feedbacks : 搜索到的反馈列表
例如
```
{
   "version" : "1.1",
   "result" : {
      "total" : 2,
      "pageTotal" : 1,
      "feedbacks" : [
         {
            "status" : "RESOLVED::FIXED",
            "change_ts" : "2015-05-12 09:07:13",
            "id" : 1,
            "project" : "TestProduct::TestComponent",
            "title" : "测试bugzilla to tower",
            "repoter" : "bugs@linuxdeepin.com",
            "heat" : 0
         },
         {
            "status" : "IN_PROGRESS::",
            "change_ts" : "2015-05-12 09:24:32",
            "project" : "TestProduct::用户反馈",
            "id" : 2,
            "heat" : 8,
            "repoter" : "bugs@linuxdeepin.com",
            "title" : "再次测试 bugzilla 到 tower 功能"
         }
      ]
   }
}


```



### 获取反馈
####方法
Deepin.Feedback.getFeedbacks

####参数

* perPageNum : 每页几条

* page : 第一页

* project : 筛选项目，可选

* status : 筛选状态，可选，一般为 RESOLVED

* order: 按什么排序，类型：列表，可选
	字段可选 "id", "statusChangeTime", "heat"，默认升序排列。
	降序： 字段名在后面加 一个空格 + "DESC"，如 “id DESC”，以 id 降序排序


#### 返回
* total : 搜索结果总数

* pageTotal : 页面总数

* feedbacks : 搜索到的反馈列表


### 获取我的反馈
####方法
Deepin.Feedback.getMyFeedbacks

####参数
* email : 查阅者邮箱

* perPageNum : 每页几条

* page : 第一页

* type: 类型
	值可选 其中一个：
	- cc 关注的
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

