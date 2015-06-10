<!--Meta
category:DeepinID
title:用户信息
DO NOT Delete Meta Above -->

##  用户信息

DeepinID提供基本的用户信息查询/修改接口. 修改接口接口权限不对第三方开发人员开放。

当前版本： v1

旧版本接口参考文档： 待定。

**TODO List:**

- [ ] 补充旧版接口文档
- [ ] 补充用户信息修改删除文档



### 1 获取单个用户信息（无授权）

#### 1.1 API Endpoint

GET [https://api.deepin.org/v1/users/:indentify]()

#### 1.2 Request Parameters

**Url Parameter**

| 参数名称        | 描述        |
|----------------|-------------|
| **:indentify** | 用户标识，可以是用户名，UID，用户邮箱  |


** Example：**

```http
GET https://api.deepin.org/v1/users/iceyer
GET https://api.deepin.org/v1/users/17898
GET https://api.deepin.org/v1/users/iceyers@gmail.com
```

#### 1.3 Respone

**Return 200 and user info when user is exist:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
    "uid": 17898,
    "username": "Iceyer",
    "nickname": "Iceyer",
    "avatar": "http://u.deepin.org/ucenter_server/avatar.php?uid=17898&size=small",
    "profile_image": "http://u.deepin.org/ucenter_server/avatar.php?uid=17898",
    "website": "",
    "signature": ""
}
```

**Return 404 if user is NOT exist:**

```http
HTTP/1.1 404 Not Found
Content-Type: application/json; charset=utf-8

{"message":"Invaild User Name"}

```

### 2 获取多个用户信息（无授权）

#### 2.1 API Endpoint

GET [https://api.deepin.org/v1/users]()

#### 2.2 Request Parameters

**Query String Parameter：**

| 参数名称        | 描述        |
|----------------|-------------|
| **id** | UID  |
| **username** | 用户名  |
| **email** | 邮箱  |

建议同时只能通过一种参数查询，因为各个参数之间是”与“关系。


** Example：**

```http
GET https://api.deepin.org/v1/users?id=17898&id=7045
GET https://api.deepin.org/v1/users?email=iceyers@gmail.com&email=snyh@snyh.org
```

#### 2.3 Respone

**Return 200 and user info when user is exist:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
    {
        "uid": 7045,
        "username": "snyh1010",
        "nickname": "misscx",
        "avatar": "http://u.deepin.org/ucenter_server/avatar.php?uid=7045&size=small",
        "profile_image": "http://u.deepin.org/ucenter_server/avatar.php?uid=7045",
        "website": "",
        "signature": ""
    },
    {
        "uid": 17898,
        "username": "Iceyer",
        "nickname": "Iceyer",
        "avatar": "http://u.deepin.org/ucenter_server/avatar.php?uid=17898&size=small",
        "profile_image": "http://u.deepin.org/ucenter_server/avatar.php?uid=17898",
        "website": "",
        "signature": ""
    }
]
```

**Return 404 if user is NOT exist:**

```http
HTTP/1.1 404 Not Found
Content-Type: application/json; charset=utf-8

{"message":"Invaild User Name"}

```

### 3 获取授权用户信息

#### 3.1 API Endpoint

GET [https://api.deepin.org/v1/user]()

#### 2.2 Request Parameters

**OAuth2 Scope：**

```
user:read
```

**Header Parameter：**

| 参数名称          | 描述        |
|----------------  |-------------|
| **Access-Token** | 用户通过oauth授权获得的token |


** Example：**

````
curl -v -H Access-Token:OWNjN2QyMTMt https://api.deepin.org/v1/user
````

#### 3.3 Respone

**Return 200 and user info when user is exist:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
    "uid": 17898,
    "username": "Iceyer",
    "nickname": "Iceyer",
    "email": "iceyers@gmail.com",
    "scope": "base,user:read",
    "avatar": "http://u.deepin.org/ucenter_server/avatar.php?uid=17898&size=small",
    "profile_image": "http://u.deepin.org/ucenter_server/avatar.php?uid=17898",
    "website": "",
    "signature": ""
}
```