package main

import "fmt"

func main() {
	kevin := map[string]string{"name": "kevin", "age": "18"}
	for key, _ := range kevin {
		fmt.Println(key)
	}
}
