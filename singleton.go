package singleton

import "sync"

type singleton struct {
}

var instance *singleton
var once sync.Once

func GetInstance() *singleton {
	if instance==nil {
		once.Do(func() {
			instance = &singleton{}
		})
	}
	return instance
}

/* How to use
ins := GetInstance()
 */
