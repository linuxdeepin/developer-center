<!--Meta
category:DeepinID
title:用户信息
DO NOT Delete Meta Above -->

##  用户信息

DeepinID提供基本的用户信息查询接口


### 1 用户基本信息查询

#### 1.1 API Endpoint

GET [https://api.deepin.org/user](https://api.deepin.org/user)

#### 1.2 请求参数

```
#Http Heaer
Access-Token: MDRjZGJlYTctMDFjMy00YzM0LWEyNjctMGQ0N2U5YTBlZTBh
```

**示例：**

``` 
curl -v -H Access-Token:OWNjN2QyMTMtMWRmNC00N http://127.0.0.1:8010/user
```

#### 1.2 返回数据

**示例：**

```json
{
  "error_code": 200,
  "error_msg": "",
  "data": {
    "uid": 12,
    "username": "adwa",
    "nickname": "",
    "email": "adwa@gmail.com",
    "scope": "base",
    "avatar": "",
    "profile_image": "",
    "website": "",
    "signature": "",
    "active": true,
  }
}
```

