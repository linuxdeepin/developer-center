<!--Meta
category:DeepinID
title:接口设计
DO NOT Delete Meta Above-->

## 1. RESTful API

DeepinID服务器提供对DeepinID用户数据的基本访问接口，采用RESTful的接口设计原则。对于每一项资源，都对应到一个唯一的URI上，通过HTTP协议来实现具体的CURD操作，HTTP方法与资源访问方式映射关系如下：

| HTTP Method | Resource Action | Symbol |
|-------------|-----------------|--------|
| POST | Create | C |
| PUT | Update | U |
| GET | Read | R |
| DELETE | Delete | D |

例如，对于用户数据，其对于URI为：

** [https://api.linuxdeepin.com/admin/user/id]()**

添加用户：

** POST [https://api.linuxdeepin.com/admin/user/id]()**

修改用户信息：

** PUT [https://api.linuxdeepin.com/admin/user/id/:id]()**

查询用户信息：

** GET [https://api.linuxdeepin.com/admin/user/id/:id]()**

删除用户：

** DELETE [https://api.linuxdeepin.com/admin/user/id/:id]()**

## 2. 安全

DeepinID接口安全性完全依赖于HTTPS协议，所以HTTPS协议是必须的。

## 3. 权限控制

DeepinID接口的权限控制主要由Access-Token控制，目前权限设计尚不完善，只有完全控制权限和无访问权限两种。在实现上，没一个针对DeepinID资源访问的HTTPS请求都必须在其Header中携带Access-Token参数。

``` http
Header:
Access-Token: "789fdiaudfjewe8728323hj2k39239adf8amvn09fdajkj"
```
