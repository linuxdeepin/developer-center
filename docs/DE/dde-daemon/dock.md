# dock
--


## Usage

```go
const (
	FieldTitle   = "title"
	FieldIcon    = "icon"
	FieldMenu    = "menu"
	FieldAppXids = "app-xids"

	FieldStatus   = "app-status"
	ActiveStatus  = "active"
	NormalStatus  = "normal"
	InvalidStatus = "invalid"
)
```

```go
const (
	TriggerShow int32 = iota
	TriggerHide
)
```

```go
const (
	COMPONENT_CODESET = 1 << iota
	COMPONENT_MODIFIER
	COMPONENT_TERRITORY
)
```

```go
const (
	HideModeKey    string = "hide-mode"
	DisplayModeKey string = "display-mode"
	ClockTypeKey   string = "clock-type"
	DisplayDateKey string = "display-date"
	DisplayWeekKey string = "display-week"
)
```


#### type AppEntry

```go
type AppEntry struct {
	Id   string
	Type string
	Data map[string]string

	DataChanged func(string, string)
}
```

#### func (*AppEntry) Activate

```go
func (e *AppEntry) Activate(x, y int32) bool
```

#### func (*AppEntry) ContextMenu

```go
func (e *AppEntry) ContextMenu(x, y int32)
```


#### func (*AppEntry) HandleDragDrop

```go
func (e *AppEntry) HandleDragDrop(x, y int32, data string)
```

#### func (*AppEntry) HandleDragEnter

```go
func (e *AppEntry) HandleDragEnter(x, y int32, data string)
```

#### func (*AppEntry) HandleDragLeave

```go
func (e *AppEntry) HandleDragLeave(x, y int32, data string)
```

#### func (*AppEntry) HandleDragOver

```go
func (e *AppEntry) HandleDragOver(x, y int32, data string)
```

#### func (*AppEntry) HandleMenuItem

```go
func (e *AppEntry) HandleMenuItem(id string)
```

#### func (*AppEntry) HandleMouseWheel

```go
func (e *AppEntry) HandleMouseWheel(x, y, delta int32)
```

#### func (*AppEntry) SecondaryActivate

```go
func (e *AppEntry) SecondaryActivate(x, y int32)
```

#### type ClientManager

```go
type ClientManager struct {
	// ActiveWindowChanged会在焦点窗口被改变时触发，会将最新的焦点窗口id发送给监听者。
	ActiveWindowChanged func(xid uint32)

	// ShowingDesktopChanged会在_NET_SHOWING_DESKTOP改变时被触发。
	ShowingDesktopChanged func()
}
```

ClientManager用来管理启动程序相关窗口。

#### func (*ClientManager) ActivateWindow

```go
func (m *ClientManager) ActivateWindow(xid uint32) bool
```
ActivateWindow会激活给定id的窗口，被激活的窗口通常会成为焦点窗口。

#### func (*ClientManager) ActiveWindow

```go
func (m *ClientManager) ActiveWindow(xid uint32) bool
```
ActiveWindow会激活给定id的窗口，被激活的窗口将通常会程序焦点窗口。(废弃，名字应该是ActivateWindow，当时手残打错了，此接口会在之后被移除，请使用正确的接口)

#### func (*ClientManager) CloseWindow

```go
func (m *ClientManager) CloseWindow(xid uint32) bool
```
CloseWindow会将传入id的窗口关闭。

#### func (*ClientManager) CurrentActiveWindow

```go
func (m *ClientManager) CurrentActiveWindow() uint32
```
CurrentActiveWindow会返回当前焦点窗口的窗口id。


#### func (*ClientManager) IsLauncherShown

```go
func (m *ClientManager) IsLauncherShown() bool
```
IsLauncherShown判断launcher是否已经显示。

#### func (*ClientManager) ToggleShowDesktop

```go
func (m *ClientManager) ToggleShowDesktop()
```
ToggleShowDesktop会触发显示桌面，当桌面显示时，会将窗口恢复，当桌面未显示时，会隐藏窗口以显示桌面。


#### type DesktopAppInfo

```go
type DesktopAppInfo struct {
	*gio.DesktopAppInfo
	*glib.KeyFile
}
```

#### type DisplayModeType

```go
type DisplayModeType int32
```


```go
const (
	DisplayModeModernMode DisplayModeType = iota
	DisplayModeEfficientMode
	DisplayModeClassicMode
)
```

