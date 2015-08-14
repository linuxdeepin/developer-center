# systeminfo
--


## Usage

#### type SystemInfo

```go
type SystemInfo struct {
	// Current version, ex: "2015 Desktop"
	Version string
	// CPU information
	Processor string
	// Disk capacity
	DiskCap uint64
	// Memory size
	MemoryCap uint64
	// System architecture
	SystemType int64
}
```
