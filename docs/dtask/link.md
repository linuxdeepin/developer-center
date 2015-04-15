<!--Meta
category:DTask
title:Link 接口
DO NOT Delete Meta Above -->

### 关联
PUT /links

#### Form 参数
两个参数，参数名必须为 tower_todo,gerrit,bugzilla 中的其中一个，值为对应 id

#### 返回数据
如
```
{"error":false,"result":true}
```

#### 例子
```
curl -d 'bugzilla=10&gerrit=12' -X PUT http://10.0.0.231:3000/links/

http -f PUT http://10.0.0.231:3000/links/ bugzilla=10 gerrit=12
```


### 解除关联

DELETE /links

#### Form 参数
两个参数，参数名必须为 tower_todo,gerrit,bugzilla 中的其中一个，值为对应 id

#### 返回数据
如
```
{"error":false,"result":true}
```

#### 例子
```
curl -d 'bugzilla=10&gerrit=12'  -X DELETE http://10.0.0.231:3000/links

http -f DELETE http://10.0.0.231:3000/links/ bugzilla=10 gerrit=12
```


### 获取关联

GET /links

#### Form 参数
一个参数，参数名必须为 tower_todo,gerrit,bugzilla 中的其中一个，值为对应 id

#### 返回数据
如
```
{
    "error": false, 
    "result": {
        "gerrit": [
            "12"
        ]
    }
}
```

#### 例子
```
curl -d 'bugzilla=10' -X GET http://10.0.0.231:3000/links

http -f GET http://10.0.0.231:3000/links/ bugzilla=10
```