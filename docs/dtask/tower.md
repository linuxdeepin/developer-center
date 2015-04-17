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
		"access_token":"44d8b81df5db4aa2a4eb001c100247ba"
	}
}
```

#### 例子
```
curl -d 'username=abcdefg&password=123456' -X POST http://10.0.0.231:3000/services/tower/token

http POST http://10.0.0.231:3000/services/tower/token username=abcdefg password=123456
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

http GET http://10.0.0.231:3000/services/tower/members Tower-Token:44d8b81df5db4aa2a4eb001c100247ba
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

http GET http://10.0.0.231:3000/services/tower/projects Tower-Token:44d8b81df5db4aa2a4eb001c100247ba
```

### 获取 tower 某个项目下的 todolist 们

GET /services/tower/projects/:project_guid/todolists

#### 请求头
Tower-Token: access_token

#### URL 参数
* project_guid ： 项目guid

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
curl -H 'Tower-Token: 44d8b81df5db4aa2a4eb001c100247ba' -X GET http://10.0.0.231:3000/services/tower/projects/d9748b3d998640469f894b6b8bfb2e46/todolists

http GET http://10.0.0.231:3000/services/tower/projects/d9748b3d998640469f894b6b8bfb2e46/todolists Tower-Token:44d8b81df5db4aa2a4eb001c100247ba
```

### 获取 todo 的信息
GET /services/tower/todos/:todo_guid

#### URL 参数
* todo_guid

#### 返回数据
```
{
   "error" : false,
   "result" : {
        ...
   }
}

```

#### 例子
```
curl -H 'Tower-Token:44d8b81df5db4aa2a4eb001c100247ba ' http://10.0.0.231:3000/services/tower/todos/d6609cfc0d914888ae1cdd8a6f7f33f1

http http://10.0.0.231:3000/services/tower/todos/d6609cfc0d914888ae1cdd8a6f7f33f1 Tower-Token:44d8b81df5db4aa2a4eb001c100247ba
```

### 导入 bugzilla 的某个bug

PUT /services/tower/import/bugzilla_bug

#### 功能
将 bugzilla 的 bug 导入到 tower, 在指定的 tower todolist 下创建新的 todo，新建立的 todo 标题为 “#bugzila #bug_id + bug 标题”，内容为“from: bug_url”，并将它与相应的 bug 关联起来。
同时也在 bugzilla 对于 bug 的页面增加一条评论，内容包含 todo 的 url。

#### 请求头
Tower-Token: access_token

#### Form 参数
* todolist_guid : tower todolist guid
* bug_id: bugzilla bug id

#### 返回数据

当调用此接口前， bugzilla 的 bug 还未导入 tower, 返回的 result 为字符串，内容为 tower todo 的 url,如
```
{
	"result":"https:\/\/tower.im\/projects\/0\/todos\/d9bb255f3c6d4deca4c7a127bb90b9be",
	"error":false
}
```

当调用此接口前，bugzilla 的 bug 已经导入过 tower 了，返回的 result 为列表，内容为 tower todo guid,如
```
{"error":false,"result":["d6609cfc0d914888ae1cdd8a6f7f33f1"]}
```

例子
```
curl -H 'Tower-Token: 44d8b81df5db4aa2a4eb001c100247ba' -d 'todolist_guid=e60eab8489484d74a0eef6213041e630&bug_id=12' -X PUT http://10.0.0.231:3000/services/tower/import/bugzilla_bug

http PUT http://10.0.0.231:3000/services/tower/import/bugzilla_bug  Tower-Token:44d8b81df5db4aa2a4eb001c100247ba todolist_guid=e60eab8489484d74a0eef6213041e630 bug_id=12
```
