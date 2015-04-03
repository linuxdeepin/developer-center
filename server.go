package main

import (
	"fmt"
	"github.com/gin-gonic/contrib/static"
	"github.com/gin-gonic/gin"
	"os/exec"
)

func updateStaticSite() error {
	if err := exec.Command("git", "pull").Run(); nil != err {
		fmt.Println("git pull Failed")
		return err
	}
	if err := exec.Command("python", "./build.py").Run(); nil != err {
		fmt.Println("Build index.md Failed")
		return err
	}
	if err := exec.Command("mkdocs", "build").Run(); nil != err {
		fmt.Println("mkdocs build Failed")
		return err
	}
	return nil
}

func main() {
	// Test Cfg
	eng := gin.Default()
	eng.POST("hook/github", func(c *gin.Context) {
		updateStaticSite()
	})
	eng.Use(static.Serve("/", static.LocalFile("site", false)))

	eng.Run("0.0.0.0:8083")
}
