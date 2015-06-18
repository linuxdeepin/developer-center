<!--Meta
category:DeepinID
title:应用管理
DO NOT Delete Meta Above -->

##  授权用户应用管理


DeepinID提供用户添加/删除/修改应用信息的接口。

当前版本： v1

**TODO List:**

- [ ] PUT/DELETE

### 通用认证参数

查询用户创建的应用接口均需要有用户授权的token，并且token中需要拥有app对应的权限。


### 1 获取授权用户应用列表

#### 1.1 API Endpoint

GET [https://api.deepin.org/v1/user/apps](https://api.deepin.org/v1/apps)

#### 1.2 Request Parameters

**OAuth2 Scope：**

```
app
```

**Header Parameter：**

| 参数名称          | 描述        |
|----------------  |-------------|
| **Access-Token** | 用户通过oauth授权获得的token |

**Example：**

```json
curl -H Access-Token:OWNjN2QyMTMtMWRmNC00N https://api.deepin.org/v1/user/apps
```

#### 1.3 Respone

**Return 200 and user's app list:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
	{
		"client_id": "afb057",
		"user_id": 1,
		"app_name": "Blog",
		"client_secret": "ec37971eb",
		"redirect_uri": "http://planet.deepin.org/wp-content/themes/deepin2015/deepin-login.php",
		"app_home_uri": "https://ci.deepin.io",
		"app_description": "",
		"scope": "base,user:read,app",
		"access_type": "authorization_code"
	},
	{
		"client_id": "a86b0059",
		"user_id": 1,
		"app_name": "Bugzilla",
		"client_secret": "8542ad2391db56fd58ab8d83c34896ec2adc17d6",
		"redirect_uri": "http://test_bugzilla.deepin.io/index.cgi",
		"app_home_uri": "https://bugzilla.deepin.io",
		"app_description": "",
		"scope": "base,user:read,app",
		"access_type": "authorization_code"
	}
]
```

**Return Empty List if user has no app:**

### 2 获取授权用户单个应用信息

#### 2.1 API Endpoint

GET [https://api.deepin.org/v1/user/apps/:client_id](https://api.deepin.org/v1/apps/:client_id)

#### 2.2 Request Parameters

**OAuth2 Scope：**

```
app
```

**Header Parameter：**

| 参数名称          | 描述        |
|----------------  |-------------|
| **Access-Token** | 用户通过oauth授权获得的token |


**Url Parameter**

| 参数名称        | 描述        |
|----------------|-------------|
| **:client_id** | client_id |


**Example：**


```json
curl -H Access-Token:OWNjN2QyMTMtMWRmNC00N https://api.deepin.org/v1/user/apps/b401162c9d06
```

#### 2.3 Respone

**Return 200 and user info when user is exist:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
	"client_id": "70a86b0059e0c4a",
	"user_id": 1,
	"app_name": "Bugzilla",
	"client_secret": "8542ad2391db56fd58ab8d83c34896ec2adc17d6",
	"redirect_uri": "http://test_bugzilla.deepin.io/index.cgi",
	"app_home_uri": "https://bugzilla.deepin.io",
	"app_description": "",
	"scope": "base,user:read,app",
	"access_type": "authorization_code"
}
```

**Return 404 if user is NOT exist:**

```http
HTTP/1.1 404 Not Found
Content-Type: application/json; charset=utf-8

{
	"message": "App Not Exist"
}
```

### 3 授权用户创建应用

#### 3.1 API Endpoint

POST [https://api.deepin.org/v1/user/apps](https://api.deepin.org/v1/apps)

#### 3.2 Request Parameters

**Body Json Parameter：**

| 参数名称        | 描述        |
|----------------|-------------|
| **app_name** | 应用名称，全局唯一，不可重复，不可为空。  |
| **redirect_uri** | 应用回调url，服务器会检查完整的回调uri。注意需要携带完整的schema，如http://。并且https://example.com/callback 和  http://example.com/callback 是不同的回调地址。 |
| **app_home_uri** | 应用主页  |
| **app_description** | 应用描述  |
| **scope** | 应用权限，不得超过授权用户的权限列表。（TODO：暂时被忽略，会获取为用户完整权限）  |

**Example：**

```http
POST /v1/apps
Content-Type: application/json

{
    "app_name": "TestApp",
    "redirect_uri": "https://bugzilla.deepin.io/index.cgi",
    "app_home_uri": "bugzilla.deepin.io",
    "app_description": "Deepin Bugzilla",
    "scope": "base"
}
```
Or：

```bash
curl -H "Content-Type: application/json" -H Access-Token:OWNjN2QyMTMtMWRmNC00N -X POST -d '{"app_name": "MyAppName","redirect_uri": "https://bugzilla.deepin.io/index.cgi", "app_home_uri": "bugzilla.deepin.io", "app_description": "Deepin Bugzilla", "scope": "basebase,user:read,app"}' https://api.deepin.org/v1/user/apps
```

#### 3.3 Respone

**Return 200 and app info if create success:**

```http
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
	"client_id": "968b527f73f023b278902597a52475af71344ac8",
	"user_id": 1,
	"app_name": "MyAppName",
	"client_secret": "d8f26a925ba258efe40ec812bf7684196b419f78",
	"redirect_uri": "https://bugzilla.deepin.io/index.cgi",
	"app_home_uri": "bugzilla.deepin.io",
	"app_description": "Deepin Bugzilla",
	"scope": "base,user:read,app",
	"access_type": "AuthorizeRequestType"
}
```

**Return 400 if create failed:**

```http
HTTP/1.1 404 Not Found
Content-Type: application/json; charset=utf-8

{"message":"Duplicate App Name"}
```
