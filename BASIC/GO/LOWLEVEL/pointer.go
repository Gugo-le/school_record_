package main

import "fmt"

func main() {
	a := 2
	b := &a
	fmt.Println(*b) // *: 메모리를 살펴봄::훑어봄?
}
