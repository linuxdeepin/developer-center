package main

import (
	"crypto/hmac"
	"crypto/sha1"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"os/exec"

	"github.com/gin-gonic/contrib/static"
	"github.com/gin-gonic/gin"
)

var (
	Secret = ""
)

func init() {
	js, err := os.Open("conf/docs.json")
	if nil != err {
		panic(err)
	}
	defer js.Close()
	jsdata, _ := ioutil.ReadAll(js)
	var cfg map[string]interface{}
	json.Unmarshal(jsdata, &cfg)
	Secret = fmt.Sprint(cfg["GitHubSecret"])
}

func updateStaticSite() error {
	if err := exec.Command("git", "pull").Run(); nil != err {
		fmt.Println("git pull Failed")
		return err
	}
	if err := exec.Command("python", "./build.py").Run(); nil != err {
		fmt.Println("Build index.md Failed")
		return err
	}

	if err := os.RemoveAll("./site"); nil != err {
		return err
	}

	if out, err := exec.Command("mkdocs", "build").CombinedOutput(); nil != err {
		fmt.Println("mkdocs build Failed", string(out), err)
		return err
	} else {
		fmt.Println(string(out))
	}

	fmt.Println("update successfully")
	os.Exit(1)
	return nil
}

func main() {
	// Test Cfg
	eng := gin.Default()
	eng.POST("hook/github", func(c *gin.Context) {
		sig := c.Request.Header.Get("X-Hub-Signature")
		sig = sig[5:]
		mac := hmac.New(sha1.New, []byte(Secret))
		io.Copy(mac, c.Request.Body)
		expectedMAC := mac.Sum(nil)
		msgSig := hex.EncodeToString(expectedMAC)
		if !hmac.Equal([]byte(msgSig), []byte(sig)) {
			fmt.Println("Signature Error")
			return
		}
		githubPushUpdate()
	})
	eng.Use(static.Serve("/", static.LocalFile("site", false)))

	eng.Run("0.0.0.0:8083")
}
