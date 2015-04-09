<!--Meta
category:DTask
title:Tower 接口
DO NOT Delete Meta Above -->


### tower 认证

POST /tower/authorization

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
