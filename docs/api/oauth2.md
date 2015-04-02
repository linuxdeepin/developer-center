<!--Meta
category:DeepinID
title:OAuth2接口
DO NOT Delete Meta Above-->

## 认证流程

DeepinID通过标准的OAuth2协议实现登录认证服务
站点应用通过访问passport.deepin.com进行登录验证

## Access Token

认证通过后，接入应用能够获取对应权限的Access Token，需要在每个请求中携带Access Token，有两种方式携带Access-Token。

对于GET请求，可以在Header中携带token：
```
Access-Token: MDRjZGJlYTctMDFjMy00YzM0LWEyNjctMGQ0N2U5YTBlZTBh
```

对于POST请求，需要在提交表单中携带toeken:
```
access_token=MDRjZGJlYTctMDFjMy00YzM0LWEyNjctMGQ0N2U5YTBlZTBh
```

## 认证/授权接口

### 1 Authorize接口

#### 1.1 API Endpoint

GET [https://api.linuxdeepin.com/oauth2/authorize](https://api.linuxdeepin.com/oauth2/authorize)

#### 1.2 请求参数

| 参数名称         | 必选  | 类型    | 描述       |
|------------------|-------|--------|-------------|
| **response_type** | true | string | code |
| **client_id** | true | string | 申请应用时分配的AppKey |
| **redirect_uri** | true | string | 授权回调地址，需与应用设置的回调地址一致 |
| **scope** | false | string | 申请scope权限所需参数，可一次申请多个scope权限，用逗号分隔。如果没有，则为默认权限。|
| **state** | false |  string | 用于保持请求和回调的状态，在回调时，会在Query Parameter中回传该参数。 开发者可以用这个参数验证请求有效性， 也可以记录用户请求授权页前的位置。 这个参数可用于防止跨站请求伪造（CSRF）攻击 |

**示例：**

``` html
https://api.linuxdeepin.com/oauth2/authorize?client_id=b401162c9d061040885d0fac242ea&redirect_uri=https://ci.deepin.io/securityRealm/finishLogin&response_type=code&state=1425660329-uLzQ6rjWU4-mjviAH4MA6WgJCsO9MoUdXjd4k8vMOuk
```
#### 1.2 返回数据

| 返回值字段  | 类型 | 字段说明 |
|------------|------|----------|
| **code** |string | 用于调用access_token，接口获取授权后的access token。 |
| **state** | string | 如果传递参数，会回传该参数。 |

**示例：**

``` html
https://ci.deepin.io/securityRealm/finishLogin?code=NWMzMzlmOGMtM2I0Ny00NzM0LWFkNzEtMTJjNjY1NDMyZDM1&state=1425660329-uLzQ6rjWU4-mjviAH4MA6WgJCsO9MoUdXjd4k8vMOuk
```

### 2 Token接口

#### 2.1 API Endpoint

POST [https://api.linuxdeepin.com/oauth2/token](https://api.linuxdeepin.com/oauth2/token)

#### 2.2 请求参数

| 参数名称         | 必选  | 类型    | 描述       |
|------------------|-------|--------|-------------|
| **grant_type** | true | string | 请求的类型，填写authorization_code  |
| **client_id** | true | string | 申请应用时分配的AppKey |
| **client_secret** | true | string | 申请应用时分配的AppSecret。 |
| **code** | true | string | 调用authorize获得的code值。 |
| **redirect_uri** | true | string | 回调地址，需需与注册应用里的回调地址一致 |

**示例：**

``` html
POST https://api.linuxdeepin.com/oauth2/token

Content-Type:
application/x-www-form-urlencoded

Body:
client_id=b401162c9d061040885d0fac242ea&client_secret=ec37971eb48cfa1a97f53021&grant_type=authorization_code&code=MDRhNzA4YmYtNjNiZC00MTViLWE2YzYtZTU1ZDNiN2JjYjMy&redirect_uri=https://ci.deepin.io/securityRealm/finishLogin
```

#### 2.3 返回数据

| 返回值字段  | 类型 | 字段说明 |
|-------------|------|---------|
| **access_token** |    string | 用于调用access_token，接口获取授权后的access token。 |
| **expires_in** |  string | access_token的生命周期，单位是秒数。 |
| **scope** |string | 用户权限 |
| **uid** | string | 当前授权用户的UID。 |

**示例：**

``` json
{
   "access_token": "ZGUyNmUyODktM2QxZi00YmJhLWJmYmItMmQwMWYyZDliYmUz",
   "expires_in": 3000,
   "refresh_token": "YmU2ZmE1ZTItMTJjNS00MDZhLWIyYzItYzFiZjk3YmVhM2Nh",
   "scope": "base,",
   "uid": 10001
}
```
