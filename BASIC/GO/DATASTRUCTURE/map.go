package main

import "fmt"

func main3() {
	kevin := map[string]string{"name": "kevin", "age": "18"}
	for key, value := range kevin {
		fmt.Println(key, value)
	}
}
