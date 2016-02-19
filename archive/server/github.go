package main

import (
	"os"
	"time"
)

var githubLockFile = ".github.lock"

type lock struct {
}

func (l *lock) isLock() bool {
	if _, err := os.Stat(githubLockFile); nil != err {
		return false
	}
	return true
}

func (l *lock) lock() {
	os.Create(githubLockFile)
}

func (l *lock) unlock() {
	os.Remove(githubLockFile)
}

var intval = 180 * time.Second
var t = time.NewTimer(intval)
var l = lock{}

func startRetryDaemon() {
	for {
		select {
		case <-t.C:
			err := updateStaticSite()
			if nil != err {
				t.Reset(intval)
			} else {
				t.Stop()
				l.unlock()
			}

		}
	}
}

func githubPushUpdate() {
	if l.isLock() {
		//kill timer
		t.Stop()
	}
	l.lock()
	err := updateStaticSite()
	if nil != err {
		go startRetryDaemon()
	}
	l.unlock()
}
