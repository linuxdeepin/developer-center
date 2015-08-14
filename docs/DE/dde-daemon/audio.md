# Audio Interface Introduction

## 声明结构体

* Port

```go
Name string
Description string
// Unknow:0, No:1, Yes:2
Available byte
```


## Interface: com.deepin.daemon.Audio

###DBusInfo

>Dest: `com.deepin.daemon.Audio`  
>Path: `/com/deepin/daemon/Audio`  
>IFC : `com.deepin.daemon.Audio`

###Properties

* Sinks []*Sink
>Desc: 输出设备 ObjectPath 列表

* Sources []*Source
>Desc: 输入设备 ObjectPath 列表

* SinkInputs []*SinkInput
>Desc: 正在输出声音的程序列表

* DefaultSink string
>Desc: 默认输出设备的名称

* DefaultSource string
>Desc: 默认输入设备的名称

* MaxUIVolume float64
>Desc: 最大音量

###Methods

* Reset()
>Desc: 重置

* GetDefaultSink() (ret0 *Sink)
>ret0: 默认输出设备的 Object
>Desc: 获取默认输出设备

* GetDefaultSource() (ret0 *Source)
>ret0: 默认输入设备的 Object
>Desc: 获取默认输入设备

* SetDefaultSink(name string)
>name: 输出设备的名称
>Desc: 设置默认输出设备

* SetDefaultSource(name string)
>name: 输入设备的名称
>Desc: 设置默认输入设备


--------

## Interface: com.deepin.daemon.Audio.Sink

###DBusInfo

>Dest: `com.deepin.daemon.Audio`  
>Path: `/com/deepin/daemon/Audio/Sink%d`  
>IFC : `com.deepin.daemon.Audio.Sink`

###Properties

* Name string

* Description string

* BaseVolume float64
>Desc: 默认音量

* Mute bool
>Desc: 是否静音

* Volume float64
>Desc: 当前音量

* SupportBalance bool
>Desc: 是否支持左右声道

* Balance float64
>Desc: 左右声道平衡值

* SupportFade bool
>Desc: 是否支持前后声道

* Fade float64
>Desc: 前后声道平衡值

* Ports []Port
>Desc: 支持的输出端口

* ActivePort Port
>Desc: 当前使用的输出端口

###Methods

* SetVolume (v float64, isPlay bool)
>v: 音量大小  
>isPlay: 是否播放声音反馈  
>Desc: 设置音量大小

* SetBalance (v float64, isPlay bool)
>v: 声道平衡值  
>isPlay: 是否播放声音反馈  
>Desc: 设置左右声道平衡值

* SetFade (v float64, isPlay bool)
>v: 声道平衡值  
>isPlay: 是否播放声音反馈  
>Desc: 设置前后声道平衡值

* SetMute (v bool)
>Desc: 设置是否静音

* SetPort (name string)
>Desc: 设置此设备当前使用的端口

--------

## Interface: com.deepin.daemon.Audio.Source

###DBusInfo

>Dest: `com.deepin.daemon.Audio`  
>Path: `/com/deepin/daemon/Audio/Source%d`  
>IFC : `com.deepin.daemon.Audio.Source`

###Properties

* Name string

* Description string

* BaseVolume float64

* Mute bool

* Volume float64

* SupportBalance

* Balance float64

* SupportFade float64

* Fade float64

* Ports []Port

* ActivePort Port

###Methods

* SetVolume (v float64, isPlay bool)

* SetBalance (v float64, isPlay bool)

* SetFade (v float64, isPlay bool)

* SetMute (v float64, isPlay bool)

* SetPort(name string)

--------

## Interface: com.deepin.daemon.Audio.SinkInput

###DBusInfo

>Dest: `com.deepin.daemon.Audio`  
>Path: `/com/deepin/daemon/Audio/SinkInput%d`  
>IFC : `com.deepin.daemon.Audio.SinkInput`

###Properties

* Name string

* Icon string

* Mute bool

* Volume float64

* SupportBalance

* Balance float64

* SupportFade float64

* Fade float64

###Methods

* SetVolume (v float64, isPlay bool)

* SetBalance (v float64, isPlay bool)

* SetFade (v float64, isPlay bool)

* SetMute (v float64, isPlay bool)


--------

## Interface: com.deepin.daemon.Audio.Meter

###DBusInfo

>Dest: `com.deepin.daemon.Audio`  
>Path: `/com/deepin/daemon/Audio/Meter%d`  
>IFC : `com.deepin.daemon.Audio.Meter`

###Properties

* Volume  float64

###Methods

* Tick ()

--------