#### type DockProperty

```go
type DockProperty struct {

	// Height是前端dock的高度。
	Height int32

	// PanelWidth是前端dock底板的宽度。
	PanelWidth int32
}
```

DockProperty存储dock前端界面相关的一些属性，包括dock的高度以及底板的宽度。


#### type DockedAppManager

```go
type DockedAppManager struct {

	// Docked是信号，在某程序驻留成功后被触发，并将该程序的id发送给信号的接受者。
	Docked func(id string) // find indicator on front-end.
	// Undocked是信号，在某已驻留程序被移除驻留后被触发，将被移除程序id发送给信号接受者。
	Undocked func(id string)
}
```

DockedAppManager是管理已驻留程序的管理器。


#### func (*DockedAppManager) Dock

```go
func (m *DockedAppManager) Dock(id, title, icon, cmd string) bool
```
Dock驻留程序。通常情况下只需要传递程序id即可，在特殊情况下需要传入title，icon以及cmd。
title表示前端程序的tooltip内容，icon为程序图标，cmd为程序的启动命令。 成功后会触发Docked信号。
（废弃，此接口名并不好，第一反映很难理解，请使用新接口RequestDock)

#### func (*DockedAppManager) DockedAppList

```go
func (m *DockedAppManager) DockedAppList() []string
```
DockedAppList返回一个已排序的程序id列表。

#### func (*DockedAppManager) IsDocked

```go
func (m *DockedAppManager) IsDocked(id string) bool
```
IsDocked通过传入的程序id判断一个程序是否已经驻留。

#### func (*DockedAppManager) ReqeustDock

```go
func (m *DockedAppManager) ReqeustDock(id, title, icon, cmd string) bool
```
RequestDock驻留程序。通常情况下只需要传递程序id即可，在特殊情况下需要传入title，icon以及cmd。
title表示前端程序的tooltip内容，icon为程序图标，cmd为程序的启动命令。 成功后会触发Docked信号。

#### func (*DockedAppManager) RequestUndock

```go
func (m *DockedAppManager) RequestUndock(id string) bool
```
RequestUndock益处指定程序id的已驻留程序。成功后会出发Undocked信号。

#### func (*DockedAppManager) Sort

```go
func (m *DockedAppManager) Sort(items []string)
```
Sort将已驻留的程序按传入的程序id的顺序重新排序，并保存。

#### func (*DockedAppManager) Undock

```go
func (m *DockedAppManager) Undock(id string) bool
```
Undock通过程序id移除已驻留程序。成功后会触发Undocked信号。（废弃，请使用新接口RequestUndock）

#### type EntryManager

```go
type EntryManager struct {
}
```

EntryManager为驻留程序以及打开程序的管理器。

#### func  NewEntryManager

```go
func NewEntryManager() *EntryManager
```

#### type EntryProxyer

```go
type EntryProxyer struct {

	// Id属性为程序id。
	Id string
	// Type属性为程序类型，包括app，applet两种。
	Type string
	// Data包含其他程序相关属性，如icon，title，status，menu，app-xids。
	Data map[string]string
	// DataChanged会在Data属性有改变是被触发。
	DataChanged func(string, string)
}
```

EntryProxyer为驻留程序以及打开程序的dbus接口。


#### func (*EntryProxyer) Activate

```go
func (e *EntryProxyer) Activate(x, y int32) bool
```
Activate在程序被点击时作出响应，接受鼠标事件的位置信息。

#### func (*EntryProxyer) ContextMenu

```go
func (e *EntryProxyer) ContextMenu(x, y int32)
```
ContextMenu接受鼠标事件的位置信息，然后生成

#### func (*EntryProxyer) HandleDragDrop

```go
func (e *EntryProxyer) HandleDragDrop(x, y int32, data string)
```
HandleDragDrop在前端触发Dropp事件时被调用。

#### func (*EntryProxyer) HandleDragEnter

```go
func (e *EntryProxyer) HandleDragEnter(x, y int32, data string)
```
HandleDragEnter在前端触发DragEnter事件时被调用。

#### func (*EntryProxyer) HandleDragLeave

```go
func (e *EntryProxyer) HandleDragLeave(x, y int32, data string)
```
HandleDragLeave在前端触发DragLeave事件时被调用。

#### func (*EntryProxyer) HandleDragOver

```go
func (e *EntryProxyer) HandleDragOver(x, y int32, data string)
```
HandleDragOver在前端触发DragOver事件时被调用。

