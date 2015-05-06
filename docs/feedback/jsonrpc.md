<!--Meta
category:用户反馈服务
title:JSONRPC接口
DO NOT Delete Meta Above -->

# 用户反馈 JSONRPC 接口

### 调用 JSONRPC 接口
POST https://bugzilla.deepin.io/jsonrpc.cgi

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
```
{
	"version" : "1.1",
	"result" : { ... }
}
```

示例
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
Deepin.Feedback.create 





### 参数
* product ： 产品

* version ： 版本

* summary :  标题

* description : 长描述

* type : 可选 "problem" 或 "suggestion"

* email : 反馈者留下的邮箱

* attachments : 附件文件的 url 列表

### 传入数据示例

```
{
	"method" : "Deepin.Feedback.create",
	"version" : "1.1",
	"params":	 {
		"product" : "TestProduct",
		"version" :"1.0",
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
