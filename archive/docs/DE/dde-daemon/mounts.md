# mounts
--

## Usage


#### type DiskInfo

```go
type DiskInfo struct {
	// Disk description
	Name string
	// Disk type, ex: native, removable, network...
	Type string

	CanUnmount bool
	CanEject   bool

	// The size of disk used
	Used uint64
	// The capacity of disk
	Size uint64

	Path string
	UUID string
	// The mounted path
	MountPoint string
	Icon       string
}
```


#### type DiskInfos

```go
type DiskInfos []DiskInfo
```


#### type Manager

```go
type Manager struct {
	// All disk info list in system
	DiskList DiskInfos

	// Error(uuid, reason) signal. It will be emited if operation failure
	//
	// uuid: the disk uuid
	// reason: detail info about the failure
	Error func(string, string)
}
```


#### func (*Manager) DeviceEject

```go
func (m *Manager) DeviceEject(uuid string) (bool, error)
```
Eject disk.

uuid: get from DiskList

#### func (*Manager) DeviceMount

```go
func (m *Manager) DeviceMount(uuid string) (bool, error)
```
Mount disk.

#### func (*Manager) DeviceUnmount

```go
func (m *Manager) DeviceUnmount(uuid string) (bool, error)
```
Unmount disk.
