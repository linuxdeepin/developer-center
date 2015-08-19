# appearance
--------

Manage desktop appearance

## Usage

```go
const (
	TypeDTheme        string = "dtheme"
	TypeGtkTheme             = "gtk"
	TypeIconTheme            = "icon"
	TypeCursorTheme          = "cursor"
	TypeBackground           = "background"
	TypeStandardFont         = "standardfont"
	TypeMonospaceFont        = "monospacefont"
	TypeFontSize             = "fontsize"
)
```

#### type Theme

subthemes.Theme

```go
type Theme struct {
	Id   string
	Path string

	Deletable bool
}
```


#### type Background

background.Background

```go
type Background struct {
	URI string

	Deletable bool
}
```

#### type Family

fonts.Family

```go
type Family struct {
	Id   string
	Name string

	Styles []string
}
```


#### type DTheme

```go
type DTheme struct {
	Id        string
	Name      string
	Path      string
	Thumbnail string

	Previews []string

	Deletable bool

	Gtk    *subthemes.Theme
	Icon   *subthemes.Theme
	Cursor *subthemes.Theme

	Background *background.Background

	StandardFont  *fonts.Family
	MonospaceFont *fonts.Family
	FontSize      int32
}
```


#### type Manager

```go
type Manager struct {
	// Current desktop theme
	Theme string
	// Current desktop font size
	FontSize int32

	// Theme changed signal
	// ty, name
	Changed func(string, string)
}
```


#### func (*Manager) Delete

```go
func (m *Manager) Delete(ty, name string) error
```
Delete delete the special 'name'


#### func (*Manager) List

```go
func (m *Manager) List(ty string) ([]string, error)
```
List list all available for the special type

#### func (*Manager) Set

```go
func (m *Manager) Set(ty, value string) error
```
Set set to the special 'value'

#### func (*Manager) Show

```go
func (m *Manager) Show(ty, name string) (string, error)
```
Show show detail info for the special type ret0: detail info, json format

#### func (*Manager) Thumbnail

```go
func (m *Manager) Thumbnail(ty, name string) (string, error)
```
Thumbnail get thumbnail for the special 'name'
