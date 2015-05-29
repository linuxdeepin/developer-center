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
	* result: 结果数据
	* version: JSONRPC 版本
```
{
	"version" : "1.1",
	"result" : { ... }
}
```

* 错误情况
	* error : 错误
		* code : 错误代码
		* name : 错误名
		* message : 出错信息
	* version ： JSONRPC 版本

例如

```

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
用 curl 调用 Bugzilla JSONRPC 服务 Bug.get 方法获取某个 bug 的详细信息。
```
curl -X POST https://bugzilla.deepin.io/jsonrpc.cgi -H Content-Type:application/json-rpc  -d '{"params":{"ids":[1]},"method":"Bug.get","version":"2.0"}'

```

## 接口

### 提交反馈

#### 方法
Deepin.Feedback.putFeedback

#### 参数
* project ： 用户反馈项目下的组件
* summary :  标题
* description : 长描述
* type :  只可填 "problem"  或 "suggestion"
* email : 反馈者留下的邮箱
* attachments : 附件列表，类型列表，可选
	- url : 附件url
	- name : 文件名
	- type : 文件类型

#### 传入数据示例

```
{
	"method" : "Deepin.Feedback.putFeedback",
	"version" : "1.1",
	"params":	 {
		"project" : "深度截图",
		"description": "asdfasdfa asdf asdf asdfas dfsd sdfas dfasdfasdf",
		"summary" : "a new feedback",
		"attachments": [
			{
				"name" : "abcdef.png",
				"url" : "https://a.com/sdfsdffasdf"
			}
		],
 		"email" : "abc@example.org",
		"type" : "problem"
	}
}
```

### 获取项目

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
* category : 项目分类

```
{
   "result" : [
      {
         "category" : "application",
         "name" : "深度截图",
         "icon" : null
      },
      {
         "name" : "深度系统安装",
         "icon" : "http://test_bugzilla.deepin.io/extensions/DeepinFeedback/web/products/%E6%B7%B1%E5%BA%A6%E7%B3%BB%E7%BB%9F%E5%AE%89%E8%A3%85.png",
         "category" : "system"
      }
   ],
   "version" : "1.1"
}

```


### 获取详细
####方法
Deepin.Feedback.getDetail

####参数
* feedbackID : 反馈id
* secretKey : 密钥
* email : 查阅者邮箱,可选

#### 返回

* id : 反馈id
* reporter: 报告者
	- id 报告者 id
	- email 报告者邮箱

* title: 标题
* description : 问题描述
* attachments : 附件列表，类型列表
	有以下字段的列表
	- url : 附件url
	- name : 文件名
	- type : 文件类型

* statuschangeTs : 状态最后修改时间
* creationTs : 反馈提交时间
* heat : 热度
* isAttention: 是否关注，布尔值
* attentionsCount : 关注数量
* status : 状态 （一级状态）
* resolution : 解决方案 （二级状态）


例如
```
{
   "result" : {
      "statusChangeTs" : "2015-05-18T06:21:00Z",
      "isAttention" : false,
      "status" : "UNCONFIRMED",
      "resolution" : "",
      "title" : "add_attachment test",
      "attachments" : [
         {
            "name" : "abc",
            "url" : "url1",
            "type" : "gif"
         }
      ],
      "heat" : 5,
      "creationTs" : "2015-05-18T06:21:00Z",
      "attentionsCount" : 1,
      "id" : 1073,
      "reporter" : {
         "id" : 18,
         "email" : "electricface@qq.com"
      },
      "description" : "test add attachments"
   },
   "version" : "1.1"
}
```


### 获取状态修改历史
####方法
Deepin.Feedback.getStates

####参数
* secretKey : 密钥
* feedbackID : 反馈id
* email : 查阅者邮箱，可选

#### 返回
有以下字段的列表，按时间顺序排序

* message : 修改状态时留下的评论
* ts : 状态修改时间
* status : 状态 （一级状态）
* resolution : 解决方案（二级状态）
* who : 状态修改操作者的邮箱

例如
```
{
   "result" : [
      {
         "resolution" : "",
         "who" : "bugs@linuxdeepin.com",
         "ts" : "2015-04-09T05:12:00Z",
         "status" : "UNCONFIRMED",
         "message" : null
      },
      {
         "status" : "IN_PROGRESS",
         "message" : "zxcvz asdfas",
         "ts" : "2015-05-12T01:24:32Z",
         "who" : "elelectricface@qq.com",
         "resolution" : ""
      },
      {
         "ts" : "2015-05-12T06:45:31Z",
         "who" : "elelectricface@qq.com",
         "status" : "RESOLVED",
         "message" : "aaa",
         "resolution" : "FIXED"
      }
   ],
   "version" : "1.1"
}

```


### 获取所有讨论
####方法
Deepin.Feedback.getDiscuss

####参数
* feedbackID : 反馈id
* email : 查阅者 email，可选
* secretKey : 密钥

#### 返回
* count : 评论总数
* comments : 评论列表
	字段：
	- id:  评论id 号，不连续的
	- ts: 评论提交时间
	- author : 评论者
		* email: 评论者邮箱
		* id : 评论者id
	- content: 评论内容
	- attachments : 附件列表，类型列表
		* url : 附件url
		* name : 文件名
		* type : 文件类型

例如
```
{
   "result" : {
      "count" : 2,
      "comments" : [
         {
            "attachments" : [
               {
                  "url" : "http://abcdef.com/adfasdf",
                  "name" : "abcdef.png",
                  "type" : "image/jpeg"
               }
            ],
            "content" : "ab  def game",
            "id" : 1233,
            "ts" : "2015-05-18T06:36:56Z",
            "author" : {
               "id" : 3,
               "email" : "user1@linuxdeepin.com"
            }
         },
         {
            "attachments" : null,
            "ts" : "2015-05-18T06:38:34Z",
            "id" : 1234,
            "content" : "ab adf aasdf __===",
            "author" : {
               "email" : "user2@linuxdeepin.com",
               "id" : 4
            }
         }
      ]
   },
   "version" : "1.1"
}

