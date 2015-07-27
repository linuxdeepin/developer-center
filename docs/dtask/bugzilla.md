<!--Meta
category:DTask
title:Bugzilla 接口
DO NOT Delete Meta Above -->

### 获取所有 bugzilla 产品
GET /dtask/services/bugzilla/products

### Form 参数
无

### 返回数据
如
```
{
	"result":{
		"products":[
    		{
        		"name" : "product name 1",
            	...
        	},
            ...
    	]
    },
	"error": false
}
```

### 从 tower 导入 todo
PUT /dtask/services/bugzilla/import/tower_todo

#### 功能
根据 tower todo guid 获取 todo 的一些信息，以此在 bugzilla.deepin.io 上创建一个 bug, 并且在 dtask link 关系中关联 todo_guid 与 bug id, 已经有关联时将不创建新 bug.

根据 todo 所在 todolist 的名称决定创建在 bugzilla 的哪一个分类中, 比如  BZImport::TestProduct::3.0::TestComponent , 将创建在 bugzilla 的 TestProduct 之下的 TestComponent 执行,并且版本设置为 3.0


#### 请求头头
Tower-Token: tower access token

#### Form 参数
todo_guid : tower todo 的 GUID

#### 返回数据
如
```
{"result":1338,"error":false}
```

例子
```
http -f PUT https://api.deepin.io/dtask/services/bugzilla/import/tower_todo Tower-Token:12537b98400ee9cxxxf4256bdd0c66xx todo_guid=c24xxxd00e9a4e1f9e7b7008a6262c75
```