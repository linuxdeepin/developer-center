<!--Meta
category:DTask
title:Task 接口(废弃)
DO NOT Delete Meta Above -->

## Task

### 创建 task

POST /task/

#### 返回数据
如
```
 {"error":false,"result":"55249460ada5d840f7010000"}
```

### 获取 task 信息

GET /task/:task_id

#### 参数
* task_id

#### 返回数据
如 
```
{
    "error": false,
    "result": {
        "_id": "552640e5ada5d86fb1020000",
        "createAt": 1428570341999,
        "tower_todo": "d9bb255f3c6d4deca4c7a127bb90b9be",
        "link": {
            "bugzilla": [
                "2"
            ]
        }
    }
}
```

### 获取 task 的 tower todo

GET /task/:task_id/tower/todo/

#### 参数
* task_id

#### 返回数据
如
```
{"result":"d9bb255f3c6d4deca4c7a127bb90b9be","error":false}
```

### 设置 task 的 tower todo

PUT /task/:task_id/tower/todo/:todo_guid

#### 参数
* task_id
* todo_guid

#### 返回数据
如 
```
{"error":false,"result":true}
```

### 删除 task 的 tower todo

DELETE /task/:task_id/tower/todo/

#### 参数
* task_id

#### 返回数据
如
```
{"result":true,"error":false}
```

### 删除 task
DELETE /task/:task_id

#### 参数
* task_id

#### 返回数据
如
```
{"error":false,"result":true}
```

## 关联

### 关联 task 与 target target_id
PUT /task/:task_id/link/:target/:target_id

#### 参数
* task_id
* target 如 bugzilla, gerrit
* target_id

#### 返回数据
如
```
{"error":false,"result":true}
```

### 解除 task 与 target target_id 的关联

DELETE /task/:task_id/link/:target/:target_id

#### 参数
* task_id
* target 如 bugzilla, gerrit
* target_id

#### 返回数据
如
```
{"error":false,"result":true}
```


### 获取 task 的关联们

GET /task/:task_id/link

#### 参数
task_id

#### 返回数据
如
```
{"result":{"bugzilla":["123","124"]},"error":false}
```

### 获取 task 与 target 关联的 target_id 们

GET /task/:task_id/link/:target


#### 参数
* task_id
* target 如 bugzilla, gerrit

#### 返回数据
如
```
{"result":["123","124"],"error":false}
```

### 获取与 target target_id 相关联的 task 们
GET /task/link/:target/:target_id

#### 参数
* target 如 bugzilla, gerrit
* target_id

#### 返回数据
如
```
{"error":false,"result":["55249460ada5d840f7010000"]}
```

### 解除 target target_id 与所有相关联的 task 的关联 
DELETE /task/link/:target/:target_id

#### 参数
* target
* target_id

#### 返回数据
如
```
{"error":false,"result":true}
```

### 获取 task link 的信息
GET /task/:task_id/link_info

#### 参数
* task_id

#### 返回数据
如
```
{"result":["bugzilla 123 status CONFIRMED","failed get bugzilla 124"],"error":false}
```
