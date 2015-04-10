<!--Meta
category:DTask
title:Link 接口
DO NOT Delete Meta Above -->

### 关联
PUT /link/:target_a/:a_id/:target_b/:b_id

#### 参数
* target_a
* a_id
* target_b
* b_id

#### 返回数据
如
```
{"error":false,"result":true}
```

#### 例子
```
curl -X PUT http://localhost:3000/link/bugzilla/10/gerrit/12
```


### 解除关联

DELETE /link/:target_a/:a_id/:target_b/:b_id

#### 参数
* target_a
* a_id
* target_b
* b_id

#### 返回数据
如
```
{"error":false,"result":true}
```

#### 例子
```
curl -X DELETE http://localhost:3000/link/bugzilla/10/gerrit/12
```


### 获取关联

GET /link/:target/:id

#### 参数
* target
* id

#### 返回数据
如
```
{"error":false,"result":{"tower_todo":["ee77f06485d54dfd93b2f3d068c30645"]}}
```

#### 例子
```
curl -X GET http://localhost:3000/link/bugzilla/2
```