#### func (*EntryProxyer) HandleMenuItem

```go
func (e *EntryProxyer) HandleMenuItem(id string)
```
HandleMenuItem对出入的id在右键菜单中对应的项做处理。

#### func (*EntryProxyer) HandleMouseWheel

```go
func (e *EntryProxyer) HandleMouseWheel(x, y, delta int32)
```
HandleMouseWheel在前端触发鼠标滚轮事件时被调用。

#### func (*EntryProxyer) SecondaryActivate

```go
func (e *EntryProxyer) SecondaryActivate(x, y int32)
```
SecondaryActivate与Activate作用相同，可用于其他鼠标点击事件，通常不会被使用。

#### func (*EntryProxyer) ShowQuickWindow

```go
func (e *EntryProxyer) ShowQuickWindow()
```
ShowQuickWindow用于applet程序中，在需要显示时applet的窗口调用。

#### type EntryProxyerManager

```go
type EntryProxyerManager struct {
	// Entries为目前所有打开程序与驻留程序列表。（此属性可能会被废弃掉，调用一个初始化的方法，然后在需要的情况下触发Added信号）。
	Entries []*EntryProxyer

	// Added在程序需要在前端显示时被触发。
	Added func(dbus.ObjectPath)
	// Removed会在程序不再需要在dock前端显示时触发。
	Removed func(string)
	// TrayInited在trayicon相关内容初始化完成后触发。
	TrayInited func()
}
```

EntryProxyerManager为驻留程序以及打开程序的dbus接口管理器。 所有已驻留程序以及打开的程序都会生成对应的dbus接口。


#### type HideModeType

```go
type HideModeType int32
```


```go
const (
	HideModeKeepShowing HideModeType = iota
	HideModeKeepHidden
	HideModeAutoHide
	HideModeSmartHide
)
```


#### type HideStateManager

```go
type HideStateManager struct {
	ChangeState func(int32)
}
```



#### func (*HideStateManager) CancelToggleShow

```go
func (m *HideStateManager) CancelToggleShow()
```


#### func (*HideStateManager) SetState

```go
func (m *HideStateManager) SetState(s int32) int32
```

#### func (*HideStateManager) ToggleShow

```go
func (m *HideStateManager) ToggleShow()
```

#### func (*HideStateManager) UpdateState

```go
func (m *HideStateManager) UpdateState()
```

#### type HideStateType

```go
type HideStateType int32
```


```go
const (
	HideStateShowing HideStateType = iota
	HideStateShown
	HideStateHidding
	HideStateHidden
)
```


#### type NormalApp

```go
type NormalApp struct {
	Id        string
	DesktopID string
	Icon      string
	Name      string
	Menu      string
}
```


#### type Region

```go
type Region struct {
}
```

Region表示dock有效的可接受事件区域以及可显示区域。


#### func (*Region) GetDockRegion

```go
func (r *Region) GetDockRegion() xproto.Rectangle
```
GetDockRegion获取dock有效的可接受事件区域以及可显示区域。

#### type RemoteEntry

```go
type RemoteEntry struct {
	Path     dbus.ObjectPath
	DestName string

	Id   *dbusPropertyRemoteEntryId
	Type *dbusPropertyRemoteEntryType
	Data *dbusPropertyRemoteEntryData
}
```


#### type RuntimeApp

```go
type RuntimeApp struct {
	Id        string
	DesktopID string

	CurrentInfo *WindowInfo
	Menu        string
}
```

#### type Setting

```go
type Setting struct {

	// HideModeChanged在dock的隐藏模式改变后触发，返回改变后的模式。
	HideModeChanged func(mode int32)
	// DisplayModeChanged在dock的显示模式改变后触发，返回改变后的模式。
	DisplayModeChanged func(mode int32)
	// ClockTypeChanged在dock的时钟模式改变后触发，返回改变后的模式。
	ClockTypeChanged func(mode int32)
	// DisplayDateChanged在dock的显示日期设置改变后触发，返回是否显示日期。
	DisplayDateChanged func(bool)
	// DisplayWeekChanged在dock的显示星期设置改变后触发，返回是否显示星期。
	DisplayWeekChanged func(bool)
}
```

Setting存储dock相关的设置。


#### func (*Setting) GetClockType

```go
func (s *Setting) GetClockType() int32
```
GetClockType获取dock当前的始终模式。


#### func (*Setting) GetDisplayDate

