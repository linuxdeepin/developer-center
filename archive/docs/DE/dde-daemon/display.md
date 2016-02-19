# display
--

## Usage

```go
const (
	DisplayModeUnknow  = -100
	DisplayModeCustom  = 0
	// 复制屏模式
	DisplayModeMirrors = 1
	// 扩展屏模式
	DisplayModeExtend  = 2
	// 单屏模式
	DisplayModeOnlyOne = 3
)
```


#### type Display

```go
type Display struct {
	// 监视器列表
	Monitors []*Monitor

	// 总宽度
	ScreenWidth  uint16
	// 总高度
	ScreenHeight uint16

	//used by deepin-dock/launcher/desktop
	// 主屏
	Primary        string
	PrimaryRect    xproto.Rectangle
	PrimaryChanged func(xproto.Rectangle)

	// 多屏显示模式
	DisplayMode   int16
	BuiltinOutput *Monitor

	// 是否更改了当前配置
	HasChanged bool

	// 亮度
	Brightness map[string]float64
}
```


#### func (*Display) Apply

```go
func (dpy *Display) Apply()
```

应用当前改变，并弹出确认框等待用户确认

#### func (*Display) AssociateTouchScreen

```go
func (dpy *Display) AssociateTouchScreen(output string, touchscreen string)
```

#### func (*Display) ChangeBrightness

```go
func (dpy *Display) ChangeBrightness(output string, v float64) error
```
The range of brightness value is 0.1~1. Generally speaking user can use media
key to change brightness when the output supports backlight, but we can't rely
on this assumption. If xrandr/acpi driver works, the value of zero is safety.
But if the driver doesn't work well, ChangeBrightness has received a zero value
and then the system will enter an unusable situation.


#### func (*Display) JoinMonitor

```go
func (dpy *Display) JoinMonitor(a string, b string) error
```



#### func (*Display) QueryCurrentPlanName

```go
func (dpy *Display) QueryCurrentPlanName() string
```

#### func (*Display) QueryOutputFeature

```go
func (dpy *Display) QueryOutputFeature(name string) int32
```

是否支持亮度调节，现在只支持这个


#### func (*Display) Reset

```go
func (dpy *Display) Reset()
```

#### func (*Display) ResetBrightness

```go
func (dpy *Display) ResetBrightness(output string)
```

#### func (*Display) ResetChanges

```go
func (dpy *Display) ResetChanges()
```

重置当前改变

用户在确认框选择放弃时，调用此接口


#### func (*Display) SaveChanges

```go
func (dpy *Display) SaveChanges()
```

将当前配置写入文件

当用户在确认框确认后，调用此接口

#### func (*Display) SetBrightness

```go
func (dpy *Display) SetBrightness(output string, v float64) error
```

#### func (*Display) SetPrimary

```go
func (dpy *Display) SetPrimary(name string) error
```

#### func (*Display) SplitMonitor

```go
func (dpy *Display) SplitMonitor(a string) error
```

#### func (*Display) SwitchMode

```go
func (dpy *Display) SwitchMode(mode int16, outputName string)
```

切换显示模式， 见上面 `DisplayMode*` 相关的定义



#### type Mode

```go
type Mode struct {
	ID     uint32
	Width  uint16
	Height uint16
	Rate   float64
}
```

分辨率信息，通过 `ID` 来设置


#### type Modes

```go
type Modes []Mode
```


#### func (Modes) Len


#### type Monitor

```go
type Monitor struct {
	Outputs []string

	BestMode Mode

	// 是否可组合
	IsComposited bool
	Name         string
	FullName     string

	// X 坐标轴起始点
	X int16
	// Y 坐标轴起始点
	Y int16

	// 是否启用
	Opened   bool
	// 屏幕旋转
	Rotation uint16
	// 镜子中的成像
	Reflect  uint16

	CurrentMode Mode

	Width  uint16
	Height uint16
}
```


#### func (*Monitor) ListModes

```go
func (m *Monitor) ListModes() []Mode
```

支持的分辨率列表


#### func (*Monitor) ListReflect

```go
func (m *Monitor) ListReflect() []uint16
```

#### func (*Monitor) ListRotations

```go
func (m *Monitor) ListRotations() []uint16
```

#### func (*Monitor) SetMode

```go
func (m *Monitor) SetMode(id uint32) error
```

设置分辨率


#### func (*Monitor) SetPos

```go
func (m *Monitor) SetPos(x, y int16) error
```

#### func (*Monitor) SetReflect

```go
func (m *Monitor) SetReflect(v uint16) error
```

#### func (*Monitor) SetRotation

```go
func (m *Monitor) SetRotation(v uint16) error
```

#### func (*Monitor) SwitchOn

```go
func (m *Monitor) SwitchOn(v bool) error
```

是否启动监视器
