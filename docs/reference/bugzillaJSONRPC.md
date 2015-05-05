<!--Meta
category:参考文档
title:Bugzilla JSONRPC 接口
DO NOT Delete Meta Above -->

## Bugzilla API Documentation

[API index](https://www.bugzilla.org/docs/tip/en/html/api/index.html)

### Bugzilla WebService


目前 bugzilla.deepin.io 使用是 4.4 版，只能调用 jsonrpc 接口，没有 REST api ,调用接口前要先登录

详细请阅读 
 [Bugzilla WebService](https://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService.html)

[Bugzilla::WebService::Server::JSONRPC](https://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService/Server/JSONRPC.html)

#### Bugzilla_token
You can specify **Bugzilla_token** as argument to any WebService method, and you will be logged in as that user if the token is correct. This is the token returned when calling User.login mentioned above.

An error is thrown if you pass an invalid token and you will need to log in again to get a new token.

#### User.login
不需要加 Bugzilla_token

[登陆，获取新的 Bugzilla_token](https://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService/User.html#login)

#### Bug.create
[创建 bug](https://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService/Bug.html#create)

#### Bug.get
[获取bug信息](https://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService/Bug.html#get)

#### Bug.add_comment
[bug增加评论](https://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService/Bug.html#add_comment)


#### Bug.add_attachment
[bug增加附件](https://www.bugzilla.org/docs/tip/en/html/api/Bugzilla/WebService/Bug.html#add_attachment)