```

### 提交评论
#### 方法
Deepin.Feedback.putDiscuss

#### 参数
* feedbackID : 反馈id
* email : 提交者邮箱
* secretKey : 密钥
* attachments : 附件列表，类型：列表，可选
	有以下字段的列表
	- url : 附件url
	- name : 文件名
	- type : 文件类型

#### 返回
* id : 评论 id

### 关注/取消关注
####方法
Deepin.Feedback.putAttention

####参数
* feedbackID : 反馈id
* email : 查阅者 email
* secretKey : 密钥
* status: 是否关注，布尔值
	- true: 关注
	- false: 取消关注

#### 返回
* attentionsCount : 关注人数


### 获取关注列表
####方法
Deepin.Feedback.getAttentions

####参数
* feedbackID : 反馈id
* secretKey : 密钥


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
有以下字段的列表，按id 降序排序

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
只搜索标题
####方法
Deepin.Feedback.searchFeedback

####参数
* keyword : 用户输入的字符
* perPageNum : 每页几条
* page : 第几页
* project : 筛选项目，可选
* status : 筛选状态，可选，一般为 RESOLVED
* order: 按什么排序，类型：列表，可选

	排序字段可选 "id", "statusChangeTime", "heat"，默认升序排列。
	降序： 字段名在后面加 一个空格 + "DESC"，如 “id DESC”，以 id 降序排序


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
		- id : 报告者id
		- email : 报告者邮箱
	* creationTs : 反馈提交时间
	* statusChangeTs: 状态最后修改时间
	* heat : 热度

例如

```
{
   "version" : "1.1",
   "result" : {
      "total" : 2,
      "pageTotal" : 1,
      "feedbacks" : [
         {
            "statusChangeTs" : "2015-05-12T06:45:31Z",
            "heat" : 8,
            "title" : "再次测试 bugzilla 到 tower 功能",
            "status" : "RESOLVED",
            "resolution" : "FIXED",
            "project" : "TestProduct",
            "id" : 2,
            "reporter" : {
               "id" : 1,
               "email" : "bugs@linuxdeepin.com"
            }
         },
         {
            "resolution" : "FIXED",
            "project" : "TestProduct",
            "reporter" : {
               "email" : "bugs@linuxdeepin.com",
               "id" : 1
            },
            "id" : 1,
            "statusChangeTs" : null,
            "title" : "测试bugzilla to tower",
            "heat" : 0,
            "status" : "RESOLVED"
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
* page : 第几页
* project : 筛选项目，可选
* status : 筛选状态，可选，一般为 RESOLVED
* order: 按什么排序，类型：列表，可选

	排序字段可选 "id", "statusChangeTime", "heat"，默认升序排列。
	降序： 字段名在后面加 一个空格 + "DESC"，如 “id DESC”，以 id 降序排序


#### 返回
* total : 搜索结果总数
* pageTotal : 页面总数
* feedbacks : 搜索到的反馈列表
字段参见 searchFeedback 方法

### 获取我的反馈
#### 方法
Deepin.Feedback.getMyFeedbacks

#### 参数
* secretKey : 密钥
* email : 查阅者邮箱
* perPageNum : 每页几条
* page : 第几页

* type: 关系类型,字符串
	值可选其中之一：
	- "report" : 报告的
	- "attention": 关注的
	- "comment" : 评论的

* project : 筛选项目，可选
* status : 筛选状态，可选，一般为 RESOLVED
* order: 按什么排序，类型：列表，可选

	排序字段可选 "id", "statusChangeTime", "heat"，默认升序排列。
	降序： 字段名在后面加 一个空格 + "DESC"，如 “id DESC”，以 id 降序排序


#### 返回
* total : 搜索结果总数
* pageTotal : 页面总数
* feedbacks : 搜索到的反馈列表

    字段参见 searchFeedback 方法,但获取的 feedback 附加了一个额外字段 "visible",布尔值，表示用户是否可见此反馈。

### 获取用户的反馈
####方法
Deepin.Feedback.getUserFeedbacks

####参数
* secretKey : 密钥
* userID : 用户id
* perPageNum : 每页几条
* page : 第几页
* type: 关系类型,字符串
	值可选其中之一：
	- "report" : 报告的
	- "attention" : 关注的


* project : 筛选项目，可选
* status : 筛选状态，可选，一般为 RESOLVED
* order: 按什么排序，类型：列表，可选

	排序字段可选 "id", "statusChangeTime", "heat"，默认升序排列。
	降序： 字段名在后面加 一个空格 + "DESC"，如 “id DESC”，以 id 降序排序


#### 返回
* total : 搜索结果总数
* pageTotal : 页面总数
* feedbacks : 搜索到的反馈列表

	字段参见 searchFeedback 方法

