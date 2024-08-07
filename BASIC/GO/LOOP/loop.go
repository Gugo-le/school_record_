package main

import "fmt"

func superAdd(numbers ...int) int {
	for number := range numbers { // range는 인덱스를 줌
		fmt.Println(number)
	}
	return 1
}

func main() {
	superAdd(1, 2, 3, 4, 5, 6)
}
