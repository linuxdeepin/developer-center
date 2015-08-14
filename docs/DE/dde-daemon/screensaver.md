# screensaver
--

## Usage


#### type ScreenSaver

```go
type ScreenSaver struct {

	// Idle 定时器超时信号，当系统在给定时间内未被使用时发送
	IdleOn func()
	// Idle 超时时，如果设置了壁纸切换，则发送此信号
	CycleActive func()
	// Idle 超时后，如果系统被使用就发送此信号，重新开始 Idle 计时器
	IdleOff func()
}
```


#### func (*ScreenSaver) Inhibit

```go
func (ss *ScreenSaver) Inhibit(name, reason string) uint32
```
抑制 Idle 计时器，不再检测系统是否空闲，然后返回一个 id，用来取消此操作。

name: 抑制 Idle 计时器的程序名称

reason: 抑制原因

ret0: 此次操作对应的 id，用来取消抑制

#### func (*ScreenSaver) SetTimeout

```go
func (ss *ScreenSaver) SetTimeout(seconds, interval uint32, blank bool)
```
设置 Idle 的定时器超时时间

seconds: 超时时间，以秒为单位

interval: 屏保模式下，背景更换的间隔时间

blank: 是否黑屏，此参数暂时无效

#### func (*ScreenSaver) SimulateUserActivity

```go
func (ss *ScreenSaver) SimulateUserActivity()
```
模拟用户操作，让系统处于使用状态，重新开始 Idle 定时器

#### func (*ScreenSaver) UnInhibit

```go
func (ss *ScreenSaver) UnInhibit(cookie uint32)
```
根据 id 取消对应的抑制操作
