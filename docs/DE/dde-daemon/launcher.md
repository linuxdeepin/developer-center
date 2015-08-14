# launcher
--


## Usage

```go
const (
	AppDirName string = "applications"

	SoftwareStatusCreated  string = "created"
	SoftwareStatusModified string = "updated"
	SoftwareStatusDeleted  string = "deleted"
)
```

#### type CategoryInfoExport

```go
type CategoryInfoExport struct {
	Name  string
	Id    CategoryId
	Items []ItemId
}
```



#### type FrequencyExport

```go
type FrequencyExport struct {
	Id        ItemId
	Frequency uint64
}
```


#### type ItemChangedStatus

```go
type ItemChangedStatus struct {
}
```


#### type ItemInfoExport

```go
type ItemInfoExport struct {
	Path          string
	Name          string
	Id            ItemId
	Icon          string
	CategoryId    CategoryId
	TimeInstalled int64
}
```


#### type Launcher

```go
type Launcher struct {

	// ItemChanged当launcher中的item有改变后触发。
	ItemChanged func(
		status string,
		itemInfo ItemInfoExport,
		categoryId CategoryId,
	)
	// UninstallSuccess在卸载程序成功后触发。
	UninstallSuccess func(ItemId)
	// UninstallFailed在卸载程序失败后触发。
	UninstallFailed func(ItemId, string)

	// SendToDesktopSuccess在发送到桌面成功后触发。
	SendToDesktopSuccess func(ItemId)
	// SendToDesktopFailed在发送到桌面失败后触发。
	SendToDesktopFailed func(ItemId, string)

	// RemoveFromDesktopSuccess在从桌面移除成功后触发。
	RemoveFromDesktopSuccess func(ItemId)
	// RemoveFromDesktopFailed在从桌面移除失败后触发。
	RemoveFromDesktopFailed func(ItemId, string)

	// SearchDone在搜索结束后触发。
	SearchDone func([]ItemId)

	// NewAppLaunched在新安装程序被标记为已启动后被触发。（废弃，不够直观，使用新信号NewAppMarkedAsLaunched）
	NewAppLaunched func(ItemId)
	// NewAppMarkedAsLaunched在新安装程序被标记为已启动后被触发。
	NewAppMarkedAsLaunched func(ItemId)
}
```

Launcher为launcher的后端。


#### func (*Launcher) GetAllCategoryInfos

```go
func (self *Launcher) GetAllCategoryInfos() []CategoryInfoExport
```
GetAllCategoryInfosu获取所有分类的分类信息。

#### func (*Launcher) GetAllFrequency

```go
func (self *Launcher) GetAllFrequency() (infos []FrequencyExport)
```
GetAllFrequency获取所有的使用频率信息。 包括：item的id与使用频率。

#### func (*Launcher) GetAllItemInfos

```go
func (self *Launcher) GetAllItemInfos() []ItemInfoExport
```
GetAllItemInfos获取所有item的信息。

#### func (*Launcher) GetAllNewInstalledApps

```go
func (self *Launcher) GetAllNewInstalledApps() []ItemId
```
GetAllNewInstalledApps获取所有新安装的程序。

#### func (*Launcher) GetAllTimeInstalled

```go
func (self *Launcher) GetAllTimeInstalled() []TimeInstalledExport
```
GetAllTimeInstalled获取所有程序的安装时间。 包括：item的id与安装时间。

#### func (*Launcher) GetCategoryInfo

```go
func (self *Launcher) GetCategoryInfo(cid int64) CategoryInfoExport
```
GetCategoryInfo获取分类id对应的分类信息。 包括：分类名，分类id，分类所包含的程序。


#### func (*Launcher) GetItemInfo

```go
func (self *Launcher) GetItemInfo(id string) ItemInfoExport
```
GetItemInfo获取id对应的item信息。
包括：item的path，item的Name，item的id，item的icon，item的分类id，item的安装时间

#### func (*Launcher) IsItemOnDesktop

```go
func (self *Launcher) IsItemOnDesktop(id string) bool
```
IsItemOnDesktop判断程序是否已经在桌面上。

#### func (*Launcher) MarkLaunched

```go
func (self *Launcher) MarkLaunched(id string)
```
MarkLaunched将程序标记为已启动过。

#### func (*Launcher) RecordFrequency

```go
func (self *Launcher) RecordFrequency(id string)
```
RecordFrequency记录程序的使用频率。

#### func (*Launcher) RecordRate

```go
func (self *Launcher) RecordRate(id string)
```
RecordRate记录程序的使用频率。（废弃，统一用词，请使用新接口RecordFrequency）

#### func (*Launcher) RequestRemoveFromDesktop

```go
func (self *Launcher) RequestRemoveFromDesktop(id string) bool
```
RequestRemoveFromDesktop请求将程序从桌面移除。

#### func (*Launcher) RequestSendToDesktop

```go
func (self *Launcher) RequestSendToDesktop(id string) bool
```
RequestSendToDesktop请求将程序发送到桌面。

#### func (*Launcher) RequestUninstall

```go
func (self *Launcher) RequestUninstall(id string, purge bool)
```
RequestUninstall请求卸载程。

#### func (*Launcher) Search

```go
func (self *Launcher) Search(key string)
```
Search搜索给定的关键字。



#### type Setting

```go
type Setting struct {

	// CategoryDisplayModeChanged当分类的显示模式改变后触发。
	CategoryDisplayModeChanged func(int64)

	// SortMethodChanged在排序方式改变后触发。
	SortMethodChanged func(int64)
}
```

Setting存储launcher相关的设置。


#### func (*Setting) GetCategoryDisplayMode

```go
func (s *Setting) GetCategoryDisplayMode() int64
```
GetCategoryDisplayMode获取launcher当前的分类显示模式。


#### func (*Setting) GetSortMethod

```go
func (s *Setting) GetSortMethod() int64
```
GetSortMethod获取launcher当前的排序模式。

#### func (*Setting) SetCategoryDisplayMode

```go
func (s *Setting) SetCategoryDisplayMode(newMode int64)
```
SetCategoryDisplayMode设置launcher的分类显示模式。

#### func (*Setting) SetSortMethod

```go
func (s *Setting) SetSortMethod(newMethod int64)
```
SetSortMethod设置launcher的排序方法。

#### type SettingInterface

```go
type SettingInterface interface {
	GetCategoryDisplayMode() int64
	SetCategoryDisplayMode(newMode int64)
	GetSortMethod() int64
	SetSortMethod(newMethod int64)
	// contains filtered or unexported methods
}
```


#### type TimeInstalledExport

```go
type TimeInstalledExport struct {
	Id   ItemId
	Time int64
}
```
