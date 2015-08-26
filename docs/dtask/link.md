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
curl -d 'bugzilla=1&gerrit=1' -X PUT https://api.deepin.io/dtask/links/

https -f PUT api.deepin.io/dtask/links/ bugzilla=1 gerrit=1
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
curl -d 'bugzilla=1&gerrit=1'  -X DELETE https://api.deepin.io/dtask/links

https -f DELETE api.deepin.io/dtask/links/ bugzilla=1 gerrit=1
```


### 获取关联

GET /links

#### Form 参数
两个参数，参数名必须为 tower_todo,gerrit,bugzilla 中的其中一个。

其中一个参数的值为对应 id， 另一个参数的值必须为 '-', 表示待查询的。

如 bugzilla=1 & gerrit=- , 表示查询 bugzilla bug #1 关联上的 gerrit CL 。


#### 返回数据
如
```
{
    "error": false,
    "result": [
        "2"
    ]
}
```

#### 例子
```
curl -d 'bugzilla=1&gerrit=-' -X GET https://api.deepin.io/dtask/links

https -f GET api.deepin.io/dtask/links/ bugzilla=1 gerrit=-
```
