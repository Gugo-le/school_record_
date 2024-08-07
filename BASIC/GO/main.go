package main

import "fmt"

func repeatMe(words ...string) {
	fmt.Println(words)
}

func main() {
	repeatMe("kevin", "ian", "rucas", "sophia", "andreaha")
}
