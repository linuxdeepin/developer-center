package main

// Open url in browser:

import (
	//	_ "pkg.deepin.io/server/docs.deepin.io/oauth2"

	"./router"
	"github.com/Iceyer/gutils/config"
)

type DeepinRestServer struct {
	router *router.Router
	Port   string
}

func (s *DeepinRestServer) Start() {
	s.router = router.StaticRouter()
	host := config.Read(config.KeyServerHost)
	if "" == s.Port {
		s.Port = config.Read(config.KeyServerPort)
	}
	s.router.BootStrap(host + ":" + s.Port)
}
