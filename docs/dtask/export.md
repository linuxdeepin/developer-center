<!--Meta
category:DTask
title:Export 接口
DO NOT Delete Meta Above -->

### bugzilla 到 tower

PUT /export/bugzilla/:bug_id/tower_todolist/:todo_list_guid

#### 功能
将 bugzilla 的 bug  导出到 tower, 在指定的 tower todolist 下创建新的 todo，新建立的 todo 标题为 “#bugzila #bug_id + bug 标题”，内容为“from: bug_url”，并将它与 bug 关联起来。
同时也设置 bugzilla 上 bug 的 url 为 todo 的 url，并增加一条评论，内容也包含 todo 的 url。

#### 请求头
Tower-Token: access_token

#### 参数
* bug_id
* todo_list_guid

#### 返回数据

当调用此接口前， bugzilla 的 bug 还未导入 tower, 返回的 result 为字符串，内容为 tower todo 的 url,如
```
{
	"result":"https:\/\/tower.im\/projects\/3ec8de76957d47f2a3301b5625d42fb2\/todos\/d9bb255f3c6d4deca4c7a127bb90b9be",
	"error":false
}
```

当调用此接口前，bugzilla 的 bug 已经导入过 tower 了，返回的 result 为列表，内容为 tower todo guid,如
```
{"error":false,"result":["d6609cfc0d914888ae1cdd8a6f7f33f1"]}
```

例子
```
curl -H 'Tower-Token: f5d2d2ef8afde4029d74f95eb8657bb0' -X GET http://localhost:3000/tower/projects/bec56353863d4376a6ccad7ef37e77e8/todolists
```