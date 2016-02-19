# timedate
--


## Usage

#### type ZoneInfo

```go
type ZoneInfo struct {
	// Timezone name, ex: "Asia/Shanghai"
	Name string
	// Timezone description, ex: "China Shanghai"
	Desc string

	// Timezone offset
	Offset int32

	DST DSTInfo
}
```


#### type DSTInfo

```go
type DSTInfo struct {
	// The timestamp of entering DST every year
	Enter int64
	// The timestamp of leaving DST every year
	Leave int64

	// The DST offset
	Offset int32
}
```


#### type Manager

```go
type Manager struct {
	// Whether can use NTP service
	CanNTP bool
	// Whether enable NTP service
	NTP bool
	// Whether set RTC to Local standard
	LocalRTC bool

	// Current timezone
	Timezone string

	// Use 24 hour format to display time
	Use24HourFormat *property.GSettingsBoolProperty `access:"readwrite"`
	// DST offset
	DSTOffset *property.GSettingsIntProperty `access:"readwrite"`
	// User added timezone list
	UserTimezones *property.GSettingsStrvProperty
}
```

#### func (*Manager) AddUserTimezone

```go
func (m *Manager) AddUserTimezone(zone string) error
```
Add the specified time zone to user time zone list.

#### func (*Manager) DeleteUserTimezone

```go
func (m *Manager) DeleteUserTimezone(zone string) error
```
Delete the specified time zone from user time zone list.


#### func (*Manager) GetZoneInfo

```go
func (m *Manager) GetZoneInfo(zone string) (zoneinfo.ZoneInfo, error)
```
Get ZoneInfo of the specified time zone.

#### func (*Manager) GetZoneList

```go
func (m *Manager) GetZoneList() []string
```
Get all ZoneInfo in the specified list.

#### func (*Manager) SetDate

```go
func (m *Manager) SetDate(year, month, day, hour, min, sec, nsec int32) error
```
SetDate Set the system clock to the specified.

The time may be specified in the format '2015' '1' '1' '18' '18' '18' '8'.

#### func (*Manager) SetLocalRTC

```go
func (m *Manager) SetLocalRTC(localRTC, fixSystem bool) error
```
To control whether the RTC is the local time or UTC. Standards are divided into:
localtime and UTC. UTC standard will automatically adjust the daylight saving
time.

实时时间(RTC)是否使用 local 时间标准。时间标准分为 local 和 UTC。 UTC 时间标准会自动根据夏令时而调整系统时间。

localRTC: whether to use local time.

fixSystem: if true, will use the RTC time to adjust the system clock; if false,
the system time is written to the RTC taking the new setting into account.

#### func (*Manager) SetNTP

```go
func (m *Manager) SetNTP(useNTP bool) error
```
To control whether the system clock is synchronized with the network.

useNTP: if true, enable ntp; else disable

#### func (*Manager) SetTime

```go
func (m *Manager) SetTime(usec int64, relative bool) error
```
Set the system clock to the specified.

usec: pass a value of microseconds since 1 Jan 1970 UTC.

relative: if true, the passed usec value will be added to the current system
time; if false, the current system time will be set to the passed usec value.

#### func (*Manager) SetTimezone

```go
func (m *Manager) SetTimezone(zone string) error
```
Set the system time zone to the specified value. timezones you may parse from
/usr/share/zoneinfo/zone.tab.

zone: pass a value like "Asia/Shanghai" to set the timezone.
