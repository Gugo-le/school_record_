package main

import "fmt"

func superAdd(numbers ...int) int {
	total := 0
	for _, number := range numbers { // range는 인덱스를 줌
		total += number // total = total + number
	}
	return total
}

func main() {
	result := superAdd(1, 2, 3, 4, 5, 6)
	fmt.Println(result)
}
