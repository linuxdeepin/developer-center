# langselector
--


## Usage

```go
const (
	// Locale changed state: has been done
	//
	// Locale 更改状态：已经修改完成
	LocaleStateChanged = 0
	// Locale changed state: changing
	//
	// Locale 更改状态：正在修改中
	LocaleStateChanging = 1
)
```

```go
var (
	// Error: not found the file
	//
	// 错误：没有此文件
	ErrFileNotExist = fmt.Errorf("File not exist")
	// Error: not found the locale
	//
	// 错误：无效的 Locale
	ErrLocaleNotFound = fmt.Errorf("Locale not found")
	// Error: changing locale failure
	//
	// 错误：修改 locale 失败
	ErrLocaleChangeFailed = fmt.Errorf("Changing locale failed")
)
```

#### type LangSelector

```go
type LangSelector struct {
	// The current locale
	CurrentLocale string
	// Signal: will be emited if locale changed
	Changed func(locale string)

	// Store locale changed state
	LocaleState int32
}
```

#### type LocaleInfo

```go
type LocaleInfo struct {
	// Locale name
	Locale string
	// Locale description
	Desc string
}
```

#### func (*LangSelector) GetLocaleList

```go
func (lang *LangSelector) GetLocaleList() []LocaleInfo
```
Get locale info list that deepin supported

得到系统支持的 locale 信息列表

#### func (*LangSelector) SetLocale

```go
func (lang *LangSelector) SetLocale(locale string) error
```
Set user desktop environment locale, the new locale will work after relogin.
(Notice: this locale is only for the current user.)

设置用户会话的 locale，注销后生效，此改变只对当前用户生效。

locale: see '/etc/locale.gen'
