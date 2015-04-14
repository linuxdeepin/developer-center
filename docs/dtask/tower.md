<!--Meta
category:DTask
title:Tower 接口
DO NOT Delete Meta Above -->


### tower 认证

POST /services/tower/token

#### Form 参数
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

#### 例子
```
curl -d 'username=abcdefg&password=123456' -X POST http://10.0.0.231/services/tower/token
```

### 获取 tower 的团队成员们
GET /services/tower/members

#### 请求头
Tower-Token: access_token

#### 返回数据
如
```
{
   "result" : [
      {
         "guid" : "44d8b81df5db4aa2a4eb001c100247ba",
         "name" : "成员一"
      },
      {
         "name" : "成员二",
         "guid" : "d9748b3d998640469f894b6b8bfb2e46"
      },
      {
         "guid" : "e60eab8489484d74a0eef6213041e630",
         "name" : "成员三"
      },
      ...
   ],
   "error" : false
}
```

#### 例子
```
curl -H 'Tower-Token: 44d8b81df5db4aa2a4eb001c100247ba' -X GET http://10.0.0.231:3000/services/tower/members
```

### 获取 tower 的项目们
GET /services/tower/projects

#### 请求头
Tower-Token: access_token


#### 返回数据
如
```
{
   "result" : [
      {
         "guid" : "44d8b81df5db4aa2a4eb001c100247ba",
         "name" : "项目一"
      },
      {
         "name" : "项目二",
         "guid" : "d9748b3d998640469f894b6b8bfb2e46"
      },
      {
         "guid" : "e60eab8489484d74a0eef6213041e630",
         "name" : "项目三"
      },
      ...
   ],
   "error" : false
}
```


#### 例子
```
curl -H 'Tower-Token: 44d8b81df5db4aa2a4eb001c100247ba' -X GET http://10.0.0.231:3000/services/tower/projects
```

### 获取 tower 某个项目下的 todolist 们

GET /services/tower/projects/:project_guid/todolists

#### 请求头
Tower-Token: access_token

#### URL 参数
project_guid ： 项目guid

#### 返回数据
如
```
{
   "result" : [
      {
         "guid" : "44d8b81df5db4aa2a4eb001c100247ba",
         "name" : "列表一"
      },
      {
         "name" : "列表二",
         "guid" : "d9748b3d998640469f894b6b8bfb2e46"
      },
      {
         "guid" : "e60eab8489484d74a0eef6213041e630",
         "name" : "列表三"
      },
      ...
   ],
   "error" : false
}
```



#### 例子
```
curl -H 'Tower-Token: 44d8b81df5db4aa2a4eb001c100247ba' -X GET http://localhost:3000/services/tower/projects/d9748b3d998640469f894b6b8bfb2e46/todolists
```