<!--Meta
category:DTask
title:Link 接口
DO NOT Delete Meta Above -->

### 关联
PUT /links

#### Form 参数
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
curl -d 'target_a=bugzilla&a_id=10&target_b=gerrit&b_id=12' -X PUT http://10.0.0.231:3000/links/

http -f PUT http://10.0.0.231:3000/links/ target_a=bugzilla a_id=10 target_b=gerrit b_id=12
```


### 解除关联

DELETE /links

#### Form 参数
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
curl -d 'target_a=bugzilla&a_id=10&target_b=gerrit&b_id=12'  -X DELETE http://10.0.0.231:3000/links

http -f DELETE http://10.0.0.231:3000/links/ target_a=bugzilla a_id=10 target_b=gerrit b_id=12
```


### 获取关联

GET /links

#### Form 参数
* target
* id

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
curl -d 'target=bugzilla&id=10' -X GET http://10.0.0.231:3000/links

http -f GET http://10.0.0.231:3000/links/ target=bugzilla id=10
```