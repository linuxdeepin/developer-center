# Accounts Interface Introduction

----------


##Interface: /com/deepin/daemon/Accounts

###DBusInfo

>Dest: `com.deepin.daemon.Accounts`  
>Path: `/com/deepin/daemon/Accounts`  
>IFC : `com.deepin.daemon.Accounts`


###Properties

* UserList   []string
>Desc: 用户 ObjectPath 列表

* GuestIcon  string

* AllowGuest bool


###Methods

* CreateUser (name, fullname string, ty int32)
>name: 用户名  
>fullname: 全名，可以为空  
>ty: 用户类型，0 为普通用户，1 为管理员

* DeleteUser (name string, rmFiles bool)
>name: 用户名  
>rmFiles: 是否删除用户数据

* FindUserById (uid string) (path string)

* FindUserByName (name string) (path string)

* RandUserIcon () (icon string, ok bool)
>icon: 头像路径  
>ok: 是否获取成功

* IsUsernameValid (name string) (valid bool, reason string code int32)
>name: 需要检查的用户名  
>valid: 是否合法  
>reason: 不合法原因  
>code: 不合法代码  
>Desc: 检查用户名是否有效

* AllowGuestAccount (allow bool)
>Desc: 允许来宾账户登录

* CreateGuestAccount() (path string)
>path: 来宾账户的 ObjectPath


###Signals

* UserAdded   func(string)
 
* UserDeleted func(string)
 
* Error func(pid uint32, action string, reason string)
>pid: 调用者的 pid  
>action: 被调用的接口  
>reason: 错误信息  


-----------


##Interface: com.deepin.daemon.Accounts.User

###DBusInfo

>Dest: `com.deepin.daemon.Accounts`  
>Path: `/com/deepin/daemon/Accounts/User%d`  
>IFC : `com.deepin.daemon.Accounts.User`


###Properties

* UserName       string

* Uid            string
 
* Gid            string
 
* HomeDir        string
 
* Shell          string
 
* IconFile       string
 
* BackgroundFile string
 
* Locked bool
>Desc: 用户是否被禁用
 
* AutomaticLogin bool
>Desc: 是否允许此用户自动登录
 
* AccountType int32
 
* LoginTime   uint64
 
* IconList     []string
 
* HistoryIcons []string


###Methods

* SetUserName (name string) (ok bool)

* SetHomeDir (home string) (ok bool)

* SetShell (shell string) (ok bool)

* SetPassword (words string) (ok bool)

* SetAccountType (ty int32) (ok bool)

* SetLocked (locked bool) (ok bool)

* SetAutomaticLogin (auto bool) (ok bool)

* SetIconFile (icon string) (ok bool)

* DeleteIconFile (icon string) (ok bool)

* SetBackgroundFile (bg string) (ok bool)

* DeleteHistoryIcon (icon string) (ok bool)

* IsIconDeletable(icon string) (ok bool)

* GetLargeIcon () (largeIcon string)
>Desc: 获取当前头像的大图标
