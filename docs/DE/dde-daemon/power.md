# power
--

handle LidSwitch, PowerButton and Battery status event.

## Usage

```go
const (
	//sync with com.deepin.daemon.power.schemas
	//
	// 按下电源键和合上笔记本盖时支持的操作
	//
	// 关闭显示器
	ActionBlank int32 = 0
	// 挂起
	ActionSuspend = 1
	// 关机
	ActionShutdown = 2
	// 休眠
	ActionHibernate = 3
	// 询问
	ActionInteractive = 4
	// 无
	ActionNothing = 5
	// 注销
	ActionLogout = 6
)
```

```go
const (
	// 高性能模式下空闲检测超时
	HighPerformanceIdleTime = 15 * 60
	// 高性能模式下挂起超时
	HighPerformanceSuspendTime = 0
	// 均衡模式下空闲检测超时
	BlancedIdleTime = 10 * 60
	// 均衡模式下挂起超时
	BlancedSuspendTime = 0
	// 节能模式下空闲检测超时
	PowerSaverIdleTime = 5 * 60
	// 节能模式下挂起超时
	PowerSaverSuspendTime = 15 * 60
)
```

```go
const (
	//sync with com.deepin.daemon.power.schema
	// 电源计划：自定义
	PowerPlanCustom = 0
	// 电源计划：节能模式
	PowerPlanPowerSaver = 1
	// 电源计划：均衡模式
	PowerPlanBalanced = 2
	// 电源计划：高性能模式
	PowerPlanHighPerformance = 3
)
```

```go
const (
	//defined at http://upower.freedesktop.org/docs/Device.html#Device:Type
	DeviceTypeUnknow    = 0
	DeviceTypeLinePower = 1
	DeviceTypeBattery   = 2
	DeviceTypeUps       = 3
	DeviceTypeMonitor   = 4
	DeviceTypeMouse     = 5
	DeviceTypeKeyboard  = 6
	DeviceTypePda       = 7
	DeviceTypePhone     = 8
)
```

```go
const (
	//defined at http://upower.freedesktop.org/docs/Device.html#Device:State
	BatteryStateUnknown          = 0
	BatteryStateCharging         = 1
	BatteryStateDischarging      = 2
	BatteryStateEmpty            = 3
	BatteryStateFullyCharged     = 4
	BatteryStatePendingCharge    = 5
	BatteryStatePendingDischarge = 6
)
```


#### type Power

```go
type Power struct {

	// 按下电源键执行的操作
	PowerButtonAction *property.GSettingsEnumProperty `access:"readwrite"`
	// 合上笔记本盖时执行的操作
	LidClosedAction *property.GSettingsEnumProperty `access:"readwrite"`
	// 屏幕唤醒时是否锁屏
	LockWhenActive *property.GSettingsBoolProperty `access:"readwrite"`

	// 是否有显示器
	LidIsPresent bool

	// 接通电源时的电源计划
	LinePowerPlan *property.GSettingsEnumProperty `access:"readwrite"`
	// 接通电源时的挂起超时
	LinePowerSuspendDelay int32 `access:"readwrite"`
	// 接通电源时的空闲检测超时
	LinePowerIdleDelay int32 `access:"readwrite"`

	// 使用电池时的电源计划
	BatteryPlan *property.GSettingsEnumProperty `access:"readwrite"`
	// 使用电池时的挂起超时
	BatterySuspendDelay int32 `access:"readwrite"`
	// 使用电池时的空闲检测超时
	BatteryIdleDelay int32 `access:"readwrite"`

	// 剩余电量
	BatteryPercentage float64

	//Not in Charging, Charging, Full
	BatteryState uint32

	// 是否有电池设备
	BatteryIsPresent bool

	// 是否使用电池
	OnBattery bool

	// 电源计划列表
	PlanInfo string
}
```

#### func (*Power) Reset

```go
func (p *Power) Reset()
```