```go
func (s *Setting) GetDisplayDate() bool
```
GetDisplayDate获取是否显示日期。

#### func (*Setting) GetDisplayMode

```go
func (s *Setting) GetDisplayMode() int32
```
GetDisplayMode获取dock当前的显示模式。

#### func (*Setting) GetDisplayWeek

```go
func (s *Setting) GetDisplayWeek() bool
```
GetDisplayWeek获取是否显示星期。

#### func (*Setting) GetHideMode

```go
func (s *Setting) GetHideMode() int32
```
GetHideMode返回当前的隐藏模式。

#### func (*Setting) SetClockType

```go
func (s *Setting) SetClockType(_clockType int32) bool
```
SetClockType设置dock的时钟显示模式。

#### func (*Setting) SetDisplayDate

```go
func (s *Setting) SetDisplayDate(d bool) bool
```
SetDisplayDate设置是否显示日期。

#### func (*Setting) SetDisplayMode

```go
func (s *Setting) SetDisplayMode(_mode int32) bool
```
SetDisplayMode设置dock的显示模式。

#### func (*Setting) SetDisplayWeek

```go
func (s *Setting) SetDisplayWeek(d bool) bool
```
SetDisplayWeek设置是否显示星期。

#### func (*Setting) SetHideMode

```go
func (s *Setting) SetHideMode(_mode int32) bool
```
SetHideMode设置dock的隐藏模式。

#### type TrayManager

```go
type TrayManager struct {

	// 目前已有系统托盘窗口的id。
	TrayIcons []uint32

	// Removed信号会在系统过盘图标被移除时被触发。
	Removed func(id uint32)
	// Added信号会在系统过盘图标增加时被触发。
	Added func(id uint32)
	// Changed信号会在系统托盘图标改变后被触发。
	Changed func(id uint32)
}
```

TrayManager为系统托盘的管理器。


#### func (*TrayManager) EnableNotification

```go
func (m *TrayManager) EnableNotification(xid uint32, enable bool)
```
EnableNotification设置对应id的窗口是否可以通知。


#### func (*TrayManager) GetName

```go
func (m *TrayManager) GetName(xid uint32) string
```
GetName返回传入的系统图标的窗口id的窗口名。

#### func (*TrayManager) Manage

```go
func (m *TrayManager) Manage() bool
```
Manage方法获取系统托盘图标的管理权。

#### func (*TrayManager) RetryManager

```go
func (m *TrayManager) RetryManager()
```
RetryManager方法尝试获取系统托盘图标的权利全，并出发Added信号。

#### func (*TrayManager) Unmanage

```go
func (m *TrayManager) Unmanage() bool
```
Unmanage移除系统托盘图标的管理权限。

#### type WindowInfo

```go
type WindowInfo struct {
	Xid         xproto.Window
	Title       string
	Icon        string
	OverlapDock bool
}
```


#### type XMouseAreaInterface

```go
type XMouseAreaInterface interface {
	ConnectCursorInto(func(int32, int32, string)) func()
	ConnectCursorOut(func(int32, int32, string)) func()
	UnregisterArea(string) error
	RegisterAreas(interface{}, int32) (string, error)
	RegisterFullScreen() (string, error)
}
```


#### type XMouseAreaProxyer

```go
type XMouseAreaProxyer struct {

	// InvalidId信号会在需要相应事件，但目前所持有的鼠标响应区域非法时被触发。
	InvalidId func()
}
```

XMouseAreaProxyer为dde-api中XMouseAreaProxy接口的简单封装，用于触发隐藏dock的显示。
由于之前在C后端调用DBus不方便，因此特意实现了次接口，没有存在的意义，将会被废弃。


#### func (*XMouseAreaProxyer) RegisterAreas

```go
func (a *XMouseAreaProxyer) RegisterAreas(areas []coordinateRange, eventMask int32)
```
RegisterAreas注册多个区域为鼠标可响应区域。 coordinateRange类型为{x0, y0, x1, y1}所表示的矩形区域。 (x0,
y0)表示矩形的左上角，(x1, y1)表示矩形的右下角。

#### func (*XMouseAreaProxyer) RegisterFullScreen

```go
func (a *XMouseAreaProxyer) RegisterFullScreen()
```
RegisterFullScreen将全屏注册为有效的鼠标响应区域。

#### type XidInfo

```go
type XidInfo struct {
	Xid   uint32
	Title string
}
```
