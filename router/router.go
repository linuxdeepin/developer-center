package router

import (
	"github.com/Iceyer/gutils/config"
	"github.com/Iceyer/gutils/i18n"
	"github.com/Iceyer/gutils/session"
	"github.com/gin-gonic/contrib/sessions"
	"github.com/gin-gonic/contrib/static"
	"github.com/gin-gonic/gin"
)

type Processer interface {
	Run(*gin.Engine) error
}

type ProcesserHandler func(*gin.Engine) error

type DefaultProcesser struct {
	Handler ProcesserHandler
}

func (p *DefaultProcesser) Run(engine *gin.Engine) error {
	return p.Handler(engine)
}

type Router struct {
	engine     *gin.Engine
	processers []Processer
}

func NewRouter(engine *gin.Engine) *Router {
	return &Router{
		engine: engine,
	}
}

var _staticRouter *Router

func StaticRouter() *Router {
	gin.SetMode(gin.ReleaseMode)
	if nil == _staticRouter {
		eng := gin.Default()
		eng.Use(static.Serve("/article", static.LocalFile("./archive/site", true)))
		eng.Use(static.Serve("/", static.LocalFile("./public", true)))
		store, _ := session.NewLevelDBStore("data/session")
		eng.Use(sessions.Sessions("deepinid_session", store))
		eng.Use(i18n.GinLang("deepin_language", config.Read("RootDomain")))
		_staticRouter = NewRouter(eng)
	}
	return _staticRouter
}

func (r *Router) Plugin(processer Processer) error {
	if nil != processer {
		r.processers = append(r.processers, processer)
		return nil
	}
	panic("Processer must not be nil")
}

func (r *Router) BootStrap(bind string) error {
	for _, p := range r.processers {
		err := p.Run(r.engine)
		if nil != err {
			panic(err)
		}
	}
	r.engine.Run(bind)
	return nil
}
