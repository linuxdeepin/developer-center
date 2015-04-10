<!--Meta
category:DTask
title:Tower 接口
DO NOT Delete Meta Above -->


### tower 认证

POST /tower/token

#### 参数
* username
* password

#### 返回数据
如
```
{
	"error":false,
	"result":{
		"expires_in":2592000,
		"access_token":"a198a4f7b8b98a16086190530e2d71ea"
	}
}
```


### 获取 tower 的项目们
GET /tower/projects

#### 请求头
Tower-Token: access_token

#### 参数
无

#### 返回数据
如
```
{
	"44d8b81df5db4aa2a4eb001c100247ba":"成员一",
	"d9748b3d998640469f894b6b8bfb2e46":"成员二",
	"e60eab8489484d74a0eef6213041e630":"成员三"
	...
}
```


### 获取 tower 某个项目下的 todolist 们

GET /tower/projects/:project_guid/todolists

#### 请求头
Tower-Token: access_token

#### 参数
project_guid ： 项目guid

#### 返回数据
如
```
{
	"44d8b81df5db4aa2a4eb001c100247ba":"项目一",
	"d9748b3d998640469f894b6b8bfb2e46":"项目二",
	"e60eab8489484d74a0eef6213041e630":"项目三"
	...
}
```
